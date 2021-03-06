# coding: utf-8

"""
    Strava API v3

    The [Swagger Playground](https://developers.strava.com/playground) is the easiest way to familiarize yourself with the Strava API by submitting HTTP requests and observing the responses before you write any client code. It will show what a response will look like with different endpoints depending on the authorization scope you receive from your athletes. To use the Playground, go to https://www.strava.com/settings/api and change your “Authorization Callback Domain” to developers.strava.com. Please note, we only support Swagger 2.0. There is a known issue where you can only select one scope at a time. For more information, please check the section “client code” at https://developers.strava.com/docs.  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class PolylineMap(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'polyline': 'str',
        'summary_polyline': 'str'
    }

    attribute_map = {
        'id': 'id',
        'polyline': 'polyline',
        'summary_polyline': 'summary_polyline'
    }

    def __init__(self, id=None, polyline=None, summary_polyline=None, _configuration=None):  # noqa: E501
        """PolylineMap - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._polyline = None
        self._summary_polyline = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if polyline is not None:
            self.polyline = polyline
        if summary_polyline is not None:
            self.summary_polyline = summary_polyline

    @property
    def id(self):
        """Gets the id of this PolylineMap.  # noqa: E501

        The identifier of the map  # noqa: E501

        :return: The id of this PolylineMap.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PolylineMap.

        The identifier of the map  # noqa: E501

        :param id: The id of this PolylineMap.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def polyline(self):
        """Gets the polyline of this PolylineMap.  # noqa: E501

        The polyline of the map, only returned on detailed representation of an object  # noqa: E501

        :return: The polyline of this PolylineMap.  # noqa: E501
        :rtype: str
        """
        return self._polyline

    @polyline.setter
    def polyline(self, polyline):
        """Sets the polyline of this PolylineMap.

        The polyline of the map, only returned on detailed representation of an object  # noqa: E501

        :param polyline: The polyline of this PolylineMap.  # noqa: E501
        :type: str
        """

        self._polyline = polyline

    @property
    def summary_polyline(self):
        """Gets the summary_polyline of this PolylineMap.  # noqa: E501

        The summary polyline of the map  # noqa: E501

        :return: The summary_polyline of this PolylineMap.  # noqa: E501
        :rtype: str
        """
        return self._summary_polyline

    @summary_polyline.setter
    def summary_polyline(self, summary_polyline):
        """Sets the summary_polyline of this PolylineMap.

        The summary polyline of the map  # noqa: E501

        :param summary_polyline: The summary_polyline of this PolylineMap.  # noqa: E501
        :type: str
        """

        self._summary_polyline = summary_polyline

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PolylineMap, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PolylineMap):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PolylineMap):
            return True

        return self.to_dict() != other.to_dict()
