# -*- coding: utf-8 -*-
"""Authentication classes.
"""
from __future__ import unicode_literals

from datetime import datetime
from typing import Optional, Tuple

from django.conf import settings
from django.contrib.auth.models import User, update_last_login
from django.core.signing import BadSignature
from django.db import DataError
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.utils.translation import ugettext as _

import jwt
from django_digest import HttpDigestAuthenticator
from multidb.pinning import use_master
from oauth2_provider.models import AccessToken
from rest_framework import exceptions
from rest_framework.authentication import (
    BaseAuthentication,
    TokenAuthentication,
    get_authorization_header,
)
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from oauth2_provider.oauth2_validators import OAuth2Validator
from oauth2_provider.settings import oauth2_settings
from oidc.utils import authenticate_sso

from onadata.apps.api.models.temp_token import TempToken
from onadata.apps.api.tasks import send_account_lockout_email
from onadata.libs.utils.cache_tools import (
    LOCKOUT_IP,
    LOGIN_ATTEMPTS,
    cache,
    safe_key,
)
from onadata.libs.utils.common_tags import API_TOKEN
from onadata.libs.utils.email import get_account_lockout_email_data

ENKETO_AUTH_COOKIE = getattr(settings, "ENKETO_AUTH_COOKIE", "__enketo")
JWT_SECRET_KEY = getattr(settings, "JWT_SECRET_KEY", "jwt")
JWT_ALGORITHM = getattr(settings, "JWT_ALGORITHM", "HS256")
TEMP_TOKEN_EXPIRY_TIME = getattr(
    settings, "DEFAULT_TEMP_TOKEN_EXPIRY_TIME", 60 * 60 * 6
)

LOCKOUT_EXCLUDED_PATHS = getattr(
    settings,
    "LOCKOUT_EXCLUDED_PATHS",
    [
        "formList",
        "submission",
        "xformsManifest",
        "xformsMedia",
        "form.xml",
        "submissionList",
        "downloadSubmission",
        "upload",
        "formUpload",
    ],
)


def expired(time_token_created):
    """Checks if the time between when time_token_created and current time
    is greater than the token expiry time.

    :params time_token_created: The time the token we are checking was created.
    :returns: Boolean True if not passed expired time, otherwise False.
    """
    time_diff = (timezone.now() - time_token_created).total_seconds()
    token_expiry_time = TEMP_TOKEN_EXPIRY_TIME

    return True if time_diff > token_expiry_time else False


def get_api_token(cookie_jwt):
    """Get API Token from JSON Web Token"""
    # having this here allows the values to be mocked easily as oppossed to
    # being on the global scope
    try:
        jwt_payload = jwt.decode(
            cookie_jwt, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM]
        )
        api_token = get_object_or_404(Token, key=jwt_payload.get(API_TOKEN))

        return api_token
    except BadSignature as e:
        raise exceptions.AuthenticationFailed(_("Bad Signature: %s" % e))
    except jwt.DecodeError as e:
        raise exceptions.AuthenticationFailed(_("JWT DecodeError: %s" % e))


class DigestAuthentication(BaseAuthentication):
    """Digest authentication
    """

    def __init__(self):
        self.authenticator = HttpDigestAuthenticator()

    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != b"digest":
            return None

        try:
            check_lockout(request)
            if self.authenticator.authenticate(request):
                update_last_login(None, request.user)
                return request.user, None
            else:
                attempts = login_attempts(request)
                remaining_attempts = (
                    getattr(settings, "MAX_LOGIN_ATTEMPTS", 10) - attempts
                )
                raise AuthenticationFailed(
                    _(
                        "Invalid username/password. "
                        "For security reasons, after {} more failed "
                        "login attempts you'll have to wait {} minutes "
                        "before trying again.".format(
                            remaining_attempts,
                            getattr(settings, "LOCKOUT_TIME", 1800) // 60,
                        )
                    )
                )
        except (AttributeError, ValueError, DataError) as e:
            raise AuthenticationFailed(e)

    def authenticate_header(self, request):
        response = self.authenticator.build_challenge_response()

        return response["WWW-Authenticate"]


class TempTokenAuthentication(TokenAuthentication):
    """TempToken authentication using "Authorization: TempToken xxxx" header.
    """

    model = TempToken

    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != b"temptoken":
            return None

        if len(auth) == 1:
            error_msg = _("Invalid token header. No credentials provided.")
            raise exceptions.AuthenticationFailed(error_msg)
        elif len(auth) > 2:
            error_msg = _(
                "Invalid token header. "
                "Token string should not contain spaces."
            )
            raise exceptions.AuthenticationFailed(error_msg)

        return self.authenticate_credentials(auth[1])

    def authenticate_credentials(self, key):
        try:
            if isinstance(key, bytes):
                key = key.decode("utf-8")
            token = self.model.objects.get(key=key)
        except self.model.DoesNotExist:
            invalid_token = True
            if getattr(settings, "SLAVE_DATABASES", []):
                try:
                    with use_master:
                        token = self.model.objects\
                            .select_related("user").get(key=key)
                except self.model.DoesNotExist:
                    invalid_token = True
                else:
                    invalid_token = False
            if invalid_token:
                raise exceptions.AuthenticationFailed(_("Invalid token"))

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed(
                _("User inactive or deleted")
            )

        if expired(token.created):
            raise exceptions.AuthenticationFailed(_("Token expired"))

        return (token.user, token)

    def authenticate_header(self, request):
        return "TempToken"


class EnketoTokenAuthentication(TokenAuthentication):
    """Enketo Token Authentication via JWT shared domain cookie name.
    """

    model = Token

    def authenticate(self, request):
        try:
            cookie_jwt = request.get_signed_cookie(
                ENKETO_AUTH_COOKIE, salt=getattr(settings, "ENKETO_API_SALT")
            )
            api_token = get_api_token(cookie_jwt)

            if getattr(api_token, "user"):
                return api_token.user, api_token
        except self.model.DoesNotExist:
            raise exceptions.AuthenticationFailed(_("Invalid token"))
        except KeyError:
            pass
        except BadSignature:
            # if the cookie wasn't signed it means zebra might have
            # generated it
            cookie_jwt = request.COOKIES.get(ENKETO_AUTH_COOKIE)
            api_token = get_api_token(cookie_jwt)
            if getattr(api_token, "user"):
                return api_token.user, api_token

            raise exceptions.ParseError(
                _("Malformed cookie. Clear your cookies then try again")
            )

        return None


class TempTokenURLParameterAuthentication(TempTokenAuthentication):
    """TempToken URL via temp_token request parameter.
    """

    model = TempToken

    def authenticate(self, request):
        key = request.GET.get("temp_token")
        if not key:
            return None

        return self.authenticate_credentials(key)


class SSOHeaderAuthentication(BaseAuthentication):
    """
    SSO Cookie authentication. Authenticates a user using the SSO
    cookie or HTTP_SSO header.
    """

    def authenticate(self, request):  # pylint: disable=no-self-use
        return authenticate_sso(request)


def retrieve_user_identification(
        request) -> Tuple[Optional[str], Optional[str]]:
    ip = None

    if request.META.get('HTTP_X_REAL_IP'):
        ip = request.META['HTTP_X_REAL_IP'].split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    try:
        if isinstance(request.META["HTTP_AUTHORIZATION"], bytes):
            username = (
                request.META["HTTP_AUTHORIZATION"]
                .decode("utf-8")
                .split('"')[1].strip()
            )
        else:
            username = request.META["HTTP_AUTHORIZATION"].split(
                '"')[1].strip()
    except (TypeError, AttributeError, IndexError):
        pass
    else:
        if not username:
            raise AuthenticationFailed(_("Invalid username"))
        return ip, username
    return None, None


def check_lockout(request) -> Tuple[Optional[str], Optional[str]]:
    """Check request user is not locked out on authentication.

    Returns the username if not locked out, None if request path is in
    LOCKOUT_EXCLUDED_PATHS.
    Raises AuthenticationFailed on lockout.
    """
    uri_path = request.get_full_path()
    if not any(part in LOCKOUT_EXCLUDED_PATHS for part in uri_path.split("/")):
        ip, username = retrieve_user_identification(request)

        if ip and username:
            lockout = cache.get(safe_key("{}{}-{}".format(
                LOCKOUT_IP, ip, username)))
            if lockout:
                time_locked_out = datetime.now() - datetime.strptime(
                    lockout, "%Y-%m-%dT%H:%M:%S"
                )
                remaining_time = round(
                    (
                        getattr(settings, "LOCKOUT_TIME", 1800)
                        - time_locked_out.seconds
                    )
                    / 60
                )
                raise AuthenticationFailed(
                    _(
                        "Locked out. Too many wrong username"
                        "/password attempts. "
                        "Try again in {} minutes.".format(remaining_time)
                    )
                )
            return ip, username
    return None, None


def login_attempts(request):
    """
    Track number of login attempts made by a specific IP within
    a specified amount of time
    """
    ip, username = check_lockout(request)
    attempts_key = safe_key("{}{}-{}".format(LOGIN_ATTEMPTS, ip, username))
    attempts = cache.get(attempts_key)

    if attempts:
        cache.incr(attempts_key)
        attempts = cache.get(attempts_key)
        if attempts >= getattr(settings, "MAX_LOGIN_ATTEMPTS", 10):
            lockout_key = safe_key("{}{}-{}".format(LOCKOUT_IP, ip, username))
            lockout = cache.get(lockout_key)
            if not lockout:
                send_lockout_email(username, ip)
                cache.set(
                    lockout_key,
                    datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
                    getattr(settings, "LOCKOUT_TIME", 1800),
                )
            check_lockout(request)
            return attempts
        return attempts

    cache.set(attempts_key, 1)

    return cache.get(attempts_key)


def send_lockout_email(username, ip):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        pass
    else:
        email_data = get_account_lockout_email_data(username, ip)
        end_email_data = get_account_lockout_email_data(username, ip, end=True)

        send_account_lockout_email.apply_async(
            args=[
                user.email,
                email_data.get("message_txt"),
                email_data.get("subject"),
            ]
        )
        # send end of lockout email 1 minute after lockout time
        send_account_lockout_email.apply_async(
            args=[
                user.email,
                end_email_data.get("message_txt"),
                end_email_data.get("subject"),
            ],
            countdown=getattr(settings, "LOCKOUT_TIME", 1800) + 60,
        )


class MasterReplicaOAuth2Validator(OAuth2Validator):
    """
    Custom OAuth2Validator class that takes into account replication lag
    between Master & Replica databases
    https://github.com/jazzband/django-oauth-toolkit/blob/3bde632d5722f1f85ffcd8277504955321f00fff/oauth2_provider/oauth2_validators.py#L49
    """
    def validate_bearer_token(self, token, scopes, request):
        if not token:
            return False

        introspection_url = oauth2_settings.RESOURCE_SERVER_INTROSPECTION_URL
        introspection_token = oauth2_settings.RESOURCE_SERVER_AUTH_TOKEN
        introspection_credentials = oauth2_settings.\
            RESOURCE_SERVER_INTROSPECTION_CREDENTIALS

        try:
            access_token = AccessToken.objects.select_related(
                "application", "user").get(token=token)
        except AccessToken.DoesNotExist:
            # Try retrieving AccessToken from MasterDB if not available
            # in Read replica
            with use_master:
                try:
                    access_token = AccessToken.objects.select_related(
                        "application", "user").get(token=token)
                except AccessToken.DoesNotExist:
                    access_token = None

        if not access_token or not access_token.is_valid(scopes):
            if introspection_url and (
                    introspection_token or introspection_credentials):
                access_token = self._get_token_from_authentication_server(
                    token,
                    introspection_url,
                    introspection_token,
                    introspection_credentials
                )

        if access_token and access_token.is_valid(scopes):
            request.client = access_token.application
            request.user = access_token.user
            request.scopes = scopes
            request.access_token = access_token
            return True
        else:
            self._set_oauth2_error_on_request(request, access_token, scopes)
            return False
