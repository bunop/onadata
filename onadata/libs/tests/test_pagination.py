"""
Tests onadata.libs.pagination module
"""
from django.http.request import HttpRequest

from rest_framework.request import Request

from onadata.apps.main.tests.test_base import TestBase
from onadata.apps.logger.models import Instance
from onadata.libs.pagination import StandardPageNumberPagination


class TestPaginationModule(TestBase):
    """
    Tests for onadata.libs.pagination module
    """

    def test_generate_link_header_function(self):
        req = HttpRequest()
        req.META['SERVER_NAME'] = 'testserver'
        req.META['SERVER_PORT'] = '80'
        req.META['QUERY_STRING'] = "page=1&page_size=1"
        req.GET = {"page": 1, "page_size": 1}
        self._publish_transportation_form()
        self._make_submissions()
        qs = Instance.objects.filter(xform=self.xform)
        out = StandardPageNumberPagination().generate_link_header(
            Request(req), qs
        )
        expected_out = {
            'Link': '<http://testserver?page=2&page_size=1>; rel="next",'
                    ' <http://testserver?page=4&page_size=1>; rel="last"'
        }
        self.assertEqual(out, expected_out)

        # First page link is created when not on the first page
        req.META['QUERY_STRING'] = "page=2&page_size=1"
        req.GET = {"page": 2, "page_size": 1}
        out = StandardPageNumberPagination().generate_link_header(
            Request(req), qs
        )
        expected_out = {
            'Link': '<http://testserver?page_size=1>; rel="prev", '
                    '<http://testserver?page=3&page_size=1>; rel="next", '
                    '<http://testserver?page=4&page_size=1>; rel="last", '
                    '<http://testserver?page=1&page_size=1>; rel="first"'}
        self.assertEqual(out, expected_out)

        # Last page link is not created on last page
        req.META['QUERY_STRING'] = "page=4&page_size=1"
        req.GET = {"page": 4, "page_size": 1}
        out = StandardPageNumberPagination().generate_link_header(
            Request(req), qs
        )
        expected_out = {
            'Link': '<http://testserver?page=3&page_size=1>; rel="prev", '
                    '<http://testserver?page=1&page_size=1>; rel="first"'}
        self.assertEqual(out, expected_out)
