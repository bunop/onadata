from django.core.exceptions import MultipleObjectsReturned
from django.utils import timezone
from django.utils.decorators import classonlymethod
from django.utils.translation import ugettext as _
from django.views.decorators.cache import never_cache
from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework import mixins
from multidb.pinning import use_master

from onadata.apps.api.models.odk_token import ODKToken
from onadata.apps.api.models.temp_token import TempToken
from onadata.apps.api.permissions import ConnectViewsetPermissions
from onadata.apps.api.viewsets.user_profile_viewset import \
    serializer_from_settings
from onadata.apps.main.models.user_profile import UserProfile
from onadata.libs.mixins.authenticate_header_mixin import \
    AuthenticateHeaderMixin
from onadata.libs.mixins.cache_control_mixin import CacheControlMixin
from onadata.libs.mixins.etags_mixin import ETagsMixin
from onadata.libs.mixins.object_lookup_mixin import ObjectLookupMixin
from onadata.libs.serializers.password_reset_serializer import (
    PasswordResetChangeSerializer, PasswordResetSerializer, get_user_from_uid)
from onadata.libs.serializers.project_serializer import ProjectSerializer
from onadata.libs.serializers.user_profile_serializer import \
    UserProfileWithTokenSerializer
from onadata.settings.common import DEFAULT_SESSION_EXPIRY_TIME
from onadata.libs.utils.cache_tools import (cache,
                                            USER_PROFILE_PREFIX)


def user_profile_w_token_response(request, status):
    """ Returns authenticated user profile"""

    if request and not request.user.is_anonymous:
        session = getattr(request, "session")
        if not session.session_key:
            # login user to create session token
            # TODO cannot call this without calling authenticate first or
            # setting the backend, commented for now.
            # login(request, request.user)
            session.set_expiry(DEFAULT_SESSION_EXPIRY_TIME)

    try:
        user_profile = request.user.profile
    except UserProfile.DoesNotExist:
        user_profile = cache.get(
            f'{USER_PROFILE_PREFIX}{request.user.username}')
        if not user_profile:
            with use_master:
                user_profile, _ = UserProfile.objects.get_or_create(
                    user=request.user)
                serializer = serializer_from_settings()(
                    user_profile,
                    context={'request': request})
                cache.set(
                    f'{USER_PROFILE_PREFIX}{request.user.username}',
                    serializer.data)

    serializer = UserProfileWithTokenSerializer(
        instance=user_profile, context={"request": request})

    return Response(serializer.data, status=status)


class ConnectViewSet(mixins.CreateModelMixin, AuthenticateHeaderMixin,
                     CacheControlMixin, ETagsMixin, ObjectLookupMixin,
                     viewsets.GenericViewSet):
    """
    This endpoint allows you retrieve the authenticated user's profile info.
    """
    lookup_field = 'user'
    queryset = UserProfile.objects.all()
    permission_classes = (ConnectViewsetPermissions, )
    serializer_class = UserProfileWithTokenSerializer

    # pylint: disable=R0201
    def create(self, request, *args, **kwargs):
        return user_profile_w_token_response(request, status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        return user_profile_w_token_response(request, status.HTTP_200_OK)

    @action(methods=['GET'], detail=True)
    def starred(self, request, *args, **kwargs):
        """Return projects starred for this user."""
        user_profile = self.get_object()
        user = user_profile.user
        projects = user.project_stars.all()
        serializer = ProjectSerializer(
            projects, context={'request': request}, many=True)

        return Response(data=serializer.data)

    @action(methods=['POST'], detail=False)
    def reset(self, request, *args, **kwargs):
        context = {'request': request}
        data = request.data if request.data is not None else {}
        if 'token' in request.data:
            serializer = PasswordResetChangeSerializer(
                data=data, context=context)

            if serializer.is_valid():
                serializer.save()
                user = get_user_from_uid(serializer.data['uid'])
                return Response(data={'username': user.username},
                                status=status.HTTP_200_OK)
        else:
            serializer = PasswordResetSerializer(data=data, context=context)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['DELETE'], detail=False)
    def expire(self, request, *args, **kwargs):
        try:
            TempToken.objects.get(user=request.user).delete()
        except TempToken.DoesNotExist:
            raise ParseError(_(u"Temporary token not found!"))

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['GET'], detail=False)
    def regenerate_auth_token(self, request, *args, **kwargs):
        try:
            Token.objects.get(user=request.user).delete()
        except Token.DoesNotExist:
            raise ParseError(_(u" Token not found!"))

        new_token = Token.objects.create(user=request.user)

        return Response(data=new_token.key, status=status.HTTP_201_CREATED)

    @action(methods=['GET', 'POST'], detail=False)
    def odk_token(self, request, *args, **kwargs):
        user = request.user

        if request.method == 'GET':
            try:
                token, created = ODKToken.objects.get_or_create(
                    user=user, status=ODKToken.ACTIVE)

                if not created and timezone.now() > token.expires:
                    token.status = ODKToken.INACTIVE
                    token.save()
                    token = ODKToken.objects.create(user=user)
            except MultipleObjectsReturned:
                ODKToken.objects.filter(
                    user=user, status=ODKToken.ACTIVE).update(
                        status=ODKToken.INACTIVE)
                token = ODKToken.objects.create(user=user)

            return Response(data={
                'odk_token': token.raw_key,
                'expires': token.expires}, status=status.HTTP_200_OK)
        elif request.method == 'POST':
            # Regenerates the ODK Token if one is already existant
            ODKToken.objects.filter(
                user=user, status=ODKToken.ACTIVE).update(
                    status=ODKToken.INACTIVE)

            token = ODKToken.objects.create(user=user)

            return Response(data={
                'odk_token': token.raw_key,
                'expires': token.expires
            }, status=status.HTTP_201_CREATED)

    @classonlymethod
    def as_view(cls, actions=None, **initkwargs):
        view = super(ConnectViewSet, cls).as_view(actions, **initkwargs)

        return never_cache(view)
