# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=unused-argument

from knack.util import CLIError
from azure.cli.core.util import sdk_no_wait


def datafactory_list(client,
                     resource_group_name=None):
    if resource_group_name:
        return client.list_by_resource_group(resource_group_name=resource_group_name)
    return client.list()


def datafactory_show(client,
                     resource_group_name,
                     factory_name,
                     if_none_match=None):
    return client.get(resource_group_name=resource_group_name,
                      factory_name=factory_name,
                      if_none_match=if_none_match)


def datafactory_create(client,
                       resource_group_name,
                       factory_name,
                       if_match=None,
                       location=None,
                       tags=None,
                       factory_vsts_configuration=None,
                       factory_git_hub_configuration=None,
                       fake_identity=None,
                       zones=None):
    all_repo_configuration = []
    if factory_vsts_configuration is not None:
        all_repo_configuration.append(factory_vsts_configuration)
    if factory_git_hub_configuration is not None:
        all_repo_configuration.append(factory_git_hub_configuration)
    if len(all_repo_configuration) > 1:
        raise CLIError('at most one of  factory_vsts_configuration, factory_git_hub_configuration is needed for '
                       'repo_configuration!')
    repo_configuration = all_repo_configuration[0] if len(all_repo_configuration) == 1 else None
    return client.create_or_update(resource_group_name=resource_group_name,
                                   factory_name=factory_name,
                                   if_match=if_match,
                                   location=location,
                                   tags=tags,
                                   repo_configuration=repo_configuration,
                                   fake_identity=fake_identity,
                                   zones=zones,
                                   type="SystemAssigned")


def datafactory_update(client,
                       resource_group_name,
                       factory_name,
                       tags=None):
    return client.update(resource_group_name=resource_group_name,
                         factory_name=factory_name,
                         tags=tags,
                         type="SystemAssigned")


def datafactory_delete(client,
                       resource_group_name,
                       factory_name):
    return client.delete(resource_group_name=resource_group_name,
                         factory_name=factory_name)


def datafactory_configure_factory_repo(client,
                                       location_id,
                                       factory_resource_id=None,
                                       factory_vsts_configuration=None,
                                       factory_git_hub_configuration=None):
    all_repo_configuration = []
    if factory_vsts_configuration is not None:
        all_repo_configuration.append(factory_vsts_configuration)
    if factory_git_hub_configuration is not None:
        all_repo_configuration.append(factory_git_hub_configuration)
    if len(all_repo_configuration) > 1:
        raise CLIError('at most one of  factory_vsts_configuration, factory_git_hub_configuration is needed for '
                       'repo_configuration!')
    repo_configuration = all_repo_configuration[0] if len(all_repo_configuration) == 1 else None
    return client.configure_factory_repo(location_id=location_id,
                                         factory_resource_id=factory_resource_id,
                                         repo_configuration=repo_configuration)


def datafactory_get_data_plane_access(client,
                                      resource_group_name,
                                      factory_name,
                                      permissions=None,
                                      access_resource_path=None,
                                      profile_name=None,
                                      start_time=None,
                                      expire_time=None):
    return client.get_data_plane_access(resource_group_name=resource_group_name,
                                        factory_name=factory_name,
                                        permissions=permissions,
                                        access_resource_path=access_resource_path,
                                        profile_name=profile_name,
                                        start_time=start_time,
                                        expire_time=expire_time)


def datafactory_get_git_hub_access_token(client,
                                         resource_group_name,
                                         factory_name,
                                         git_hub_access_code,
                                         git_hub_access_token_base_url,
                                         git_hub_client_id=None):
    return client.get_git_hub_access_token(resource_group_name=resource_group_name,
                                           factory_name=factory_name,
                                           git_hub_access_code=git_hub_access_code,
                                           git_hub_client_id=git_hub_client_id,
                                           git_hub_access_token_base_url=git_hub_access_token_base_url)


def datafactory_trigger_list(client,
                             resource_group_name,
                             factory_name):
    return client.list_by_factory(resource_group_name=resource_group_name,
                                  factory_name=factory_name)


def datafactory_trigger_show(client,
                             resource_group_name,
                             factory_name,
                             trigger_name,
                             if_none_match=None):
    return client.get(resource_group_name=resource_group_name,
                      factory_name=factory_name,
                      trigger_name=trigger_name,
                      if_none_match=if_none_match)


def datafactory_trigger_create(client,
                               resource_group_name,
                               factory_name,
                               trigger_name,
                               properties,
                               if_match=None):
    return client.create_or_update(resource_group_name=resource_group_name,
                                   factory_name=factory_name,
                                   trigger_name=trigger_name,
                                   if_match=if_match,
                                   properties=properties)


def datafactory_trigger_update(instance,
                               resource_group_name,
                               factory_name,
                               trigger_name,
                               if_match=None,
                               description=None,
                               annotations=None):
    if description is not None:
        instance.properties.description = description
    if annotations is not None:
        instance.properties.annotations = annotations
    return instance.properties


def datafactory_trigger_delete(client,
                               resource_group_name,
                               factory_name,
                               trigger_name):
    return client.delete(resource_group_name=resource_group_name,
                         factory_name=factory_name,
                         trigger_name=trigger_name)


def datafactory_trigger_get_event_subscription_status(client,
                                                      resource_group_name,
                                                      factory_name,
                                                      trigger_name):
    return client.get_event_subscription_status(resource_group_name=resource_group_name,
                                                factory_name=factory_name,
                                                trigger_name=trigger_name)


def datafactory_trigger_query_by_factory(client,
                                         resource_group_name,
                                         factory_name,
                                         continuation_token=None,
                                         parent_trigger_name=None):
    return client.query_by_factory(resource_group_name=resource_group_name,
                                   factory_name=factory_name,
                                   continuation_token_parameter=continuation_token,
                                   parent_trigger_name=parent_trigger_name)


def datafactory_trigger_start(client,
                              resource_group_name,
                              factory_name,
                              trigger_name,
                              no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_start,
                       resource_group_name=resource_group_name,
                       factory_name=factory_name,
                       trigger_name=trigger_name)


def datafactory_trigger_stop(client,
                             resource_group_name,
                             factory_name,
                             trigger_name,
                             no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_stop,
                       resource_group_name=resource_group_name,
                       factory_name=factory_name,
                       trigger_name=trigger_name)


def datafactory_trigger_subscribe_to_event(client,
                                           resource_group_name,
                                           factory_name,
                                           trigger_name,
                                           no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_subscribe_to_event,
                       resource_group_name=resource_group_name,
                       factory_name=factory_name,
                       trigger_name=trigger_name)


def datafactory_trigger_unsubscribe_from_event(client,
                                               resource_group_name,
                                               factory_name,
                                               trigger_name,
                                               no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_unsubscribe_from_event,
                       resource_group_name=resource_group_name,
                       factory_name=factory_name,
                       trigger_name=trigger_name)


def datafactory_integration_runtime_list(client,
                                         resource_group_name,
                                         factory_name):
    return client.list_by_factory(resource_group_name=resource_group_name,
                                  factory_name=factory_name)


def datafactory_integration_runtime_show(client,
                                         resource_group_name,
                                         factory_name,
                                         integration_runtime_name,
                                         if_none_match=None):
    return client.get(resource_group_name=resource_group_name,
                      factory_name=factory_name,
                      integration_runtime_name=integration_runtime_name,
                      if_none_match=if_none_match)


def datafactory_integration_runtime_linked_integration_runtime_create(client,
                                                                      resource_group_name,
                                                                      factory_name,
                                                                      integration_runtime_name,
                                                                      name=None,
                                                                      subscription_id=None,
                                                                      data_factory_name=None,
                                                                      data_factory_location=None):
    return client.create_linked_integration_runtime(resource_group_name=resource_group_name,
                                                    factory_name=factory_name,
                                                    integration_runtime_name=integration_runtime_name,
                                                    name=name,
                                                    subscription_id=subscription_id,
                                                    data_factory_name=data_factory_name,
                                                    data_factory_location=data_factory_location)


def datafactory_integration_runtime_managed_create(client,
                                                   resource_group_name,
                                                   factory_name,
                                                   integration_runtime_name,
                                                   if_match=None,
                                                   description=None,
                                                   factory_vsts_configuration=None,
                                                   factory_git_hub_configuration=None,
                                                   fake_identity=None,
                                                   zones=None,
                                                   type_properties_compute_properties=None,
                                                   type_properties_ssis_properties=None):
    all_repo_configuration = []
    if factory_vsts_configuration is not None:
        all_repo_configuration.append(factory_vsts_configuration)
    if factory_git_hub_configuration is not None:
        all_repo_configuration.append(factory_git_hub_configuration)
    if len(all_repo_configuration) > 1:
        raise CLIError('at most one of  factory_vsts_configuration, factory_git_hub_configuration is needed for '
                       'repo_configuration!')
    repo_configuration = all_repo_configuration[0] if len(all_repo_configuration) == 1 else None
    properties = {}
    properties['type'] = 'Managed'
    properties['description'] = description
    properties['repo_configuration'] = repo_configuration
    properties['fake_identity'] = fake_identity
    properties['zones'] = zones
    properties['compute_properties'] = type_properties_compute_properties
    properties['ssis_properties'] = type_properties_ssis_properties
    return client.create_or_update(resource_group_name=resource_group_name,
                                   factory_name=factory_name,
                                   integration_runtime_name=integration_runtime_name,
                                   if_match=if_match,
                                   properties=properties)


def datafactory_integration_runtime_self_hosted_create(client,
                                                       resource_group_name,
                                                       factory_name,
                                                       integration_runtime_name,
                                                       if_match=None,
                                                       description=None,
                                                       type_properties_linked_info=None):
    properties = {}
    properties['type'] = 'SelfHosted'
    properties['description'] = description
    properties['linked_info'] = type_properties_linked_info
    return client.create_or_update(resource_group_name=resource_group_name,
                                   factory_name=factory_name,
                                   integration_runtime_name=integration_runtime_name,
                                   if_match=if_match,
                                   properties=properties)


def datafactory_integration_runtime_update(client,
                                           resource_group_name,
                                           factory_name,
                                           integration_runtime_name,
                                           auto_update=None,
                                           update_delay_offset=None):
    return client.update(resource_group_name=resource_group_name,
                         factory_name=factory_name,
                         integration_runtime_name=integration_runtime_name,
                         auto_update=auto_update,
                         update_delay_offset=update_delay_offset)


def datafactory_integration_runtime_delete(client,
                                           resource_group_name,
                                           factory_name,
                                           integration_runtime_name):
    return client.delete(resource_group_name=resource_group_name,
                         factory_name=factory_name,
                         integration_runtime_name=integration_runtime_name)


def datafactory_integration_runtime_get_connection_info(client,
                                                        resource_group_name,
                                                        factory_name,
                                                        integration_runtime_name):
    return client.get_connection_info(resource_group_name=resource_group_name,
                                      factory_name=factory_name,
                                      integration_runtime_name=integration_runtime_name)


def datafactory_integration_runtime_get_monitoring_data(client,
                                                        resource_group_name,
                                                        factory_name,
                                                        integration_runtime_name):
    return client.get_monitoring_data(resource_group_name=resource_group_name,
                                      factory_name=factory_name,
                                      integration_runtime_name=integration_runtime_name)


def datafactory_integration_runtime_get_status(client,
                                               resource_group_name,
                                               factory_name,
                                               integration_runtime_name):
    return client.get_status(resource_group_name=resource_group_name,
                             factory_name=factory_name,
                             integration_runtime_name=integration_runtime_name)


def datafactory_integration_runtime_list_auth_key(client,
                                                  resource_group_name,
                                                  factory_name,
                                                  integration_runtime_name):
    return client.list_auth_key(resource_group_name=resource_group_name,
                                factory_name=factory_name,
                                integration_runtime_name=integration_runtime_name)


def datafactory_integration_runtime_regenerate_auth_key(client,
                                                        resource_group_name,
                                                        factory_name,
                                                        integration_runtime_name,
                                                        key_name=None):
    return client.regenerate_auth_key(resource_group_name=resource_group_name,
                                      factory_name=factory_name,
                                      integration_runtime_name=integration_runtime_name,
                                      key_name=key_name)


def datafactory_integration_runtime_remove_link(client,
                                                resource_group_name,
                                                factory_name,
                                                integration_runtime_name,
                                                linked_factory_name):
    return client.remove_link(resource_group_name=resource_group_name,
                              factory_name=factory_name,
                              integration_runtime_name=integration_runtime_name,
                              linked_factory_name=linked_factory_name)


def datafactory_integration_runtime_start(client,
                                          resource_group_name,
                                          factory_name,
                                          integration_runtime_name,
                                          no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_start,
                       resource_group_name=resource_group_name,
                       factory_name=factory_name,
                       integration_runtime_name=integration_runtime_name)


def datafactory_integration_runtime_stop(client,
                                         resource_group_name,
                                         factory_name,
                                         integration_runtime_name,
                                         no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_stop,
                       resource_group_name=resource_group_name,
                       factory_name=factory_name,
                       integration_runtime_name=integration_runtime_name)


def datafactory_integration_runtime_sync_credentials(client,
                                                     resource_group_name,
                                                     factory_name,
                                                     integration_runtime_name):
    return client.sync_credentials(resource_group_name=resource_group_name,
                                   factory_name=factory_name,
                                   integration_runtime_name=integration_runtime_name)


def datafactory_integration_runtime_upgrade(client,
                                            resource_group_name,
                                            factory_name,
                                            integration_runtime_name):
    return client.upgrade(resource_group_name=resource_group_name,
                          factory_name=factory_name,
                          integration_runtime_name=integration_runtime_name)
