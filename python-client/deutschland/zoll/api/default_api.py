"""
    Einfuhrzoll API

    Abfragen von Importzöllen und Wechselkursen  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from deutschland.zoll.api_client import ApiClient
from deutschland.zoll.api_client import Endpoint as _Endpoint
from deutschland.zoll.model.categories import Categories
from deutschland.zoll.model.countries import Countries
from deutschland.zoll.model.exchange_rates import ExchangeRates
from deutschland.zoll.model.product_groups import ProductGroups
from deutschland.zoll.model.product_units import ProductUnits
from deutschland.zoll.model.products import Products
from deutschland.zoll.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types,
)


class DefaultApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.kategorien_get_endpoint = _Endpoint(
            settings={
                "response_type": (Categories,),
                "auth": [],
                "endpoint_path": "/kategorien",
                "operation_id": "kategorien_get",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "client",
                    "view",
                    "user_agent",
                    "last_modified_date",
                ],
                "required": [
                    "client",
                    "view",
                    "user_agent",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "client": (str,),
                    "view": (str,),
                    "user_agent": (str,),
                    "last_modified_date": (str,),
                },
                "attribute_map": {
                    "client": "client",
                    "view": "view",
                    "user_agent": "User-Agent",
                    "last_modified_date": "lastModifiedDate",
                },
                "location_map": {
                    "client": "query",
                    "view": "query",
                    "user_agent": "header",
                    "last_modified_date": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.kurse_app_kurs_export_txt_get_endpoint = _Endpoint(
            settings={
                "response_type": (ExchangeRates,),
                "auth": [],
                "endpoint_path": "/Kurse/App/KursExport.txt",
                "operation_id": "kurse_app_kurs_export_txt_get",
                "http_method": "GET",
                "servers": [
                    {
                        "url": "https://zoll.de/SiteGlobals/Functions/",
                        "description": "No description provided",
                    },
                ],
            },
            params_map={
                "all": [
                    "view",
                    "user_agent",
                ],
                "required": [
                    "view",
                    "user_agent",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "view": (str,),
                    "user_agent": (str,),
                },
                "attribute_map": {
                    "view": "view",
                    "user_agent": "User-Agent",
                },
                "location_map": {
                    "view": "query",
                    "user_agent": "header",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.laender_get_endpoint = _Endpoint(
            settings={
                "response_type": (Countries,),
                "auth": [],
                "endpoint_path": "/laender",
                "operation_id": "laender_get",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "client",
                    "view",
                    "user_agent",
                    "last_modified_date",
                ],
                "required": [
                    "client",
                    "view",
                    "user_agent",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "client": (str,),
                    "view": (str,),
                    "user_agent": (str,),
                    "last_modified_date": (str,),
                },
                "attribute_map": {
                    "client": "client",
                    "view": "view",
                    "user_agent": "User-Agent",
                    "last_modified_date": "lastModifiedDate",
                },
                "location_map": {
                    "client": "query",
                    "view": "query",
                    "user_agent": "header",
                    "last_modified_date": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.produkte_get_endpoint = _Endpoint(
            settings={
                "response_type": (Products,),
                "auth": [],
                "endpoint_path": "/produkte",
                "operation_id": "produkte_get",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "client",
                    "view",
                    "user_agent",
                    "last_modified_date",
                ],
                "required": [
                    "client",
                    "view",
                    "user_agent",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "client": (str,),
                    "view": (str,),
                    "user_agent": (str,),
                    "last_modified_date": (str,),
                },
                "attribute_map": {
                    "client": "client",
                    "view": "view",
                    "user_agent": "User-Agent",
                    "last_modified_date": "lastModifiedDate",
                },
                "location_map": {
                    "client": "query",
                    "view": "query",
                    "user_agent": "header",
                    "last_modified_date": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.produkteinheiten_get_endpoint = _Endpoint(
            settings={
                "response_type": (ProductUnits,),
                "auth": [],
                "endpoint_path": "/produkteinheiten",
                "operation_id": "produkteinheiten_get",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "client",
                    "view",
                    "user_agent",
                    "last_modified_date",
                ],
                "required": [
                    "client",
                    "view",
                    "user_agent",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "client": (str,),
                    "view": (str,),
                    "user_agent": (str,),
                    "last_modified_date": (str,),
                },
                "attribute_map": {
                    "client": "client",
                    "view": "view",
                    "user_agent": "User-Agent",
                    "last_modified_date": "lastModifiedDate",
                },
                "location_map": {
                    "client": "query",
                    "view": "query",
                    "user_agent": "header",
                    "last_modified_date": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.produktgruppen_get_endpoint = _Endpoint(
            settings={
                "response_type": (ProductGroups,),
                "auth": [],
                "endpoint_path": "/produktgruppen",
                "operation_id": "produktgruppen_get",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "client",
                    "view",
                    "user_agent",
                    "last_modified_date",
                ],
                "required": [
                    "client",
                    "view",
                    "user_agent",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "client": (str,),
                    "view": (str,),
                    "user_agent": (str,),
                    "last_modified_date": (str,),
                },
                "attribute_map": {
                    "client": "client",
                    "view": "view",
                    "user_agent": "User-Agent",
                    "last_modified_date": "lastModifiedDate",
                },
                "location_map": {
                    "client": "query",
                    "view": "query",
                    "user_agent": "header",
                    "last_modified_date": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

    def kategorien_get(
        self,
        client="ZUP",
        view="renderJson[App]",
        user_agent="zollundpost/2 CFNetwork/1220.1 Darwin/20.3.0",
        **kwargs
    ):
        """Produktkategorien  # noqa: E501

        Produktkategoriendatenbank  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.kategorien_get(client="ZUP", view="renderJson[App]", user_agent="zollundpost/2 CFNetwork/1220.1 Darwin/20.3.0", async_req=True)
        >>> result = thread.get()

        Args:
            client (str): defaults to "ZUP", must be one of ["ZUP"]
            view (str): defaults to "renderJson[App]", must be one of ["renderJson[App]"]
            user_agent (str): defaults to "zollundpost/2 CFNetwork/1220.1 Darwin/20.3.0", must be one of ["zollundpost/2 CFNetwork/1220.1 Darwin/20.3.0"]

        Keyword Args:
            last_modified_date (str): [optional] if omitted the server will use the default value of ""
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            Categories
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs["client"] = client
        kwargs["view"] = view
        kwargs["user_agent"] = user_agent
        return self.kategorien_get_endpoint.call_with_http_info(**kwargs)

    def kurse_app_kurs_export_txt_get(
        self,
        view="jsonexportkurseZOLLWeb",
        user_agent="zollundpost/2 CFNetwork/1220.1 Darwin/20.3.0",
        **kwargs
    ):
        """Währungskurse  # noqa: E501

        Liste aller Länder mit Risikoeinstufung  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.kurse_app_kurs_export_txt_get(view="jsonexportkurseZOLLWeb", user_agent="zollundpost/2 CFNetwork/1220.1 Darwin/20.3.0", async_req=True)
        >>> result = thread.get()

        Args:
            view (str): defaults to "jsonexportkurseZOLLWeb", must be one of ["jsonexportkurseZOLLWeb"]
            user_agent (str): defaults to "zollundpost/2 CFNetwork/1220.1 Darwin/20.3.0", must be one of ["zollundpost/2 CFNetwork/1220.1 Darwin/20.3.0"]

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            ExchangeRates
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs["view"] = view
        kwargs["user_agent"] = user_agent
        return self.kurse_app_kurs_export_txt_get_endpoint.call_with_http_info(**kwargs)

    def laender_get(
        self,
        client="ZUP",
        view="renderJson[App]",
        user_agent="zollundpost/2 CFNetwork/1220.1 Darwin/20.3.0",
        **kwargs
    ):
        """laender_get  # noqa: E501

        Länder  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.laender_get(client="ZUP", view="renderJson[App]", user_agent="zollundpost/2 CFNetwork/1220.1 Darwin/20.3.0", async_req=True)
        >>> result = thread.get()

        Args:
            client (str): defaults to "ZUP", must be one of ["ZUP"]
            view (str): defaults to "renderJson[App]", must be one of ["renderJson[App]"]
            user_agent (str): defaults to "zollundpost/2 CFNetwork/1220.1 Darwin/20.3.0", must be one of ["zollundpost/2 CFNetwork/1220.1 Darwin/20.3.0"]

        Keyword Args:
            last_modified_date (str): [optional] if omitted the server will use the default value of ""
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            Countries
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs["client"] = client
        kwargs["view"] = view
        kwargs["user_agent"] = user_agent
        return self.laender_get_endpoint.call_with_http_info(**kwargs)

    def produkte_get(
        self,
        client="ZUP",
        view="renderJson[App]",
        user_agent="zollundpost/2 CFNetwork/1220.1 Darwin/20.3.0",
        **kwargs
    ):
        """Produkte  # noqa: E501

        Produktdatenbank mit Zolltarifen  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.produkte_get(client="ZUP", view="renderJson[App]", user_agent="zollundpost/2 CFNetwork/1220.1 Darwin/20.3.0", async_req=True)
        >>> result = thread.get()

        Args:
            client (str): defaults to "ZUP", must be one of ["ZUP"]
            view (str): defaults to "renderJson[App]", must be one of ["renderJson[App]"]
            user_agent (str): defaults to "zollundpost/2 CFNetwork/1220.1 Darwin/20.3.0", must be one of ["zollundpost/2 CFNetwork/1220.1 Darwin/20.3.0"]

        Keyword Args:
            last_modified_date (str): [optional] if omitted the server will use the default value of ""
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            Products
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs["client"] = client
        kwargs["view"] = view
        kwargs["user_agent"] = user_agent
        return self.produkte_get_endpoint.call_with_http_info(**kwargs)

    def produkteinheiten_get(
        self,
        client="ZUP",
        view="renderJson[App]",
        user_agent="zollundpost/2 CFNetwork/1220.1 Darwin/20.3.0",
        **kwargs
    ):
        """produkteinheiten_get  # noqa: E501

        Produkteinheiten  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.produkteinheiten_get(client="ZUP", view="renderJson[App]", user_agent="zollundpost/2 CFNetwork/1220.1 Darwin/20.3.0", async_req=True)
        >>> result = thread.get()

        Args:
            client (str): defaults to "ZUP", must be one of ["ZUP"]
            view (str): defaults to "renderJson[App]", must be one of ["renderJson[App]"]
            user_agent (str): defaults to "zollundpost/2 CFNetwork/1220.1 Darwin/20.3.0", must be one of ["zollundpost/2 CFNetwork/1220.1 Darwin/20.3.0"]

        Keyword Args:
            last_modified_date (str): [optional] if omitted the server will use the default value of ""
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            ProductUnits
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs["client"] = client
        kwargs["view"] = view
        kwargs["user_agent"] = user_agent
        return self.produkteinheiten_get_endpoint.call_with_http_info(**kwargs)

    def produktgruppen_get(
        self,
        client="ZUP",
        view="renderJson[App]",
        user_agent="zollundpost/2 CFNetwork/1220.1 Darwin/20.3.0",
        **kwargs
    ):
        """produktgruppen_get  # noqa: E501

        Produktgruppen  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.produktgruppen_get(client="ZUP", view="renderJson[App]", user_agent="zollundpost/2 CFNetwork/1220.1 Darwin/20.3.0", async_req=True)
        >>> result = thread.get()

        Args:
            client (str): defaults to "ZUP", must be one of ["ZUP"]
            view (str): defaults to "renderJson[App]", must be one of ["renderJson[App]"]
            user_agent (str): defaults to "zollundpost/2 CFNetwork/1220.1 Darwin/20.3.0", must be one of ["zollundpost/2 CFNetwork/1220.1 Darwin/20.3.0"]

        Keyword Args:
            last_modified_date (str): [optional] if omitted the server will use the default value of ""
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            ProductGroups
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs["client"] = client
        kwargs["view"] = view
        kwargs["user_agent"] = user_agent
        return self.produktgruppen_get_endpoint.call_with_http_info(**kwargs)
