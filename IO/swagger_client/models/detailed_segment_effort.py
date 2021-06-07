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
from swagger_client.models.summary_segment_effort import SummarySegmentEffort  # noqa: F401,E501

class DetailedSegmentEffort(SummarySegmentEffort):
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
        'name': 'str',
        'activity': 'MetaActivity',
        'athlete': 'MetaAthlete',
        'moving_time': 'int',
        'start_index': 'int',
        'end_index': 'int',
        'average_cadence': 'float',
        'average_watts': 'float',
        'device_watts': 'bool',
        'average_heartrate': 'float',
        'max_heartrate': 'float',
        'segment': 'SummarySegment',
        'kom_rank': 'int',
        'pr_rank': 'int',
        'hidden': 'bool'
    }
    if hasattr(SummarySegmentEffort, "swagger_types"):
        swagger_types.update(SummarySegmentEffort.swagger_types)

    attribute_map = {
        'name': 'name',
        'activity': 'activity',
        'athlete': 'athlete',
        'moving_time': 'moving_time',
        'start_index': 'start_index',
        'end_index': 'end_index',
        'average_cadence': 'average_cadence',
        'average_watts': 'average_watts',
        'device_watts': 'device_watts',
        'average_heartrate': 'average_heartrate',
        'max_heartrate': 'max_heartrate',
        'segment': 'segment',
        'kom_rank': 'kom_rank',
        'pr_rank': 'pr_rank',
        'hidden': 'hidden'
    }
    if hasattr(SummarySegmentEffort, "attribute_map"):
        attribute_map.update(SummarySegmentEffort.attribute_map)

    def __init__(self, name=None, activity=None, athlete=None, moving_time=None, start_index=None, end_index=None, average_cadence=None, average_watts=None, device_watts=None, average_heartrate=None, max_heartrate=None, segment=None, kom_rank=None, pr_rank=None, hidden=None, *args, **kwargs):  # noqa: E501
        """DetailedSegmentEffort - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._activity = None
        self._athlete = None
        self._moving_time = None
        self._start_index = None
        self._end_index = None
        self._average_cadence = None
        self._average_watts = None
        self._device_watts = None
        self._average_heartrate = None
        self._max_heartrate = None
        self._segment = None
        self._kom_rank = None
        self._pr_rank = None
        self._hidden = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if activity is not None:
            self.activity = activity
        if athlete is not None:
            self.athlete = athlete
        if moving_time is not None:
            self.moving_time = moving_time
        if start_index is not None:
            self.start_index = start_index
        if end_index is not None:
            self.end_index = end_index
        if average_cadence is not None:
            self.average_cadence = average_cadence
        if average_watts is not None:
            self.average_watts = average_watts
        if device_watts is not None:
            self.device_watts = device_watts
        if average_heartrate is not None:
            self.average_heartrate = average_heartrate
        if max_heartrate is not None:
            self.max_heartrate = max_heartrate
        if segment is not None:
            self.segment = segment
        if kom_rank is not None:
            self.kom_rank = kom_rank
        if pr_rank is not None:
            self.pr_rank = pr_rank
        if hidden is not None:
            self.hidden = hidden
        SummarySegmentEffort.__init__(self, *args, **kwargs)

    @property
    def name(self):
        """Gets the name of this DetailedSegmentEffort.  # noqa: E501

        The name of the segment on which this effort was performed  # noqa: E501

        :return: The name of this DetailedSegmentEffort.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DetailedSegmentEffort.

        The name of the segment on which this effort was performed  # noqa: E501

        :param name: The name of this DetailedSegmentEffort.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def activity(self):
        """Gets the activity of this DetailedSegmentEffort.  # noqa: E501


        :return: The activity of this DetailedSegmentEffort.  # noqa: E501
        :rtype: MetaActivity
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """Sets the activity of this DetailedSegmentEffort.


        :param activity: The activity of this DetailedSegmentEffort.  # noqa: E501
        :type: MetaActivity
        """

        self._activity = activity

    @property
    def athlete(self):
        """Gets the athlete of this DetailedSegmentEffort.  # noqa: E501


        :return: The athlete of this DetailedSegmentEffort.  # noqa: E501
        :rtype: MetaAthlete
        """
        return self._athlete

    @athlete.setter
    def athlete(self, athlete):
        """Sets the athlete of this DetailedSegmentEffort.


        :param athlete: The athlete of this DetailedSegmentEffort.  # noqa: E501
        :type: MetaAthlete
        """

        self._athlete = athlete

    @property
    def moving_time(self):
        """Gets the moving_time of this DetailedSegmentEffort.  # noqa: E501

        The effort's moving time  # noqa: E501

        :return: The moving_time of this DetailedSegmentEffort.  # noqa: E501
        :rtype: int
        """
        return self._moving_time

    @moving_time.setter
    def moving_time(self, moving_time):
        """Sets the moving_time of this DetailedSegmentEffort.

        The effort's moving time  # noqa: E501

        :param moving_time: The moving_time of this DetailedSegmentEffort.  # noqa: E501
        :type: int
        """

        self._moving_time = moving_time

    @property
    def start_index(self):
        """Gets the start_index of this DetailedSegmentEffort.  # noqa: E501

        The start index of this effort in its activity's stream  # noqa: E501

        :return: The start_index of this DetailedSegmentEffort.  # noqa: E501
        :rtype: int
        """
        return self._start_index

    @start_index.setter
    def start_index(self, start_index):
        """Sets the start_index of this DetailedSegmentEffort.

        The start index of this effort in its activity's stream  # noqa: E501

        :param start_index: The start_index of this DetailedSegmentEffort.  # noqa: E501
        :type: int
        """

        self._start_index = start_index

    @property
    def end_index(self):
        """Gets the end_index of this DetailedSegmentEffort.  # noqa: E501

        The end index of this effort in its activity's stream  # noqa: E501

        :return: The end_index of this DetailedSegmentEffort.  # noqa: E501
        :rtype: int
        """
        return self._end_index

    @end_index.setter
    def end_index(self, end_index):
        """Sets the end_index of this DetailedSegmentEffort.

        The end index of this effort in its activity's stream  # noqa: E501

        :param end_index: The end_index of this DetailedSegmentEffort.  # noqa: E501
        :type: int
        """

        self._end_index = end_index

    @property
    def average_cadence(self):
        """Gets the average_cadence of this DetailedSegmentEffort.  # noqa: E501

        The effort's average cadence  # noqa: E501

        :return: The average_cadence of this DetailedSegmentEffort.  # noqa: E501
        :rtype: float
        """
        return self._average_cadence

    @average_cadence.setter
    def average_cadence(self, average_cadence):
        """Sets the average_cadence of this DetailedSegmentEffort.

        The effort's average cadence  # noqa: E501

        :param average_cadence: The average_cadence of this DetailedSegmentEffort.  # noqa: E501
        :type: float
        """

        self._average_cadence = average_cadence

    @property
    def average_watts(self):
        """Gets the average_watts of this DetailedSegmentEffort.  # noqa: E501

        The average wattage of this effort  # noqa: E501

        :return: The average_watts of this DetailedSegmentEffort.  # noqa: E501
        :rtype: float
        """
        return self._average_watts

    @average_watts.setter
    def average_watts(self, average_watts):
        """Sets the average_watts of this DetailedSegmentEffort.

        The average wattage of this effort  # noqa: E501

        :param average_watts: The average_watts of this DetailedSegmentEffort.  # noqa: E501
        :type: float
        """

        self._average_watts = average_watts

    @property
    def device_watts(self):
        """Gets the device_watts of this DetailedSegmentEffort.  # noqa: E501

        For riding efforts, whether the wattage was reported by a dedicated recording device  # noqa: E501

        :return: The device_watts of this DetailedSegmentEffort.  # noqa: E501
        :rtype: bool
        """
        return self._device_watts

    @device_watts.setter
    def device_watts(self, device_watts):
        """Sets the device_watts of this DetailedSegmentEffort.

        For riding efforts, whether the wattage was reported by a dedicated recording device  # noqa: E501

        :param device_watts: The device_watts of this DetailedSegmentEffort.  # noqa: E501
        :type: bool
        """

        self._device_watts = device_watts

    @property
    def average_heartrate(self):
        """Gets the average_heartrate of this DetailedSegmentEffort.  # noqa: E501

        The heart heart rate of the athlete during this effort  # noqa: E501

        :return: The average_heartrate of this DetailedSegmentEffort.  # noqa: E501
        :rtype: float
        """
        return self._average_heartrate

    @average_heartrate.setter
    def average_heartrate(self, average_heartrate):
        """Sets the average_heartrate of this DetailedSegmentEffort.

        The heart heart rate of the athlete during this effort  # noqa: E501

        :param average_heartrate: The average_heartrate of this DetailedSegmentEffort.  # noqa: E501
        :type: float
        """

        self._average_heartrate = average_heartrate

    @property
    def max_heartrate(self):
        """Gets the max_heartrate of this DetailedSegmentEffort.  # noqa: E501

        The maximum heart rate of the athlete during this effort  # noqa: E501

        :return: The max_heartrate of this DetailedSegmentEffort.  # noqa: E501
        :rtype: float
        """
        return self._max_heartrate

    @max_heartrate.setter
    def max_heartrate(self, max_heartrate):
        """Sets the max_heartrate of this DetailedSegmentEffort.

        The maximum heart rate of the athlete during this effort  # noqa: E501

        :param max_heartrate: The max_heartrate of this DetailedSegmentEffort.  # noqa: E501
        :type: float
        """

        self._max_heartrate = max_heartrate

    @property
    def segment(self):
        """Gets the segment of this DetailedSegmentEffort.  # noqa: E501


        :return: The segment of this DetailedSegmentEffort.  # noqa: E501
        :rtype: SummarySegment
        """
        return self._segment

    @segment.setter
    def segment(self, segment):
        """Sets the segment of this DetailedSegmentEffort.


        :param segment: The segment of this DetailedSegmentEffort.  # noqa: E501
        :type: SummarySegment
        """

        self._segment = segment

    @property
    def kom_rank(self):
        """Gets the kom_rank of this DetailedSegmentEffort.  # noqa: E501

        The rank of the effort on the global leaderboard if it belongs in the top 10 at the time of upload  # noqa: E501

        :return: The kom_rank of this DetailedSegmentEffort.  # noqa: E501
        :rtype: int
        """
        return self._kom_rank

    @kom_rank.setter
    def kom_rank(self, kom_rank):
        """Sets the kom_rank of this DetailedSegmentEffort.

        The rank of the effort on the global leaderboard if it belongs in the top 10 at the time of upload  # noqa: E501

        :param kom_rank: The kom_rank of this DetailedSegmentEffort.  # noqa: E501
        :type: int
        """

        self._kom_rank = kom_rank

    @property
    def pr_rank(self):
        """Gets the pr_rank of this DetailedSegmentEffort.  # noqa: E501

        The rank of the effort on the athlete's leaderboard if it belongs in the top 3 at the time of upload  # noqa: E501

        :return: The pr_rank of this DetailedSegmentEffort.  # noqa: E501
        :rtype: int
        """
        return self._pr_rank

    @pr_rank.setter
    def pr_rank(self, pr_rank):
        """Sets the pr_rank of this DetailedSegmentEffort.

        The rank of the effort on the athlete's leaderboard if it belongs in the top 3 at the time of upload  # noqa: E501

        :param pr_rank: The pr_rank of this DetailedSegmentEffort.  # noqa: E501
        :type: int
        """

        self._pr_rank = pr_rank

    @property
    def hidden(self):
        """Gets the hidden of this DetailedSegmentEffort.  # noqa: E501

        Whether this effort should be hidden when viewed within an activity  # noqa: E501

        :return: The hidden of this DetailedSegmentEffort.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this DetailedSegmentEffort.

        Whether this effort should be hidden when viewed within an activity  # noqa: E501

        :param hidden: The hidden of this DetailedSegmentEffort.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

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
        if issubclass(DetailedSegmentEffort, dict):
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
        if not isinstance(other, DetailedSegmentEffort):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
