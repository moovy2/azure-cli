# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
#
# Generation mode: Incremental
# --------------------------------------------------------------------------
# pylint: disable=wildcard-import
# pylint: disable=too-many-locals

from .generated.custom import *  # noqa: F403
try:
    from .manual.custom import *  # noqa: F403
except ImportError:
    pass


import uuid
import re
from azure.cli.command_modules.apim._params import ImportFormat
from azure.cli.core.util import sdk_no_wait
from azure.cli.core.azclierror import (RequiredArgumentMissingError, MutuallyExclusiveArgumentError,
                                       InvalidArgumentValueError)
from azure.mgmt.apimanagement.models import (ApiManagementServiceResource, ApiManagementServiceIdentity,
                                             ApiManagementServiceSkuProperties,
                                             ApiManagementServiceBackupRestoreParameters,
                                             ApiContract, ApiType, ApiCreateOrUpdateParameter, Protocol,
                                             VirtualNetworkType, SkuType, ApiCreateOrUpdatePropertiesWsdlSelector,
                                             SoapApiType, ContentFormat, SubscriptionKeyParameterNamesContract,
                                             OAuth2AuthenticationSettingsContract, AuthenticationSettingsContract,
                                             OpenIdAuthenticationSettingsContract, ProductContract, ProductState,
                                             NamedValueCreateContract, VersioningScheme, ApiVersionSetContract,
                                             OperationContract, ApiManagementServiceCheckNameAvailabilityParameters,
                                             ApiReleaseContract, SchemaContract)


# Helpers

API_VS_ARM_ID_Reg = "(.*?)/providers/microsoft.apimanagement/service/([^/]+)/apiVersionSets/([^/]+)"
API_VS_PREFIX = "/apiVersionSets/"


def _get_vs_fullpath(versionSetId):
    if versionSetId is not None:
        if re.match(API_VS_ARM_ID_Reg, versionSetId) is None:
            fullpath = API_VS_PREFIX + versionSetId
        else:
            fullpath = versionSetId
    else:
        fullpath = None
    return fullpath


def _get_subscription_key_parameter_names(subscription_key_query_param_name=None, subscription_key_header_name=None):
    names = None
    if subscription_key_query_param_name is not None and subscription_key_header_name is not None:
        names = SubscriptionKeyParameterNamesContract(
            header=subscription_key_header_name,
            query=subscription_key_query_param_name
        )
    elif subscription_key_query_param_name is not None or subscription_key_header_name is not None:
        raise RequiredArgumentMissingError(
            "Please specify 'subscription_key_query_param_name' and 'subscription_key_header_name' at the same time.")
    return names


# Service Operations

def apim_create(client, resource_group_name, name, publisher_email, sku_name=SkuType.developer.value,
                sku_capacity=1, virtual_network_type=VirtualNetworkType.none.value, enable_managed_identity=False,
                enable_client_certificate=None, publisher_name=None, location=None, tags=None, no_wait=False):

    parameters = ApiManagementServiceResource(
        location=location,
        notification_sender_email=publisher_email,
        publisher_email=publisher_email,
        publisher_name=publisher_name,
        sku=ApiManagementServiceSkuProperties(
            name=sku_name, capacity=sku_capacity),
        enable_client_certificate=enable_client_certificate,
        virtual_network_type=VirtualNetworkType(virtual_network_type),
        tags=tags
    )

    if enable_managed_identity:
        parameters.identity = ApiManagementServiceIdentity(type="SystemAssigned")

    if parameters.sku.name == SkuType.consumption.value:
        parameters.sku.capacity = 0

    return sdk_no_wait(no_wait, client.api_management_service.begin_create_or_update,
                       resource_group_name=resource_group_name,
                       service_name=name, parameters=parameters)


def apim_update(instance, publisher_email=None, sku_name=None, sku_capacity=None,
                virtual_network_type=None, publisher_name=None, enable_managed_identity=None,
                enable_client_certificate=None, tags=None):

    if publisher_email is not None:
        instance.publisher_email = publisher_email

    if sku_name is not None:
        instance.sku.name = sku_name

    if sku_capacity is not None:
        instance.sku.capacity = sku_capacity

    if virtual_network_type is not None:
        instance.virtual_network_type = virtual_network_type

    if publisher_email is not None:
        instance.publisher_email = publisher_email

    if publisher_name is not None:
        instance.publisher_name = publisher_name

    if not enable_managed_identity:
        instance.identity = None
    else:
        if instance.identity is None:
            instance.identity = ApiManagementServiceIdentity(
                type="SystemAssigned")

    if enable_client_certificate is not None:
        instance.enable_client_certificate = enable_client_certificate

    if tags is not None:
        instance.tags = tags

    return instance


def apim_list(client, resource_group_name=None):
    """List all APIM instances.  Resource group is optional """
    if resource_group_name:
        return client.api_management_service.list_by_resource_group(resource_group_name)
    return client.api_management_service.list()


def apim_get(client, resource_group_name, name):
    """Show details of an APIM instance """
    return client.api_management_service.get(resource_group_name, name)


def apim_check_name_availability(client, name):
    """checks to see if a service name is available to use """
    parameters = ApiManagementServiceCheckNameAvailabilityParameters(
        name=name)
    return client.api_management_service.check_name_availability(parameters)


def apim_backup(client, resource_group_name, name, backup_name, storage_account_name,
                storage_account_container, storage_account_key):
    """back up an API Management service to the configured storage account """
    parameters = ApiManagementServiceBackupRestoreParameters(
        storage_account=storage_account_name,
        access_key=storage_account_key,
        container_name=storage_account_container,
        backup_name=backup_name)

    return client.api_management_service.begin_backup(resource_group_name, name, parameters)


def apim_restore(client, resource_group_name, name, backup_name, storage_account_name,
                 storage_account_container, storage_account_key):
    """Restore an API Management service to the configured storage account """
    parameters = ApiManagementServiceBackupRestoreParameters(
        storage_account=storage_account_name,
        access_key=storage_account_key,
        container_name=storage_account_container,
        backup_name=backup_name)

    return client.api_management_service.begin_restore(resource_group_name, name, parameters)


def apim_apply_network_configuration_updates(client, resource_group_name, name, location=None):
    """Updates the Microsoft.ApiManagement resource running in the Virtual network to pick the updated DNS changes. """
    properties = {}
    if location is not None:
        properties['location'] = location

    return client.api_management_service.apply_network_configuration_updates(resource_group_name, name, properties)


# Schema operations


def apim_api_schema_create(client, resource_group_name, service_name, api_id, schema_id, schema_type,
                           schema_name=None, schema_path=None, schema_content=None,
                           resource_type=None, no_wait=False):
    """creates or updates an API Schema. """

    if schema_path is not None and schema_content is None:
        api_file = open(schema_path, 'r')
        content_value = api_file.read()
        value = content_value
    elif schema_content is not None and schema_path is None:
        value = schema_content
    elif schema_path is not None and schema_content is not None:
        raise MutuallyExclusiveArgumentError(
            "Can't specify schema_path and schema_content at the same time.")
    else:
        raise RequiredArgumentMissingError(
            "Please either specify schema_path or schema_content.")

    parameters = SchemaContract(
        id=schema_id,
        name=schema_name,
        type=resource_type,
        content_type=schema_type,
        value=value
    )

    return sdk_no_wait(no_wait, client.api_schema.begin_create_or_update,
                       resource_group_name=resource_group_name,
                       service_name=service_name, api_id=api_id, schema_id=schema_id, parameters=parameters)


def apim_api_schema_delete(client, resource_group_name, service_name, api_id, schema_id, if_match=None, no_wait=False):
    """Deletes an API Schema. """
    return sdk_no_wait(no_wait, client.api_schema.delete,
                       resource_group_name=resource_group_name,
                       service_name=service_name, api_id=api_id, schema_id=schema_id,
                       if_match="*" if if_match is None else if_match)


def apim_api_schema_get(client, resource_group_name, service_name, api_id, schema_id):
    """Shows details of an API Schema. """

    return client.api_schema.get(resource_group_name=resource_group_name,
                                 service_name=service_name,
                                 api_id=api_id,
                                 schema_id=schema_id)


def apim_api_schema_entity(client, resource_group_name, service_name, api_id, schema_id):
    """Shows details of an API Schema. """

    return client.api_schema.get_entity_tag(resource_group_name=resource_group_name,
                                            service_name=service_name,
                                            api_id=api_id,
                                            schema_id=schema_id)


def apim_api_schema_list(client, resource_group_name, api_id, service_name,
                         filter_display_name=None,
                         top=None, skip=None):
    """Get the schema configuration at the API level. """

    return client.api_schema.list_by_api(resource_group_name,
                                         service_name, api_id,
                                         filter=filter_display_name,
                                         skip=skip, top=top)


# API Operations
def apim_api_create(client, resource_group_name, service_name, api_id, description=None,
                    subscription_key_header_name=None, subscription_key_query_param_name=None,
                    open_id_provider_id=None, bearer_token_sending_methods=None,
                    authorization_server_id=None, authorization_scope=None, display_name=None,
                    service_url=None, protocols=None, path=None, subscription_key_required=None,
                    api_type=None, subscription_required=False, no_wait=False):
    """Creates a new API. """

    if authorization_server_id is not None and authorization_scope is not None:
        o_auth2 = OAuth2AuthenticationSettingsContract(
            authorization_server_id=authorization_server_id,
            scope=authorization_scope
        )
        authentication_settings = AuthenticationSettingsContract(
            o_auth2=o_auth2,
            subscription_key_required=subscription_key_required
        )
    elif open_id_provider_id is not None and bearer_token_sending_methods is not None:
        openid = OpenIdAuthenticationSettingsContract(
            openid_provider_id=open_id_provider_id,
            bearer_token_sending_methods=bearer_token_sending_methods
        )
        authentication_settings = AuthenticationSettingsContract(
            openid=openid,
            subscription_key_required=subscription_key_required
        )
    else:
        authentication_settings = None

    parameters = ApiContract(
        api_id=api_id,
        description=description,
        authentication_settings=authentication_settings,
        subscription_key_parameter_names=_get_subscription_key_parameter_names(
            subscription_key_query_param_name,
            subscription_key_header_name),
        display_name=display_name,
        service_url=service_url,
        protocols=protocols if protocols is not None else [
            Protocol.https.value],
        path=path,
        api_type=api_type if api_type is not None else ApiType.http.value,
        subscription_required=subscription_required
    )

    return sdk_no_wait(no_wait, client.api.begin_create_or_update,
                       resource_group_name=resource_group_name,
                       service_name=service_name, api_id=api_id, parameters=parameters)


def apim_api_get(client, resource_group_name, service_name, api_id):
    """Shows details of an API. """

    return client.api.get(resource_group_name=resource_group_name,
                          service_name=service_name,
                          api_id=api_id)


def apim_api_list(client, resource_group_name, service_name, filter_display_name=None, top=None, skip=None):
    """List all APIs of an API Management instance. """

    if filter_display_name is not None:
        filter_display_name = "properties/displayName eq '%s'" % filter_display_name

    return client.api.list_by_service(resource_group_name, service_name, filter=filter_display_name, skip=skip, top=top)


def apim_api_delete(
        client, resource_group_name, service_name, api_id, delete_revisions=None, if_match=None, no_wait=False):
    """Deletes an existing API. """

    cms = client.api

    return sdk_no_wait(
        no_wait,
        cms.delete,
        resource_group_name=resource_group_name,
        service_name=service_name,
        api_id=api_id,
        if_match="*" if if_match is None else if_match,
        delete_revisions=delete_revisions if delete_revisions is not None else False)


def apim_api_update(instance, description=None, subscription_key_header_name=None,
                    subscription_key_query_param_name=None, display_name=None, service_url=None, protocols=None,
                    path=None, api_type=None, subscription_required=None, tags=None):
    """Updates an existing API. """

    if description is not None:
        instance.description = description

    if subscription_key_header_name is not None:
        instance.subscription_key_parameter_names = _get_subscription_key_parameter_names(
            subscription_key_query_param_name, subscription_key_header_name)

    if display_name is not None:
        instance.display_name = display_name

    if service_url is not None:
        instance.service_url = service_url

    if protocols is not None:
        instance.protocols = protocols

    if path is not None:
        instance.path = path

    if api_type is not None:
        instance.api_type = api_type

    if subscription_required is not None:
        instance.subscription_required = subscription_required

    if tags is not None:
        instance.tags = tags

    return instance


def apim_api_import(
        client, resource_group_name, service_name, path, specification_format, description=None,
        subscription_key_header_name=None, subscription_key_query_param_name=None, api_id=None, api_revision=None,
        api_version=None, api_version_set_id=None, display_name=None, service_url=None, protocols=None,
        specification_path=None, specification_url=None, api_type=None, subscription_required=None, soap_api_type=None,
        wsdl_endpoint_name=None, wsdl_service_name=None, no_wait=False):
    """Import a new API"""
    cms = client.api

    # api_type: Type of API. Possible values include: 'http', 'soap'
    # possible parameter format is 'wadl-xml', 'wadl-link-json', 'swagger-json', 'swagger-link-json',
    #   'wsdl', 'wsdl-link', 'openapi', 'openapi+json', 'openapi-link'
    # possible parameter specificationFormat is 'Wadl', 'Swagger', 'OpenApi', 'OpenApiJson', 'Wsdl'

    parameters = ApiCreateOrUpdateParameter(
        path=path,
        protocols=protocols,
        service_url=service_url,
        display_name=display_name,
        description=description,
        subscription_required=subscription_required,
        subscription_key_parameter_names=_get_subscription_key_parameter_names(
            subscription_key_query_param_name,
            subscription_key_header_name),
        api_version=api_version,
        api_version_set_id=_get_vs_fullpath(api_version_set_id)
    )

    if api_revision is not None and api_id is not None:
        api_id = api_id + ";rev=" + api_revision
    elif api_id is None:
        api_id = uuid.uuid4().hex

    if specification_path is not None and specification_url is None:
        api_file = open(specification_path, 'r')
        content_value = api_file.read()
        parameters.value = content_value
    elif specification_url is not None and specification_path is None:
        parameters.value = specification_url
    elif specification_path is not None and specification_url is not None:
        raise MutuallyExclusiveArgumentError(
            "Can't specify specification-url and specification-path at the same time.")
    else:
        raise RequiredArgumentMissingError(
            "Please either specify specification-url or specification-path.")

    FORMAT_MAPPINGS = {
        ImportFormat.Wadl.value: {
            # specification_path is not none
            True: ContentFormat.WADL_XML.value,
            # specification_url is not none
            False: ContentFormat.WADL_LINK_JSON.value
        },
        ImportFormat.Swagger.value: {
            True: ContentFormat.SWAGGER_JSON.value,
            False: ContentFormat.SWAGGER_LINK_JSON.value
        },
        ImportFormat.OpenApi.value: {
            True: ContentFormat.OPENAPI.value,
            False: ContentFormat.OPENAPI_LINK.value
        },
        ImportFormat.OpenApiJson.value: {
            True: ContentFormat.OPENAPI_JSON.value,
            False: ContentFormat.OPENAPI_JSON_LINK.value
        },
        ImportFormat.Wsdl.value: {
            True: ContentFormat.WSDL.value,
            False: ContentFormat.WSDL_LINK.value
        }
    }

    if specification_format in FORMAT_MAPPINGS:
        parameters.format = FORMAT_MAPPINGS[specification_format][specification_path is not None]
    else:
        raise InvalidArgumentValueError(
            "SpecificationFormat: " + specification_format + "is not supported.")

    if specification_format == ImportFormat.Wsdl.value:
        if api_type == ApiType.http.value:
            soap_api_type = SoapApiType.soap_to_rest.value
        else:
            soap_api_type = SoapApiType.soap_pass_through.value

        parameters.soap_api_type = soap_api_type

        if wsdl_service_name is not None and wsdl_endpoint_name is not None:
            parameters.wsdl_selector = ApiCreateOrUpdatePropertiesWsdlSelector(
                wsdl_service_name=wsdl_service_name,
                wsdl_endpoint_name=wsdl_endpoint_name
            )

    return sdk_no_wait(
        no_wait,
        cms.begin_create_or_update,
        resource_group_name=resource_group_name,
        service_name=service_name,
        api_id=api_id,
        parameters=parameters)


# Product API Operations

def apim_product_api_list(client, resource_group_name, service_name, product_id):

    return client.product_api.list_by_product(resource_group_name, service_name, product_id)


def apim_product_api_check_association(client, resource_group_name, service_name, product_id, api_id):

    return client.product_api.check_entity_exists(resource_group_name, service_name, product_id, api_id)


def apim_product_api_add(client, resource_group_name, service_name, product_id, api_id, no_wait=False):

    return sdk_no_wait(
        no_wait,
        client.product_api.create_or_update,
        resource_group_name=resource_group_name,
        service_name=service_name,
        product_id=product_id,
        api_id=api_id)


def apim_product_api_delete(client, resource_group_name, service_name, product_id, api_id, no_wait=False):

    return sdk_no_wait(
        no_wait,
        client.product_api.delete,
        resource_group_name=resource_group_name,
        service_name=service_name,
        product_id=product_id,
        api_id=api_id)


# Product Operations

def apim_product_list(client, resource_group_name, service_name):

    return client.product.list_by_service(resource_group_name, service_name)


def apim_product_show(client, resource_group_name, service_name, product_id):

    return client.product.get(resource_group_name, service_name, product_id)


def apim_product_create(
        client, resource_group_name, service_name, product_name, product_id=None, description=None, legal_terms=None,
        subscription_required=None, approval_required=None, subscriptions_limit=None, state=None, no_wait=False):

    parameters = ProductContract(
        description=description,
        terms=legal_terms,
        subscription_required=subscription_required,
        display_name=product_name,
        approval_required=approval_required,
        subscriptions_limit=subscriptions_limit
    )

    # Possible values include: 'notPublished', 'published'
    if state is not None:
        if state == ProductState.not_published:
            parameters.state = ProductState.not_published
        elif state == ProductState.published:
            parameters.state = ProductState.published
        else:
            raise InvalidArgumentValueError(
                "State: " + state + " is not supported.")

    if product_id is None:
        product_id = uuid.uuid4().hex

    return sdk_no_wait(
        no_wait,
        client.product.create_or_update,
        resource_group_name=resource_group_name,
        service_name=service_name,
        product_id=product_id,
        parameters=parameters)


def apim_product_update(
        instance, product_name=None, description=None, legal_terms=None, subscription_required=None,
        approval_required=None, subscriptions_limit=None, state=None):

    if product_name is not None:
        instance.display_name = product_name

    if description is not None:
        instance.description = description

    if legal_terms is not None:
        instance.terms = legal_terms

    if subscription_required is not None:
        instance.subscription_required = subscription_required

    if approval_required is not None:
        instance.approval_required = approval_required

    if subscriptions_limit is not None:
        instance.subscriptions_limit = subscriptions_limit

    if state is not None:
        if state == ProductState.not_published:
            instance.state = ProductState.not_published
        elif state == ProductState.published:
            instance.state = ProductState.published
        else:
            raise InvalidArgumentValueError(
                "State: " + state + " is not supported.")

    return instance


def apim_product_delete(
        client, resource_group_name, service_name, product_id, delete_subscriptions=None, if_match=None, no_wait=False):

    return sdk_no_wait(
        no_wait,
        client.product.delete,
        resource_group_name=resource_group_name,
        service_name=service_name,
        product_id=product_id,
        delete_subscriptions=delete_subscriptions,
        if_match="*" if if_match is None else if_match)


# Named Value Operations

def apim_nv_create(
        client, resource_group_name, service_name, named_value_id, display_name, value=None, tags=None, secret=False,
        if_match=None, no_wait=False):
    """Creates a new Named Value. """

    parameters = NamedValueCreateContract(
        tags=tags,
        secret=secret,
        display_name=display_name,
        value=value
    )

    return sdk_no_wait(no_wait, client.named_value.begin_create_or_update,
                       resource_group_name=resource_group_name,
                       service_name=service_name, named_value_id=named_value_id,
                       parameters=parameters, if_match="*" if if_match is None else if_match)


def apim_nv_get(client, resource_group_name, service_name, named_value_id):
    """Shows details of a Named Value. """

    return client.named_value.get(resource_group_name, service_name, named_value_id)


def apim_nv_show_secret(client, resource_group_name, service_name, named_value_id):
    """Gets the secret of the NamedValue."""

    return client.named_value.list_value(resource_group_name, service_name, named_value_id)


def apim_nv_list(client, resource_group_name, service_name):
    """List all Named Values of an API Management instance. """

    return client.named_value.list_by_service(resource_group_name, service_name)


def apim_nv_delete(client, resource_group_name, service_name, named_value_id):
    """Deletes an existing Named Value. """

    return client.named_value.delete(resource_group_name, service_name, named_value_id, if_match='*')


def apim_nv_update(instance, value=None, tags=None, secret=None):
    """Updates an existing Named Value."""
    if tags is not None:
        instance.tags = tags

    if value is not None:
        instance.value = value

    if secret is not None:
        instance.secret = secret

    return instance


def apim_api_operation_list(client, resource_group_name, service_name, api_id):
    """List a collection of the operations for the specified API."""

    return client.api_operation.list_by_api(resource_group_name, service_name, api_id)


def apim_api_operation_get(client, resource_group_name, service_name, api_id, operation_id):
    """Gets the details of the API Operation specified by its identifier."""

    return client.api_operation.get(resource_group_name, service_name, api_id, operation_id)


def apim_api_operation_create(
        client, resource_group_name, service_name, api_id, url_template, method, display_name, template_parameters=None,
        operation_id=None, description=None, if_match=None, no_wait=False):
    """Creates a new operation in the API or updates an existing one."""

    if operation_id is None:
        operation_id = uuid.uuid4().hex

    resource = OperationContract(
        description=description,
        display_name=display_name,
        method=method,
        url_template=url_template,
        template_parameters=template_parameters)

    return sdk_no_wait(
        no_wait,
        client.api_operation.create_or_update,
        resource_group_name=resource_group_name,
        service_name=service_name,
        api_id=api_id,
        operation_id=operation_id,
        parameters=resource,
        if_match="*" if if_match is None else if_match)


def apim_api_operation_update(instance, display_name=None, description=None, method=None, url_template=None):
    """Updates the details of the operation in the API specified by its identifier."""

    if display_name is not None:
        instance.display_name = display_name

    if description is not None:
        instance.description = description

    if method is not None:
        instance.method = method

    if url_template is not None:
        instance.url_template = url_template

    return instance


def apim_api_operation_delete(
        client, resource_group_name, service_name, api_id, operation_id, if_match=None, no_wait=False):
    """Deletes the specified operation in the API."""

    return sdk_no_wait(
        no_wait,
        client.api_operation.delete,
        resource_group_name=resource_group_name,
        service_name=service_name,
        api_id=api_id,
        operation_id=operation_id,
        if_match="*" if if_match is None else if_match)


def apim_api_release_list(client, resource_group_name, service_name, api_id):
    """Lists all releases of an API."""

    return client.api_release.list_by_service(resource_group_name, service_name, api_id)


def apim_api_release_show(client, resource_group_name, service_name, api_id, release_id):
    """Returns the details of an API release."""

    return client.api_release.get(resource_group_name, service_name, api_id, release_id)


def apim_api_release_create(
        client, resource_group_name, service_name, api_id, api_revision, release_id=None, if_match=None, notes=None):
    """Creates a new Release for the API."""

    if release_id is None:
        release_id = uuid.uuid4().hex

    api_id_extended_with_revision = "/apis/" + api_id + ";rev=" + api_revision

    parameter = ApiReleaseContract(notes=notes, api_id=api_id_extended_with_revision)

    return client.api_release.create_or_update(
        resource_group_name, service_name, api_id,
        release_id, parameter, "*" if if_match is None else if_match)


def apim_api_release_update(instance, notes=None):
    """Updates the details of the release of the API specified by its identifier."""

    instance.notes = notes

    return instance


def apim_api_release_delete(client, resource_group_name, service_name, api_id, release_id, if_match=None):
    """Deletes the specified release in the API."""

    return client.api_release.delete(
        resource_group_name, service_name, api_id, release_id, "*" if if_match is None else if_match)


def apim_api_revision_list(client, resource_group_name, service_name, api_id):
    """Lists all revisions of an API."""

    return client.api_revision.list_by_service(resource_group_name, service_name, api_id)


def apim_api_revision_create(client, resource_group_name, service_name, api_id, api_revision,
                             api_revision_description=None, no_wait=False):
    """Creates a new API Revision. """

    cur_api = client.api.get(resource_group_name, service_name, api_id)

    parameters = ApiCreateOrUpdateParameter(
        path=cur_api.path,
        display_name=cur_api.display_name,
        service_url=cur_api.service_url,
        authentication_settings=cur_api.authentication_settings,
        protocols=cur_api.protocols,
        subscription_key_parameter_names=cur_api.subscription_key_parameter_names,
        api_revision_description=api_revision_description,
        source_api_id="/apis/" + api_id
    )

    return sdk_no_wait(no_wait, client.api.begin_create_or_update,
                       resource_group_name=resource_group_name, service_name=service_name,
                       api_id=api_id + ";rev=" + api_revision, parameters=parameters)


def apim_api_vs_list(client, resource_group_name, service_name):
    """Lists a collection of API Version Sets in the specified service instance."""

    return client.api_version_set.list_by_service(resource_group_name, service_name)


def apim_api_vs_show(client, resource_group_name, service_name, version_set_id):
    """Gets the details of the Api Version Set specified by its identifier."""

    return client.api_version_set.get(resource_group_name, service_name, version_set_id)


def apim_api_vs_create(
        client, resource_group_name, service_name, display_name, versioning_scheme, version_set_id=None, if_match=None,
        description=None, version_query_name=None, version_header_name=None, no_wait=False):
    """Creates or Updates a Api Version Set."""

    if version_set_id is None:
        version_set_id = uuid.uuid4().hex

    resource = ApiVersionSetContract(
        description=description,
        versioning_scheme=versioning_scheme,
        display_name=display_name)

    if versioning_scheme == VersioningScheme.header:
        if version_header_name is None:
            raise RequiredArgumentMissingError(
                "Please specify version header name while using 'header' as version scheme.")

        resource.version_header_name = version_header_name

    if versioning_scheme == VersioningScheme.query:
        if version_query_name is None:
            raise RequiredArgumentMissingError(
                "Please specify version query name while using 'query' as version scheme.")

        resource.version_query_name = version_query_name

    return sdk_no_wait(
        no_wait,
        client.api_version_set.create_or_update,
        resource_group_name=resource_group_name,
        service_name=service_name,
        version_set_id=version_set_id,
        parameters=resource,
        if_match="*" if if_match is None else if_match)


def apim_api_vs_update(
        instance, versioning_scheme=None, description=None, display_name=None, version_header_name=None,
        version_query_name=None):
    """Updates the details of the Api VersionSet specified by its identifier."""

    if display_name is not None:
        instance.display_name = display_name

    if versioning_scheme is not None:
        instance.versioning_scheme = versioning_scheme
        if versioning_scheme == VersioningScheme.header:
            if version_header_name is None:
                raise RequiredArgumentMissingError(
                    "Please specify version header name while using 'header' as version scheme.")

            instance.version_header_name = version_header_name
            instance.version_query_name = None
        if versioning_scheme == VersioningScheme.query:
            if version_query_name is None:
                raise RequiredArgumentMissingError(
                    "Please specify version query name while using 'query' as version scheme.")

            instance.version_query_name = version_query_name
            instance.version_header_name = None

    if description is None:
        instance.description = description

    return instance


def apim_api_vs_delete(client, resource_group_name, service_name, version_set_id, if_match=None, no_wait=False):
    """Deletes specific Api Version Set."""

    return sdk_no_wait(
        no_wait,
        client.api_version_set.delete,
        resource_group_name=resource_group_name,
        service_name=service_name,
        version_set_id=version_set_id,
        if_match="*" if if_match is None else if_match)
