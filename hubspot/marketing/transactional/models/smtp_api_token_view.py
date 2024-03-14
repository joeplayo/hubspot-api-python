# coding: utf-8

"""
    Transactional Single Send

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

from hubspot.marketing.transactional.configuration import Configuration


class SmtpApiTokenView(object):
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
    openapi_types = {"created_at": "datetime", "password": "str", "created_by": "str", "create_contact": "bool", "id": "str", "email_campaign_id": "str", "campaign_name": "str"}

    attribute_map = {
        "created_at": "createdAt",
        "password": "password",
        "created_by": "createdBy",
        "create_contact": "createContact",
        "id": "id",
        "email_campaign_id": "emailCampaignId",
        "campaign_name": "campaignName",
    }

    def __init__(self, created_at=None, password=None, created_by=None, create_contact=None, id=None, email_campaign_id=None, campaign_name=None, local_vars_configuration=None):  # noqa: E501
        """SmtpApiTokenView - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._created_at = None
        self._password = None
        self._created_by = None
        self._create_contact = None
        self._id = None
        self._email_campaign_id = None
        self._campaign_name = None
        self.discriminator = None

        self.created_at = created_at
        if password is not None:
            self.password = password
        self.created_by = created_by
        self.create_contact = create_contact
        self.id = id
        self.email_campaign_id = email_campaign_id
        self.campaign_name = campaign_name

    @property
    def created_at(self):
        """Gets the created_at of this SmtpApiTokenView.  # noqa: E501

        Timestamp generated when a token is created.  # noqa: E501

        :return: The created_at of this SmtpApiTokenView.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SmtpApiTokenView.

        Timestamp generated when a token is created.  # noqa: E501

        :param created_at: The created_at of this SmtpApiTokenView.  # noqa: E501
        :type created_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def password(self):
        """Gets the password of this SmtpApiTokenView.  # noqa: E501

        Password used to log into the HubSpot SMTP server.  # noqa: E501

        :return: The password of this SmtpApiTokenView.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this SmtpApiTokenView.

        Password used to log into the HubSpot SMTP server.  # noqa: E501

        :param password: The password of this SmtpApiTokenView.  # noqa: E501
        :type password: str
        """

        self._password = password

    @property
    def created_by(self):
        """Gets the created_by of this SmtpApiTokenView.  # noqa: E501

        Email address of the user that sent the token creation request.  # noqa: E501

        :return: The created_by of this SmtpApiTokenView.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this SmtpApiTokenView.

        Email address of the user that sent the token creation request.  # noqa: E501

        :param created_by: The created_by of this SmtpApiTokenView.  # noqa: E501
        :type created_by: str
        """
        if self.local_vars_configuration.client_side_validation and created_by is None:  # noqa: E501
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501

        self._created_by = created_by

    @property
    def create_contact(self):
        """Gets the create_contact of this SmtpApiTokenView.  # noqa: E501

        Indicates whether a contact should be created for email recipients.  # noqa: E501

        :return: The create_contact of this SmtpApiTokenView.  # noqa: E501
        :rtype: bool
        """
        return self._create_contact

    @create_contact.setter
    def create_contact(self, create_contact):
        """Sets the create_contact of this SmtpApiTokenView.

        Indicates whether a contact should be created for email recipients.  # noqa: E501

        :param create_contact: The create_contact of this SmtpApiTokenView.  # noqa: E501
        :type create_contact: bool
        """
        if self.local_vars_configuration.client_side_validation and create_contact is None:  # noqa: E501
            raise ValueError("Invalid value for `create_contact`, must not be `None`")  # noqa: E501

        self._create_contact = create_contact

    @property
    def id(self):
        """Gets the id of this SmtpApiTokenView.  # noqa: E501

        User name to log into the HubSpot SMTP server.  # noqa: E501

        :return: The id of this SmtpApiTokenView.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SmtpApiTokenView.

        User name to log into the HubSpot SMTP server.  # noqa: E501

        :param id: The id of this SmtpApiTokenView.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def email_campaign_id(self):
        """Gets the email_campaign_id of this SmtpApiTokenView.  # noqa: E501

        Identifier assigned to the campaign provided in the token creation request.  # noqa: E501

        :return: The email_campaign_id of this SmtpApiTokenView.  # noqa: E501
        :rtype: str
        """
        return self._email_campaign_id

    @email_campaign_id.setter
    def email_campaign_id(self, email_campaign_id):
        """Sets the email_campaign_id of this SmtpApiTokenView.

        Identifier assigned to the campaign provided in the token creation request.  # noqa: E501

        :param email_campaign_id: The email_campaign_id of this SmtpApiTokenView.  # noqa: E501
        :type email_campaign_id: str
        """
        if self.local_vars_configuration.client_side_validation and email_campaign_id is None:  # noqa: E501
            raise ValueError("Invalid value for `email_campaign_id`, must not be `None`")  # noqa: E501

        self._email_campaign_id = email_campaign_id

    @property
    def campaign_name(self):
        """Gets the campaign_name of this SmtpApiTokenView.  # noqa: E501

        A name for the campaign tied to the token.  # noqa: E501

        :return: The campaign_name of this SmtpApiTokenView.  # noqa: E501
        :rtype: str
        """
        return self._campaign_name

    @campaign_name.setter
    def campaign_name(self, campaign_name):
        """Sets the campaign_name of this SmtpApiTokenView.

        A name for the campaign tied to the token.  # noqa: E501

        :param campaign_name: The campaign_name of this SmtpApiTokenView.  # noqa: E501
        :type campaign_name: str
        """
        if self.local_vars_configuration.client_side_validation and campaign_name is None:  # noqa: E501
            raise ValueError("Invalid value for `campaign_name`, must not be `None`")  # noqa: E501

        self._campaign_name = campaign_name

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
        if not isinstance(other, SmtpApiTokenView):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SmtpApiTokenView):
            return True

        return self.to_dict() != other.to_dict()
