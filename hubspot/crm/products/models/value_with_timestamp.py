# coding: utf-8

"""
    Products

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from hubspot.crm.products.configuration import Configuration


class ValueWithTimestamp(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {"source_id": "str", "source_type": "str", "source_label": "str", "updated_by_user_id": "int", "value": "str", "timestamp": "datetime"}

    attribute_map = {"source_id": "sourceId", "source_type": "sourceType", "source_label": "sourceLabel", "updated_by_user_id": "updatedByUserId", "value": "value", "timestamp": "timestamp"}

    def __init__(self, source_id=None, source_type=None, source_label=None, updated_by_user_id=None, value=None, timestamp=None, local_vars_configuration=None):  # noqa: E501
        """ValueWithTimestamp - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._source_id = None
        self._source_type = None
        self._source_label = None
        self._updated_by_user_id = None
        self._value = None
        self._timestamp = None
        self.discriminator = None

        if source_id is not None:
            self.source_id = source_id
        self.source_type = source_type
        if source_label is not None:
            self.source_label = source_label
        if updated_by_user_id is not None:
            self.updated_by_user_id = updated_by_user_id
        self.value = value
        self.timestamp = timestamp

    @property
    def source_id(self):
        """Gets the source_id of this ValueWithTimestamp.  # noqa: E501


        :return: The source_id of this ValueWithTimestamp.  # noqa: E501
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this ValueWithTimestamp.


        :param source_id: The source_id of this ValueWithTimestamp.  # noqa: E501
        :type source_id: str
        """

        self._source_id = source_id

    @property
    def source_type(self):
        """Gets the source_type of this ValueWithTimestamp.  # noqa: E501


        :return: The source_type of this ValueWithTimestamp.  # noqa: E501
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this ValueWithTimestamp.


        :param source_type: The source_type of this ValueWithTimestamp.  # noqa: E501
        :type source_type: str
        """
        if self.local_vars_configuration.client_side_validation and source_type is None:  # noqa: E501
            raise ValueError("Invalid value for `source_type`, must not be `None`")  # noqa: E501

        self._source_type = source_type

    @property
    def source_label(self):
        """Gets the source_label of this ValueWithTimestamp.  # noqa: E501


        :return: The source_label of this ValueWithTimestamp.  # noqa: E501
        :rtype: str
        """
        return self._source_label

    @source_label.setter
    def source_label(self, source_label):
        """Sets the source_label of this ValueWithTimestamp.


        :param source_label: The source_label of this ValueWithTimestamp.  # noqa: E501
        :type source_label: str
        """

        self._source_label = source_label

    @property
    def updated_by_user_id(self):
        """Gets the updated_by_user_id of this ValueWithTimestamp.  # noqa: E501


        :return: The updated_by_user_id of this ValueWithTimestamp.  # noqa: E501
        :rtype: int
        """
        return self._updated_by_user_id

    @updated_by_user_id.setter
    def updated_by_user_id(self, updated_by_user_id):
        """Sets the updated_by_user_id of this ValueWithTimestamp.


        :param updated_by_user_id: The updated_by_user_id of this ValueWithTimestamp.  # noqa: E501
        :type updated_by_user_id: int
        """

        self._updated_by_user_id = updated_by_user_id

    @property
    def value(self):
        """Gets the value of this ValueWithTimestamp.  # noqa: E501


        :return: The value of this ValueWithTimestamp.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ValueWithTimestamp.


        :param value: The value of this ValueWithTimestamp.  # noqa: E501
        :type value: str
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def timestamp(self):
        """Gets the timestamp of this ValueWithTimestamp.  # noqa: E501


        :return: The timestamp of this ValueWithTimestamp.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ValueWithTimestamp.


        :param timestamp: The timestamp of this ValueWithTimestamp.  # noqa: E501
        :type timestamp: datetime
        """
        if self.local_vars_configuration.client_side_validation and timestamp is None:  # noqa: E501
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(lambda x: convert(x), value))
            elif isinstance(value, dict):
                result[attr] = dict(map(lambda item: (item[0], convert(item[1])), value.items()))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ValueWithTimestamp):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ValueWithTimestamp):
            return True

        return self.to_dict() != other.to_dict()
