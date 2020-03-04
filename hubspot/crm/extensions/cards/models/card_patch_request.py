# coding: utf-8

"""
    CRM cards

    Allows an app to extend the CRM UI by surfacing custom cards in the sidebar of record pages. These cards are defined up-front as part of app configuration, then populated by external data fetch requests when the record page is accessed by a user.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.extensions.cards.configuration import Configuration


class CardPatchRequest(object):
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
    openapi_types = {
        'title': 'str',
        'fetch': 'CardFetchBodyPatch',
        'display': 'CardDisplayBody',
        'actions': 'CardActions'
    }

    attribute_map = {
        'title': 'title',
        'fetch': 'fetch',
        'display': 'display',
        'actions': 'actions'
    }

    def __init__(self, title=None, fetch=None, display=None, actions=None, local_vars_configuration=None):  # noqa: E501
        """CardPatchRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._title = None
        self._fetch = None
        self._display = None
        self._actions = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if fetch is not None:
            self.fetch = fetch
        if display is not None:
            self.display = display
        if actions is not None:
            self.actions = actions

    @property
    def title(self):
        """Gets the title of this CardPatchRequest.  # noqa: E501

        The top-level title for this card. Displayed to users in the CRM UI.  # noqa: E501

        :return: The title of this CardPatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CardPatchRequest.

        The top-level title for this card. Displayed to users in the CRM UI.  # noqa: E501

        :param title: The title of this CardPatchRequest.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def fetch(self):
        """Gets the fetch of this CardPatchRequest.  # noqa: E501


        :return: The fetch of this CardPatchRequest.  # noqa: E501
        :rtype: CardFetchBodyPatch
        """
        return self._fetch

    @fetch.setter
    def fetch(self, fetch):
        """Sets the fetch of this CardPatchRequest.


        :param fetch: The fetch of this CardPatchRequest.  # noqa: E501
        :type: CardFetchBodyPatch
        """

        self._fetch = fetch

    @property
    def display(self):
        """Gets the display of this CardPatchRequest.  # noqa: E501


        :return: The display of this CardPatchRequest.  # noqa: E501
        :rtype: CardDisplayBody
        """
        return self._display

    @display.setter
    def display(self, display):
        """Sets the display of this CardPatchRequest.


        :param display: The display of this CardPatchRequest.  # noqa: E501
        :type: CardDisplayBody
        """

        self._display = display

    @property
    def actions(self):
        """Gets the actions of this CardPatchRequest.  # noqa: E501


        :return: The actions of this CardPatchRequest.  # noqa: E501
        :rtype: CardActions
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this CardPatchRequest.


        :param actions: The actions of this CardPatchRequest.  # noqa: E501
        :type: CardActions
        """

        self._actions = actions

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CardPatchRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CardPatchRequest):
            return True

        return self.to_dict() != other.to_dict()
