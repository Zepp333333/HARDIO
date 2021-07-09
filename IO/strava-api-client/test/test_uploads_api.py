# coding: utf-8

"""
    Strava API v3

    The [Swagger Playground](https://developers.strava.com/playground) is the easiest way to familiarize yourself with the Strava API by submitting HTTP requests and observing the responses before you write any client code. It will show what a response will look like with different endpoints depending on the authorization scope you receive from your athletes. To use the Playground, go to https://www.strava.com/settings/api and change your “Authorization Callback Domain” to developers.strava.com. Please note, we only support Swagger 2.0. There is a known issue where you can only select one scope at a time. For more information, please check the section “client code” at https://developers.strava.com/docs.  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

#  Copyright (c) 2021. Sergei Sazonov. All Rights Reserved

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.uploads_api import UploadsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestUploadsApi(unittest.TestCase):
    """UploadsApi unit test stubs"""

    def setUp(self):
        self.api = UploadsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_upload(self):
        """Test case for create_upload

        Upload DBActivity  # noqa: E501
        """
        pass

    def test_get_upload_by_id(self):
        """Test case for get_upload_by_id

        Get Upload  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
