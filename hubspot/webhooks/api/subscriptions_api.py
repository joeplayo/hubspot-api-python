# coding: utf-8

"""
    Webhooks API

    Provides a way for apps to subscribe to certain change events in HubSpot. Once configured, apps will receive event payloads containing details about the changes at a specified target URL. There can only be one target URL for receiving event notifications per app.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hubspot.webhooks.api_client import ApiClient
from hubspot.webhooks.exceptions import ApiTypeError, ApiValueError


class SubscriptionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def archive(self, subscription_id, app_id, **kwargs):  # noqa: E501
        """Delete a subscription  # noqa: E501

        Permanently deletes a subscription. This cannot be undone.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.archive(subscription_id, app_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int subscription_id: The ID of subscription to delete. (required)
        :param int app_id: The ID of the target app. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.archive_with_http_info(
            subscription_id, app_id, **kwargs
        )  # noqa: E501

    def archive_with_http_info(self, subscription_id, app_id, **kwargs):  # noqa: E501
        """Delete a subscription  # noqa: E501

        Permanently deletes a subscription. This cannot be undone.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.archive_with_http_info(subscription_id, app_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int subscription_id: The ID of subscription to delete. (required)
        :param int app_id: The ID of the target app. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["subscription_id", "app_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'" " to method archive" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'subscription_id' is set
        if self.api_client.client_side_validation and (
            "subscription_id" not in local_var_params
            or local_var_params["subscription_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `subscription_id` when calling `archive`"
            )  # noqa: E501
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and (
            "app_id" not in local_var_params
            or local_var_params["app_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `app_id` when calling `archive`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "subscription_id" in local_var_params:
            path_params["subscriptionId"] = local_var_params[
                "subscription_id"
            ]  # noqa: E501
        if "app_id" in local_var_params:
            path_params["appId"] = local_var_params["app_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["*/*"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["hapikey"]  # noqa: E501

        return self.api_client.call_api(
            "/webhooks/v3/{appId}/subscriptions/{subscriptionId}",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def create(self, app_id, subscription_create_request, **kwargs):  # noqa: E501
        """Subscribe to an event  # noqa: E501

        Creates a new webhook subscription for the given app. Each subscription in an app must be unique.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create(app_id, subscription_create_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int app_id: The ID of the target app. (required)
        :param SubscriptionCreateRequest subscription_create_request: Details about the new subscription. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: SubscriptionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.create_with_http_info(
            app_id, subscription_create_request, **kwargs
        )  # noqa: E501

    def create_with_http_info(
        self, app_id, subscription_create_request, **kwargs
    ):  # noqa: E501
        """Subscribe to an event  # noqa: E501

        Creates a new webhook subscription for the given app. Each subscription in an app must be unique.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_with_http_info(app_id, subscription_create_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int app_id: The ID of the target app. (required)
        :param SubscriptionCreateRequest subscription_create_request: Details about the new subscription. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(SubscriptionResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["app_id", "subscription_create_request"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'" " to method create" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and (
            "app_id" not in local_var_params
            or local_var_params["app_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `app_id` when calling `create`"
            )  # noqa: E501
        # verify the required parameter 'subscription_create_request' is set
        if self.api_client.client_side_validation and (
            "subscription_create_request" not in local_var_params
            or local_var_params["subscription_create_request"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `subscription_create_request` when calling `create`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "app_id" in local_var_params:
            path_params["appId"] = local_var_params["app_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "subscription_create_request" in local_var_params:
            body_params = local_var_params["subscription_create_request"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json", "*/*"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["hapikey"]  # noqa: E501

        return self.api_client.call_api(
            "/webhooks/v3/{appId}/subscriptions",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="SubscriptionResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_all(self, app_id, **kwargs):  # noqa: E501
        """Get subscription details  # noqa: E501

        Returns full details for all existing subscriptions for the given app.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all(app_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int app_id: The ID of the target app. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: SubscriptionListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.get_all_with_http_info(app_id, **kwargs)  # noqa: E501

    def get_all_with_http_info(self, app_id, **kwargs):  # noqa: E501
        """Get subscription details  # noqa: E501

        Returns full details for all existing subscriptions for the given app.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_with_http_info(app_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int app_id: The ID of the target app. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(SubscriptionListResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["app_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'" " to method get_all" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and (
            "app_id" not in local_var_params
            or local_var_params["app_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `app_id` when calling `get_all`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "app_id" in local_var_params:
            path_params["appId"] = local_var_params["app_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json", "*/*"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["hapikey"]  # noqa: E501

        return self.api_client.call_api(
            "/webhooks/v3/{appId}/subscriptions",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="SubscriptionListResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_by_id(self, app_id, subscription_id, **kwargs):  # noqa: E501
        """Get subscription  # noqa: E501

        Returns details about a subscription.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_by_id(app_id, subscription_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int app_id: The ID of the target app. (required)
        :param int subscription_id: The ID of the target subscription. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: SubscriptionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.get_by_id_with_http_info(
            app_id, subscription_id, **kwargs
        )  # noqa: E501

    def get_by_id_with_http_info(self, app_id, subscription_id, **kwargs):  # noqa: E501
        """Get subscription  # noqa: E501

        Returns details about a subscription.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_by_id_with_http_info(app_id, subscription_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int app_id: The ID of the target app. (required)
        :param int subscription_id: The ID of the target subscription. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(SubscriptionResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["app_id", "subscription_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_by_id" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and (
            "app_id" not in local_var_params
            or local_var_params["app_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `app_id` when calling `get_by_id`"
            )  # noqa: E501
        # verify the required parameter 'subscription_id' is set
        if self.api_client.client_side_validation and (
            "subscription_id" not in local_var_params
            or local_var_params["subscription_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `subscription_id` when calling `get_by_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "app_id" in local_var_params:
            path_params["appId"] = local_var_params["app_id"]  # noqa: E501
        if "subscription_id" in local_var_params:
            path_params["subscriptionId"] = local_var_params[
                "subscription_id"
            ]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json", "*/*"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["hapikey"]  # noqa: E501

        return self.api_client.call_api(
            "/webhooks/v3/{appId}/subscriptions/{subscriptionId}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="SubscriptionResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def update(
        self, subscription_id, app_id, subscription_patch_request, **kwargs
    ):  # noqa: E501
        """Update a subscription  # noqa: E501

        Updates the details for an existing subscription.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update(subscription_id, app_id, subscription_patch_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int subscription_id: The ID of the subscription to update. (required)
        :param int app_id: The ID of the target app. (required)
        :param SubscriptionPatchRequest subscription_patch_request: Updated details for the subscription. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: SubscriptionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.update_with_http_info(
            subscription_id, app_id, subscription_patch_request, **kwargs
        )  # noqa: E501

    def update_with_http_info(
        self, subscription_id, app_id, subscription_patch_request, **kwargs
    ):  # noqa: E501
        """Update a subscription  # noqa: E501

        Updates the details for an existing subscription.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_with_http_info(subscription_id, app_id, subscription_patch_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int subscription_id: The ID of the subscription to update. (required)
        :param int app_id: The ID of the target app. (required)
        :param SubscriptionPatchRequest subscription_patch_request: Updated details for the subscription. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(SubscriptionResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            "subscription_id",
            "app_id",
            "subscription_patch_request",
        ]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'" " to method update" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'subscription_id' is set
        if self.api_client.client_side_validation and (
            "subscription_id" not in local_var_params
            or local_var_params["subscription_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `subscription_id` when calling `update`"
            )  # noqa: E501
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and (
            "app_id" not in local_var_params
            or local_var_params["app_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `app_id` when calling `update`"
            )  # noqa: E501
        # verify the required parameter 'subscription_patch_request' is set
        if self.api_client.client_side_validation and (
            "subscription_patch_request" not in local_var_params
            or local_var_params["subscription_patch_request"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `subscription_patch_request` when calling `update`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "subscription_id" in local_var_params:
            path_params["subscriptionId"] = local_var_params[
                "subscription_id"
            ]  # noqa: E501
        if "app_id" in local_var_params:
            path_params["appId"] = local_var_params["app_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "subscription_patch_request" in local_var_params:
            body_params = local_var_params["subscription_patch_request"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json", "*/*"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["hapikey"]  # noqa: E501

        return self.api_client.call_api(
            "/webhooks/v3/{appId}/subscriptions/{subscriptionId}",
            "PATCH",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="SubscriptionResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def update_batch(
        self, app_id, batch_input_subscription_batch_update_request, **kwargs
    ):  # noqa: E501
        """Batch update subscriptions  # noqa: E501

        Activates or deactivates target app subscriptions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_batch(app_id, batch_input_subscription_batch_update_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int app_id: The app ID of the target app. (required)
        :param BatchInputSubscriptionBatchUpdateRequest batch_input_subscription_batch_update_request: Updated details for the specified subscriptions. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: BatchResponseSubscriptionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.update_batch_with_http_info(
            app_id, batch_input_subscription_batch_update_request, **kwargs
        )  # noqa: E501

    def update_batch_with_http_info(
        self, app_id, batch_input_subscription_batch_update_request, **kwargs
    ):  # noqa: E501
        """Batch update subscriptions  # noqa: E501

        Activates or deactivates target app subscriptions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_batch_with_http_info(app_id, batch_input_subscription_batch_update_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int app_id: The app ID of the target app. (required)
        :param BatchInputSubscriptionBatchUpdateRequest batch_input_subscription_batch_update_request: Updated details for the specified subscriptions. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(BatchResponseSubscriptionResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            "app_id",
            "batch_input_subscription_batch_update_request",
        ]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_batch" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and (
            "app_id" not in local_var_params
            or local_var_params["app_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `app_id` when calling `update_batch`"
            )  # noqa: E501
        # verify the required parameter 'batch_input_subscription_batch_update_request' is set
        if self.api_client.client_side_validation and (
            "batch_input_subscription_batch_update_request" not in local_var_params
            or local_var_params[  # noqa: E501
                "batch_input_subscription_batch_update_request"
            ]
            is None
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `batch_input_subscription_batch_update_request` when calling `update_batch`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "app_id" in local_var_params:
            path_params["appId"] = local_var_params["app_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "batch_input_subscription_batch_update_request" in local_var_params:
            body_params = local_var_params[
                "batch_input_subscription_batch_update_request"
            ]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json", "*/*"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["hapikey"]  # noqa: E501

        return self.api_client.call_api(
            "/webhooks/v3/{appId}/subscriptions/batch/update",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="BatchResponseSubscriptionResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
