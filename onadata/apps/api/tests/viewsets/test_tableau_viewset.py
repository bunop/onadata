# -*- coding: utf-8 -*-
"""
OpenData tests.
"""
import os
import json
from re import search
from django.test import RequestFactory
from tempfile import NamedTemporaryFile
from django.utils.dateparse import parse_datetime
from onadata.apps.main.tests.test_base import TestBase
from onadata.apps.logger.models.open_data import get_or_create_opendata
from onadata.apps.api.viewsets.v2.tableau_viewset import (
    TableauViewSet, unpack_select_multiple_data,
    unpack_gps_data, clean_xform_headers)
from onadata.libs.renderers.renderers import pairing


def streaming_data(response):
    return json.loads(u''.join(
        [i.decode('utf-8') for i in response.streaming_content]))


class TestTableauViewSet(TestBase):

    def setUp(self):
        super(TestTableauViewSet, self).setUp()
        self._create_user_and_login()
        self._submission_time = parse_datetime('2020-02-18 15:54:01Z')
        self.fixture_dir = os.path.join(
            self.this_directory, 'fixtures', 'csv_export')
        path = os.path.join(self.fixture_dir, 'tutorial_w_repeats.xls')
        self._publish_xls_file_and_set_xform(path)
        path = os.path.join(self.fixture_dir, 'repeats_sub.xml')
        self.factory = RequestFactory()
        self.extra = {
            'HTTP_AUTHORIZATION': 'Token %s' % self.user.auth_token}
        self._make_submission(
            path, forced_submission_time=self._submission_time)

        self.view = TableauViewSet.as_view({
            'post': 'create',
            'patch': 'partial_update',
            'delete': 'destroy',
            'get': 'data'
        })

    def get_open_data_object(self):
        return get_or_create_opendata(self.xform)[0]

    def test_tableau_data_and_fetch(self):  # pylint: disable=invalid-name
        """
        Test the schema and data endpoint and data returned by each.
        """
        self.view = TableauViewSet.as_view({
            'get': 'schema'
        })

        _open_data = get_or_create_opendata(self.xform)
        uuid = _open_data[0].uuid
        expected_schema = [
            {
                'table_alias': 'data',
                'connection_name': f'{self.xform.project_id}_{self.xform.id_string}',  # noqa
                'column_headers': [
                    {
                        'id': '_id',
                        'dataType': 'int',
                        'alias': '_id'
                    },
                    {
                        'id': 'name',
                        'dataType': 'string',
                        'alias': 'name'
                    },
                    {
                        'id': 'age',
                        'dataType': 'int',
                        'alias': 'age'
                    },
                    {
                        'id': 'picture',
                        'dataType': 'string',
                        'alias': 'picture'
                    },
                    {
                        'id': 'has_children',
                        'dataType': 'string',
                        'alias': 'has_children'
                    },
                    {
                        'id': '_gps_latitude',
                        'dataType': 'string',
                        'alias': '_gps_latitude'
                    },
                    {
                        'id': '_gps_longitude',
                        'dataType': 'string',
                        'alias': '_gps_longitude'
                    },
                    {
                        'id': '_gps_altitude',
                        'dataType': 'string',
                        'alias': '_gps_altitude'
                    },
                    {
                        'id': '_gps_precision',
                        'dataType': 'string',
                        'alias': '_gps_precision'
                    },
                    {
                        'id': 'browsers_firefox',
                        'dataType': 'string',
                        'alias': 'browsers_firefox'
                    },
                    {
                        'id': 'browsers_chrome',
                        'dataType': 'string',
                        'alias': 'browsers_chrome'
                    },
                    {
                        'id': 'browsers_ie',
                        'dataType': 'string',
                        'alias': 'browsers_ie'
                    },
                    {
                        'id': 'browsers_safari',
                        'dataType': 'string',
                        'alias': 'browsers_safari'
                    },
                    {
                        'id': 'meta_instanceID',
                        'dataType': 'string',
                        'alias': 'meta_instanceID'
                    }
                ]
            },
            {
                'table_alias': 'children',
                'connection_name': f'{self.xform.project_id}_{self.xform.id_string}_children',  # noqa
                'column_headers': [
                    {
                        'id': '_id',
                        'dataType': 'int',
                        'alias': '_id'
                    },
                    {
                        'id': '__parent_id',
                        'dataType': 'int',
                        'alias': '__parent_id'
                    },
                    {
                        'id': '__parent_table',
                        'dataType': 'string',
                        'alias': '__parent_table'
                    },
                    {
                        'id': 'childs_name',
                        'dataType': 'string',
                        'alias': 'childs_name'
                    },
                    {
                        'id': 'childs_age',
                        'dataType': 'int',
                        'alias': 'childs_age'
                    }
                    ]
                }]

        request1 = self.factory.get('/', **self.extra)
        response1 = self.view(request1, uuid=uuid)
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response1.data, expected_schema)
        # Test that multiple schemas are generated for each repeat
        self.assertEqual(len(response1.data), 2)
        self.assertListEqual(
            ['column_headers', 'connection_name', 'table_alias'],
            sorted(list(response1.data[0].keys()))
        )

        connection_name = f'{self.xform.project_id}_{self.xform.id_string}'
        self.assertEqual(
            connection_name, response1.data[0].get('connection_name'))
        # Test that the table alias field being sent to Tableau
        # for each schema contains the right table name
        self.assertEqual(
            u'data', response1.data[0].get('table_alias')
        )
        self.assertEqual(
            u'children', response1.data[1].get('table_alias')
        )

        _id_datatype = [
            a.get('dataType')
            for a in response1.data[0]['column_headers']
            if a.get('id') == '_id'][0]
        self.assertEqual(_id_datatype, 'int')

        self.view = TableauViewSet.as_view({
            'get': 'data'
        })
        request2 = self.factory.get('/', **self.extra)
        response2 = self.view(request2, uuid=uuid)
        self.assertEqual(response2.status_code, 200)

        # cast generator response to list for easy manipulation
        row_data = streaming_data(response2)
        expected_data = [
            {
                '_gps_altitude': '0',
                '_gps_latitude': '26.431228',
                '_gps_longitude': '58.157921',
                '_gps_precision': '0',
                '_id': self.xform.instances.first().id,
                'age': 32,
                'browsers_chrome': 'TRUE',
                'browsers_firefox': 'TRUE',
                'browsers_ie': 'TRUE',
                'browsers_safari': 'TRUE',
                'children': [
                    {
                        '__parent_id': self.xform.instances.first().id,
                        '__parent_table': 'data',
                        '_id': int(pairing(
                            self.xform.instances.first().id, 1)),
                        'childs_age': 2,
                        'childs_name': 'Harry'},
                    {
                        '__parent_id': self.xform.instances.first().id,
                        '__parent_table': 'data',
                        '_id': int(pairing(
                            self.xform.instances.first().id, 2)),
                        'childs_age': 5,
                        'childs_name': 'Potter'}],
                'has_children': '1',
                'name': 'Tom',
                'picture': 'wotm_01_green_desktop-10_36_1.jpg'
            }]

        # Test to confirm that the repeat tables generated
        # are related to the main table
        self.assertEqual(
            row_data[0]['children'][0]['__parent_table'],
            response1.data[0]['table_alias'])
        self.assertEqual(row_data, expected_data)

    def test_unpack_select_multiple_data(self):
        """
        Test expected output when `unpack_select_multiple_data`
        function is run.
        """
        picked_choices = ['firefox', 'chrome', 'ie', 'safari']
        list_name = 'browsers'
        choices_names = ['firefox', 'chrome', 'ie', 'safari']
        prefix = ''

        expected_data = {
            'browsers_chrome': 'TRUE',
            'browsers_firefox': 'TRUE',
            'browsers_ie': 'TRUE',
            'browsers_safari': 'TRUE'
            }

        select_multiple_data = unpack_select_multiple_data(
            picked_choices, list_name, choices_names, prefix)
        self.assertEqual(select_multiple_data, expected_data)

        # Confirm expected data when 2 choices are selected
        picked_choices = ['firefox', 'safari']

        select_multiple_data = unpack_select_multiple_data(
            picked_choices, list_name, choices_names, prefix)

        expected_data = {
            'browsers_chrome': 'FALSE',
            'browsers_firefox': 'TRUE',
            'browsers_ie': 'FALSE',
            'browsers_safari': 'TRUE'
            }

        self.assertEqual(select_multiple_data, expected_data)

    def test_unpack_gps_data(self):
        """
        Test that gps data is unpacked into 4 separate columns
        specific to latitude, longitude, alitude and precision.
        """
        # We receive gps data as a string
        # with 4 space separated values
        gps_data = '26.431228 58.157921 0 0'

        qstn_name = "gps"
        prefix = ""
        data = unpack_gps_data(
            gps_data, qstn_name, prefix)
        expected_data = {
            '_gps_latitude': '26.431228',
            '_gps_longitude': '58.157921',
            '_gps_altitude': '0',
            '_gps_precision': '0'
            }
        self.assertEqual(data, expected_data)

    def test_clean_xform_headers(self):
        """
        Test that column header fields for group columns
        do not contain indexing when schema columns
        are being pushed to Tableau.
        """
        headers = self.xform.get_headers(repeat_iterations=1)
        group_columns = [
            field for field in headers if search(r"\[+\d+\]", field)]
        self.assertEqual(group_columns,
                         ['children[1]/childs_name',
                          'children[1]/childs_age'])

        cleaned_data = clean_xform_headers(group_columns)
        self.assertEqual(cleaned_data,
                         ['childs_name', 'childs_age'])

    def test_replace_media_links(self):
        """
        Test that attachment details exported to Tableau contains
        media file download links instead of the file name.
        """
        images_md = """
        | survey |
        |        | type  | name   | label |
        |        | photo | image1 | Pic 1 |
        """
        xform_w_attachments = self._publish_markdown(images_md, self.user)
        submission_file = NamedTemporaryFile(delete=False)
        with open(submission_file.name, 'w') as xml_file:
            xml_file.write(
                "<?xml version='1.0'?><data id=\"%s\">"
                "<image1>1335783522563.jpg</image1>"
                "<image2>1442323232322.jpg</image2>"
                "<meta><instanceID>uuid:729f173c688e482486a48661700455ff"
                "</instanceID></meta></data>" %
                (xform_w_attachments.id_string))
        media_file = "1335783522563.jpg"
        self._make_submission_w_attachment(
            submission_file.name,
            os.path.join(self.this_directory, 'fixtures', 'transportation',
                         'instances', self.surveys[0], media_file))
        submission_data = xform_w_attachments.instances.first().json
        _open_data = get_or_create_opendata(xform_w_attachments)
        uuid = _open_data[0].uuid
        request = self.factory.get('/', **self.extra)
        response = self.view(request, uuid=uuid)
        self.assertEqual(response.status_code, 200)
        # cast generator response to list for easy manipulation
        row_data = streaming_data(response)
        self.assertEqual(
            row_data[0]['image1'],
            f"example.com{submission_data['_attachments'][0]['download_url']}")
