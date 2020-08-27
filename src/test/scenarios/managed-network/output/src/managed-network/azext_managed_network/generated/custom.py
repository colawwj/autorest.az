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

from azure.cli.core.util import sdk_no_wait


def managed_network_mn_list(client,
                            resource_group_name=None,
                            top=None,
                            skiptoken=None):
    if resource_group_name:
        return client.list_by_resource_group(resource_group_name=resource_group_name,
                                             top=top,
                                             skiptoken=skiptoken)
    return client.list_by_subscription(top=top,
                                       skiptoken=skiptoken)


def managed_network_mn_create(client,
                              resource_group_name,
                              managed_network_name,
                              location,
                              tags=None,
                              properties=None):
    return client.create_or_update(resource_group_name=resource_group_name,
                                   managed_network_name=managed_network_name,
                                   location=location,
                                   tags=tags,
                                   properties=properties)


def managed_network_mn_update(client,
                              resource_group_name,
                              managed_network_name,
                              tags=None):
    return client.begin_update(resource_group_name=resource_group_name,
                               managed_network_name=managed_network_name,
                               tags=tags)


def managed_network_mn_delete(client,
                              resource_group_name,
                              managed_network_name):
    return client.begin_delete(resource_group_name=resource_group_name,
                               managed_network_name=managed_network_name)


def managed_network_mn_get_modify(client,
                                  resource_group_name,
                                  managed_network_name):
    return client.get_modify(resource_group_name=resource_group_name,
                             managed_network_name=managed_network_name)


def managed_network_mn_scope_assignment_list(client,
                                             scope):
    return client.list(scope=scope)


def managed_network_mn_scope_assignment_show(client,
                                             scope,
                                             scope_assignment_name):
    return client.get(scope=scope,
                      scope_assignment_name=scope_assignment_name)


def managed_network_mn_scope_assignment_create(client,
                                               scope,
                                               scope_assignment_name,
                                               location,
                                               assigned_managed_network=None):
    return client.create_or_update(scope=scope,
                                   scope_assignment_name=scope_assignment_name,
                                   location=location,
                                   assigned_managed_network=assigned_managed_network)


def managed_network_mn_scope_assignment_update(client,
                                               scope,
                                               scope_assignment_name,
                                               location,
                                               assigned_managed_network=None):
    return client.create_or_update(scope=scope,
                                   scope_assignment_name=scope_assignment_name,
                                   location=location,
                                   assigned_managed_network=assigned_managed_network)


def managed_network_mn_scope_assignment_delete(client,
                                               scope,
                                               scope_assignment_name):
    return client.delete(scope=scope,
                         scope_assignment_name=scope_assignment_name)


def managed_network_mn_group_list(client,
                                  resource_group_name,
                                  managed_network_name,
                                  top=None,
                                  skiptoken=None):
    return client.list_by_managed_network(resource_group_name=resource_group_name,
                                          managed_network_name=managed_network_name,
                                          top=top,
                                          skiptoken=skiptoken)


def managed_network_mn_group_show(client,
                                  resource_group_name,
                                  managed_network_name,
                                  group_name):
    return client.get(resource_group_name=resource_group_name,
                      managed_network_name=managed_network_name,
                      managed_network_group_name=group_name)


def managed_network_mn_group_create(client,
                                    resource_group_name,
                                    managed_network_name,
                                    group_name,
                                    location,
                                    management_groups=None,
                                    subscriptions=None,
                                    virtual_networks=None,
                                    subnets=None,
                                    no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       resource_group_name=resource_group_name,
                       managed_network_name=managed_network_name,
                       managed_network_group_name=group_name,
                       location=location,
                       kind="Connectivity",
                       management_groups=management_groups,
                       subscriptions=subscriptions,
                       virtual_networks=virtual_networks,
                       subnets=subnets)


def managed_network_mn_group_update(client,
                                    resource_group_name,
                                    managed_network_name,
                                    group_name,
                                    location,
                                    management_groups=None,
                                    subscriptions=None,
                                    virtual_networks=None,
                                    subnets=None,
                                    no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       resource_group_name=resource_group_name,
                       managed_network_name=managed_network_name,
                       managed_network_group_name=group_name,
                       location=location,
                       kind="Connectivity",
                       management_groups=management_groups,
                       subscriptions=subscriptions,
                       virtual_networks=virtual_networks,
                       subnets=subnets)


def managed_network_mn_group_delete(client,
                                    resource_group_name,
                                    managed_network_name,
                                    group_name,
                                    no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_delete,
                       resource_group_name=resource_group_name,
                       managed_network_name=managed_network_name,
                       managed_network_group_name=group_name)


def managed_network_managed_network_peering_policy_list(client,
                                                        resource_group_name,
                                                        managed_network_name,
                                                        top=None,
                                                        skiptoken=None):
    return client.list_by_managed_network(resource_group_name=resource_group_name,
                                          managed_network_name=managed_network_name,
                                          top=top,
                                          skiptoken=skiptoken)


def managed_network_managed_network_peering_policy_show(client,
                                                        resource_group_name,
                                                        managed_network_name,
                                                        policy_name):
    return client.get(resource_group_name=resource_group_name,
                      managed_network_name=managed_network_name,
                      managed_network_peering_policy_name=policy_name)


def managed_network_managed_network_peering_policy_hub_and_spoke_topology_create(client,
                                                                                 resource_group_name,
                                                                                 managed_network_name,
                                                                                 policy_name,
                                                                                 location,
                                                                                 hub=None,
                                                                                 spokes=None,
                                                                                 mesh=None,
                                                                                 no_wait=False):
    properties = {}
    properties['type'] = 'HubAndSpokeTopology'
    properties['hub'] = hub
    properties['spokes'] = spokes
    properties['mesh'] = mesh
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       resource_group_name=resource_group_name,
                       managed_network_name=managed_network_name,
                       managed_network_peering_policy_name=policy_name,
                       location=location,
                       properties=properties)


def managed_network_managed_network_peering_policy_mesh_topology_create(client,
                                                                        resource_group_name,
                                                                        managed_network_name,
                                                                        policy_name,
                                                                        location,
                                                                        hub=None,
                                                                        spokes=None,
                                                                        mesh=None,
                                                                        no_wait=False):
    properties = {}
    properties['type'] = 'MeshTopology'
    properties['hub'] = hub
    properties['spokes'] = spokes
    properties['mesh'] = mesh
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       resource_group_name=resource_group_name,
                       managed_network_name=managed_network_name,
                       managed_network_peering_policy_name=policy_name,
                       location=location,
                       properties=properties)


def managed_network_managed_network_peering_policy_hub_and_spoke_topology_update(client,
                                                                                 resource_group_name,
                                                                                 managed_network_name,
                                                                                 policy_name,
                                                                                 location,
                                                                                 hub=None,
                                                                                 spokes=None,
                                                                                 mesh=None,
                                                                                 no_wait=False):
    properties = {}
    properties['type'] = 'HubAndSpokeTopology'
    properties['hub'] = hub
    properties['spokes'] = spokes
    properties['mesh'] = mesh
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       resource_group_name=resource_group_name,
                       managed_network_name=managed_network_name,
                       managed_network_peering_policy_name=policy_name,
                       location=location,
                       properties=properties)


def managed_network_managed_network_peering_policy_mesh_topology_update(client,
                                                                        resource_group_name,
                                                                        managed_network_name,
                                                                        policy_name,
                                                                        location,
                                                                        hub=None,
                                                                        spokes=None,
                                                                        mesh=None,
                                                                        no_wait=False):
    properties = {}
    properties['type'] = 'MeshTopology'
    properties['hub'] = hub
    properties['spokes'] = spokes
    properties['mesh'] = mesh
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       resource_group_name=resource_group_name,
                       managed_network_name=managed_network_name,
                       managed_network_peering_policy_name=policy_name,
                       location=location,
                       properties=properties)


def managed_network_managed_network_peering_policy_delete(client,
                                                          resource_group_name,
                                                          managed_network_name,
                                                          policy_name,
                                                          no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_delete,
                       resource_group_name=resource_group_name,
                       managed_network_name=managed_network_name,
                       managed_network_peering_policy_name=policy_name)
