# coding: utf-8

"""
    Lists

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

from hubspot.crm.lists.configuration import Configuration


class PublicIntegrationEventFilter(object):
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
    openapi_types = {"event_type_id": "int", "filter_lines": "list[PublicEventFilterMetadata]", "filter_type": "str"}

    attribute_map = {"event_type_id": "eventTypeId", "filter_lines": "filterLines", "filter_type": "filterType"}

    def __init__(self, event_type_id=None, filter_lines=None, filter_type="INTEGRATION_EVENT", local_vars_configuration=None):  # noqa: E501
        """PublicIntegrationEventFilter - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._event_type_id = None
        self._filter_lines = None
        self._filter_type = None
        self.discriminator = None

        self.event_type_id = event_type_id
        self.filter_lines = filter_lines
        self.filter_type = filter_type

    @property
    def event_type_id(self):
        """Gets the event_type_id of this PublicIntegrationEventFilter.  # noqa: E501


        :return: The event_type_id of this PublicIntegrationEventFilter.  # noqa: E501
        :rtype: int
        """
        return self._event_type_id

    @event_type_id.setter
    def event_type_id(self, event_type_id):
        """Sets the event_type_id of this PublicIntegrationEventFilter.


        :param event_type_id: The event_type_id of this PublicIntegrationEventFilter.  # noqa: E501
        :type event_type_id: int
        """
        if self.local_vars_configuration.client_side_validation and event_type_id is None:  # noqa: E501
            raise ValueError("Invalid value for `event_type_id`, must not be `None`")  # noqa: E501

        self._event_type_id = event_type_id

    @property
    def filter_lines(self):
        """Gets the filter_lines of this PublicIntegrationEventFilter.  # noqa: E501


        :return: The filter_lines of this PublicIntegrationEventFilter.  # noqa: E501
        :rtype: list[PublicEventFilterMetadata]
        """
        return self._filter_lines

    @filter_lines.setter
    def filter_lines(self, filter_lines):
        """Sets the filter_lines of this PublicIntegrationEventFilter.


        :param filter_lines: The filter_lines of this PublicIntegrationEventFilter.  # noqa: E501
        :type filter_lines: list[PublicEventFilterMetadata]
        """
        if self.local_vars_configuration.client_side_validation and filter_lines is None:  # noqa: E501
            raise ValueError("Invalid value for `filter_lines`, must not be `None`")  # noqa: E501

        self._filter_lines = filter_lines

    @property
    def filter_type(self):
        """Gets the filter_type of this PublicIntegrationEventFilter.  # noqa: E501


        :return: The filter_type of this PublicIntegrationEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._filter_type

    @filter_type.setter
    def filter_type(self, filter_type):
        """Sets the filter_type of this PublicIntegrationEventFilter.


        :param filter_type: The filter_type of this PublicIntegrationEventFilter.  # noqa: E501
        :type filter_type: str
        """
        if self.local_vars_configuration.client_side_validation and filter_type is None:  # noqa: E501
            raise ValueError("Invalid value for `filter_type`, must not be `None`")  # noqa: E501
        allowed_values = ["INTEGRATION_EVENT"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and filter_type not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `filter_type` ({0}), must be one of {1}".format(filter_type, allowed_values))  # noqa: E501

        self._filter_type = filter_type

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
        if not isinstance(other, PublicIntegrationEventFilter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublicIntegrationEventFilter):
            return True

        return self.to_dict() != other.to_dict()
