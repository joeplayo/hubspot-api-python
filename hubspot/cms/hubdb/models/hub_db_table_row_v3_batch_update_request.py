# coding: utf-8

"""
    Hubdb

    HubDB is a relational data store that presents data as rows, columns, and cells in a table, much like a spreadsheet. HubDB tables can be added or modified [in the HubSpot CMS](https://knowledge.hubspot.com/cos-general/how-to-edit-hubdb-tables), but you can also use the API endpoints documented here. For more information on HubDB tables and using their data on a HubSpot site, see the [CMS developers site](https://designers.hubspot.com/docs/tools/hubdb). You can also see the [documentation for dynamic pages](https://designers.hubspot.com/docs/tutorials/how-to-build-dynamic-pages-with-hubdb) for more details about the `useForPages` field.  HubDB tables support `draft` and `published` versions. This allows you to update data in the table, either for testing or to allow for a manual approval process, without affecting any live pages using the existing data. Draft data can be reviewed, and published by a user working in HubSpot or published via the API. Draft data can also be discarded, allowing users to go back to the published version of the data without disrupting it. If a table is set to be `allowed for public access`, you can access the published version of the table and rows without any authentication by specifying the portal id via the query parameter `portalId`.  # noqa: E501

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

from hubspot.cms.hubdb.configuration import Configuration


class HubDbTableRowV3BatchUpdateRequest(object):
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
    openapi_types = {"path": "str", "child_table_id": "int", "values": "dict[str, object]", "name": "str", "id": "str", "display_index": "int"}

    attribute_map = {"path": "path", "child_table_id": "childTableId", "values": "values", "name": "name", "id": "id", "display_index": "displayIndex"}

    def __init__(self, path=None, child_table_id=None, values=None, name=None, id=None, display_index=None, local_vars_configuration=None):  # noqa: E501
        """HubDbTableRowV3BatchUpdateRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._path = None
        self._child_table_id = None
        self._values = None
        self._name = None
        self._id = None
        self._display_index = None
        self.discriminator = None

        if path is not None:
            self.path = path
        if child_table_id is not None:
            self.child_table_id = child_table_id
        self.values = values
        if name is not None:
            self.name = name
        self.id = id
        if display_index is not None:
            self.display_index = display_index

    @property
    def path(self):
        """Gets the path of this HubDbTableRowV3BatchUpdateRequest.  # noqa: E501

        Specifies the value for `hs_path` column, which will be used as slug in the dynamic pages  # noqa: E501

        :return: The path of this HubDbTableRowV3BatchUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this HubDbTableRowV3BatchUpdateRequest.

        Specifies the value for `hs_path` column, which will be used as slug in the dynamic pages  # noqa: E501

        :param path: The path of this HubDbTableRowV3BatchUpdateRequest.  # noqa: E501
        :type path: str
        """

        self._path = path

    @property
    def child_table_id(self):
        """Gets the child_table_id of this HubDbTableRowV3BatchUpdateRequest.  # noqa: E501

        Specifies the value for the column child table id  # noqa: E501

        :return: The child_table_id of this HubDbTableRowV3BatchUpdateRequest.  # noqa: E501
        :rtype: int
        """
        return self._child_table_id

    @child_table_id.setter
    def child_table_id(self, child_table_id):
        """Sets the child_table_id of this HubDbTableRowV3BatchUpdateRequest.

        Specifies the value for the column child table id  # noqa: E501

        :param child_table_id: The child_table_id of this HubDbTableRowV3BatchUpdateRequest.  # noqa: E501
        :type child_table_id: int
        """

        self._child_table_id = child_table_id

    @property
    def values(self):
        """Gets the values of this HubDbTableRowV3BatchUpdateRequest.  # noqa: E501

        List of key value pairs with the column name and column value  # noqa: E501

        :return: The values of this HubDbTableRowV3BatchUpdateRequest.  # noqa: E501
        :rtype: dict[str, object]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this HubDbTableRowV3BatchUpdateRequest.

        List of key value pairs with the column name and column value  # noqa: E501

        :param values: The values of this HubDbTableRowV3BatchUpdateRequest.  # noqa: E501
        :type values: dict[str, object]
        """
        if self.local_vars_configuration.client_side_validation and values is None:  # noqa: E501
            raise ValueError("Invalid value for `values`, must not be `None`")  # noqa: E501

        self._values = values

    @property
    def name(self):
        """Gets the name of this HubDbTableRowV3BatchUpdateRequest.  # noqa: E501

        Specifies the value for `hs_name` column, which will be used as title in the dynamic pages  # noqa: E501

        :return: The name of this HubDbTableRowV3BatchUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HubDbTableRowV3BatchUpdateRequest.

        Specifies the value for `hs_name` column, which will be used as title in the dynamic pages  # noqa: E501

        :param name: The name of this HubDbTableRowV3BatchUpdateRequest.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this HubDbTableRowV3BatchUpdateRequest.  # noqa: E501

        The id of the table row  # noqa: E501

        :return: The id of this HubDbTableRowV3BatchUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HubDbTableRowV3BatchUpdateRequest.

        The id of the table row  # noqa: E501

        :param id: The id of this HubDbTableRowV3BatchUpdateRequest.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def display_index(self):
        """Gets the display_index of this HubDbTableRowV3BatchUpdateRequest.  # noqa: E501


        :return: The display_index of this HubDbTableRowV3BatchUpdateRequest.  # noqa: E501
        :rtype: int
        """
        return self._display_index

    @display_index.setter
    def display_index(self, display_index):
        """Sets the display_index of this HubDbTableRowV3BatchUpdateRequest.


        :param display_index: The display_index of this HubDbTableRowV3BatchUpdateRequest.  # noqa: E501
        :type display_index: int
        """

        self._display_index = display_index

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
        if not isinstance(other, HubDbTableRowV3BatchUpdateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HubDbTableRowV3BatchUpdateRequest):
            return True

        return self.to_dict() != other.to_dict()
