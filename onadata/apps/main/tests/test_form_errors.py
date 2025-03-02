import os
from unittest import skip

from django.core.files.storage import get_storage_class
from django.urls import reverse
from pyxform.errors import PyXFormError

from onadata.apps.logger.models import XForm
from onadata.apps.main.tests.test_base import TestBase
from onadata.apps.main.views import show
from onadata.libs.utils.logger_tools import XLSFormError


class TestFormErrors(TestBase):

    def _create_xform(self):
        self.xls_path = os.path.join(
            self.this_directory, "fixtures",
            "transportation", "transportation.xls")
        count = XForm.objects.count()
        self._publish_xls_file(self.xls_path)
        self.assertEqual(XForm.objects.count(), count + 1)
        self.xform = XForm.objects.all()[0]

    def test_bad_id_string(self):
        self._create_user_and_login()
        count = XForm.objects.count()
        xls_path = os.path.join(self.this_directory, "fixtures",
                                "transportation", "transportation.bad_id.xls")
        self.assertRaises(XLSFormError, self._publish_xls_file, xls_path)
        self.assertEquals(XForm.objects.count(), count)

    @skip
    def test_dl_no_xls(self):
        """
        Exports are built from the JSON form structure so we dont need the
        xls to generate an export
        """
        self._create_xform()
        self.xform.shared_data = True
        self.xform.save()
        default_storage = get_storage_class()()
        path = self.xform.xls.name
        self.assertEqual(default_storage.exists(path), True)
        default_storage.delete(path)
        self.assertEqual(default_storage.exists(path), False)
        url = reverse('xls_export', kwargs={'username': self.user.username,
                      'id_string': self.xform.id_string})
        response = self.anon.get(url)
        self.assertEqual(response.status_code, 404)

    def test_dl_xls_not_file(self):
        self._create_xform()
        self.xform.xls = "blah"
        self.xform.save()
        url = reverse('xls_export', kwargs={'username': self.user.username,
                      'id_string': self.xform.id_string})
        response = self.anon.get(url)
        self.assertEqual(response.status_code, 403)

    def test_nonexist_id_string(self):
        url = reverse(show, kwargs={'username': self.user.username,
                                    'id_string': '4444'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        response = self.anon.get(url)
        self.assertEqual(response.status_code, 404)

    def test_empty_submission(self):
        xls_path = os.path.join(
            self.this_directory, "fixtures",
            "transportation", "transportation.xls")
        xml_path = os.path.join(
            self.this_directory, "fixtures",
            "transportation", "transportation_empty_submission.xml")
        self._publish_xls_file(xls_path)
        self._make_submission(xml_path)
        self.assertTrue(self.response.status_code, 400)

    def test_submission_deactivated(self):
        self._create_xform()
        self.xform.downloadable = False
        self.xform.save()
        xml_path = os.path.join(
            self.this_directory, "fixtures",
            "transportation", "transportation_empty_submission.xml")
        self._make_submission(xml_path)
        self.assertTrue(self.response.status_code, 400)

    def test_spaced_xlsform(self):
        self._create_xform()
        count = XForm.objects.count()
        self.xform.save()
        xls_path = os.path.join(self.this_directory, "fixtures",
                                "transportation", "tutorial .xls")
        msg = ("In strict mode, the XForm ID must be a valid slug"
               " and contain no spaces. Please ensure that you "
               "have set an id_string in the settings sheet or"
               " have modified the filename to not contain any spaces.")
        self.assertRaisesMessage(
            XLSFormError, msg, self._publish_xls_file, xls_path)
        self.assertEquals(XForm.objects.count(), count)

    def test_choice_duplicate_error(self):
        """
        Test that the choice duplicate error is raised if
        the "allow_choice_duplicates" setting is not set in the
        forms settings sheet
        """
        count = XForm.objects.count()
        xls_path = os.path.join(
            self.this_directory, 'fixtures', 'cascading_selects',
            'duplicate_choice_form.xls')
        msg = (
            "The name column for the 'counties' choice list"
            " contains these duplicates: 'king'. Duplicate "
            "names will be impossible to identify in analysis"
            " unless a previous value in a cascading select "
            "differentiates them. If this is intentional, "
            "you can set the allow_choice_duplicates "
            "setting to 'yes'. "
            "Learn more: https://xlsform.org/#choice-names.")
        self.assertRaisesMessage(
            PyXFormError, msg, self._publish_xls_file, xls_path)
        self.assertEquals(XForm.objects.count(), count)
