# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Dict, List, Optional

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class ErrorResponse(msrest.serialization.Model):
    """The error response that indicates why an operation has failed.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.code = None
        self.message = None


class ResourceProperties(msrest.serialization.Model):
    """Base for resource properties.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar provisioning_state: Provisioning state of the ManagedNetwork resource. Possible values
     include: "Updating", "Deleting", "Failed", "Succeeded".
    :vartype provisioning_state: str or ~managed_network_management_client.models.ProvisioningState
    :ivar etag: A unique read-only string that changes whenever the resource is updated.
    :vartype etag: str
    """

    _validation = {
        'provisioning_state': {'readonly': True},
        'etag': {'readonly': True},
    }

    _attribute_map = {
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ResourceProperties, self).__init__(**kwargs)
        self.provisioning_state = None
        self.etag = None


class ManagedNetworkPeeringPolicyProperties(ResourceProperties):
    """Properties of a Managed Network Peering Policy.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: HubAndSpokePeeringPolicyProperties, MeshPeeringPolicyProperties.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar provisioning_state: Provisioning state of the ManagedNetwork resource. Possible values
     include: "Updating", "Deleting", "Failed", "Succeeded".
    :vartype provisioning_state: str or ~managed_network_management_client.models.ProvisioningState
    :ivar etag: A unique read-only string that changes whenever the resource is updated.
    :vartype etag: str
    :param type: Required. Gets or sets the connectivity type of a network structure
     policy.Constant filled by server.  Possible values include: "HubAndSpokeTopology",
     "MeshTopology".
    :type type: str or ~managed_network_management_client.models.Type
    :param hub: Gets or sets the hub virtual network ID.
    :type hub: ~managed_network_management_client.models.ResourceId
    :param spokes: Gets or sets the spokes group IDs.
    :type spokes: list[~managed_network_management_client.models.ResourceId]
    :param mesh: Gets or sets the mesh group IDs.
    :type mesh: list[~managed_network_management_client.models.ResourceId]
    """

    _validation = {
        'provisioning_state': {'readonly': True},
        'etag': {'readonly': True},
        'type': {'required': True},
    }

    _attribute_map = {
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'hub': {'key': 'hub', 'type': 'ResourceId'},
        'spokes': {'key': 'spokes', 'type': '[ResourceId]'},
        'mesh': {'key': 'mesh', 'type': '[ResourceId]'},
    }

    _subtype_map = {
        'type': {'HubAndSpokeTopology': 'HubAndSpokePeeringPolicyProperties', 'MeshTopology': 'MeshPeeringPolicyProperties'}
    }

    def __init__(
        self,
        *,
        hub: Optional["ResourceId"] = None,
        spokes: Optional[List["ResourceId"]] = None,
        mesh: Optional[List["ResourceId"]] = None,
        **kwargs
    ):
        super(ManagedNetworkPeeringPolicyProperties, self).__init__(**kwargs)
        self.type: str = 'ManagedNetworkPeeringPolicyProperties'
        self.hub = hub
        self.spokes = spokes
        self.mesh = mesh


class HubAndSpokePeeringPolicyProperties(ManagedNetworkPeeringPolicyProperties):
    """Properties of a Hub and Spoke Peering Policy.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar provisioning_state: Provisioning state of the ManagedNetwork resource. Possible values
     include: "Updating", "Deleting", "Failed", "Succeeded".
    :vartype provisioning_state: str or ~managed_network_management_client.models.ProvisioningState
    :ivar etag: A unique read-only string that changes whenever the resource is updated.
    :vartype etag: str
    :param type: Required. Gets or sets the connectivity type of a network structure
     policy.Constant filled by server.  Possible values include: "HubAndSpokeTopology",
     "MeshTopology".
    :type type: str or ~managed_network_management_client.models.Type
    :param hub: Gets or sets the hub virtual network ID.
    :type hub: ~managed_network_management_client.models.ResourceId
    :param spokes: Gets or sets the spokes group IDs.
    :type spokes: list[~managed_network_management_client.models.ResourceId]
    :param mesh: Gets or sets the mesh group IDs.
    :type mesh: list[~managed_network_management_client.models.ResourceId]
    """

    _validation = {
        'provisioning_state': {'readonly': True},
        'etag': {'readonly': True},
        'type': {'required': True},
    }

    _attribute_map = {
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'hub': {'key': 'hub', 'type': 'ResourceId'},
        'spokes': {'key': 'spokes', 'type': '[ResourceId]'},
        'mesh': {'key': 'mesh', 'type': '[ResourceId]'},
    }

    def __init__(
        self,
        *,
        hub: Optional["ResourceId"] = None,
        spokes: Optional[List["ResourceId"]] = None,
        mesh: Optional[List["ResourceId"]] = None,
        **kwargs
    ):
        super(HubAndSpokePeeringPolicyProperties, self).__init__(hub=hub, spokes=spokes, mesh=mesh, **kwargs)
        self.type: str = 'HubAndSpokeTopology'


class Resource(msrest.serialization.Model):
    """The general resource model definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. Ex- Microsoft.Compute/virtualMachines or
     Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param location: The geo-location where the resource lives.
    :type location: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        location: Optional[str] = None,
        **kwargs
    ):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = location


class TrackedResource(Resource):
    """The resource model definition for a ARM tracked top level resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. Ex- Microsoft.Compute/virtualMachines or
     Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param location: The geo-location where the resource lives.
    :type location: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        *,
        location: Optional[str] = None,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(TrackedResource, self).__init__(location=location, **kwargs)
        self.tags = tags


class ManagedNetwork(TrackedResource):
    """The Managed Network resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. Ex- Microsoft.Compute/virtualMachines or
     Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param location: The geo-location where the resource lives.
    :type location: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :ivar provisioning_state: Provisioning state of the ManagedNetwork resource. Possible values
     include: "Updating", "Deleting", "Failed", "Succeeded".
    :vartype provisioning_state: str or ~managed_network_management_client.models.ProvisioningState
    :ivar etag: A unique read-only string that changes whenever the resource is updated.
    :vartype etag: str
    :ivar groups: The collection of connectivity related Managed Network Groups within the Managed
     Network.
    :vartype groups: list[~managed_network_management_client.models.ManagedNetworkGroup]
    :ivar peerings: The collection of Managed Network Peering Policies within the Managed Network.
    :vartype peerings: list[~managed_network_management_client.models.ManagedNetworkPeeringPolicy]
    :param management_groups: The collection of management groups covered by the Managed Network.
    :type management_groups: list[~managed_network_management_client.models.ResourceId]
    :param subscriptions: The collection of subscriptions covered by the Managed Network.
    :type subscriptions: list[~managed_network_management_client.models.ResourceId]
    :param virtual_networks: The collection of virtual nets covered by the Managed Network.
    :type virtual_networks: list[~managed_network_management_client.models.ResourceId]
    :param subnets: The collection of  subnets covered by the Managed Network.
    :type subnets: list[~managed_network_management_client.models.ResourceId]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'etag': {'readonly': True},
        'groups': {'readonly': True},
        'peerings': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'etag': {'key': 'properties.etag', 'type': 'str'},
        'groups': {'key': 'properties.connectivity.groups', 'type': '[ManagedNetworkGroup]'},
        'peerings': {'key': 'properties.connectivity.peerings', 'type': '[ManagedNetworkPeeringPolicy]'},
        'management_groups': {'key': 'properties.scope.managementGroups', 'type': '[ResourceId]'},
        'subscriptions': {'key': 'properties.scope.subscriptions', 'type': '[ResourceId]'},
        'virtual_networks': {'key': 'properties.scope.virtualNetworks', 'type': '[ResourceId]'},
        'subnets': {'key': 'properties.scope.subnets', 'type': '[ResourceId]'},
    }

    def __init__(
        self,
        *,
        location: Optional[str] = None,
        tags: Optional[Dict[str, str]] = None,
        management_groups: Optional[List["ResourceId"]] = None,
        subscriptions: Optional[List["ResourceId"]] = None,
        virtual_networks: Optional[List["ResourceId"]] = None,
        subnets: Optional[List["ResourceId"]] = None,
        **kwargs
    ):
        super(ManagedNetwork, self).__init__(location=location, tags=tags, **kwargs)
        self.provisioning_state = None
        self.etag = None
        self.groups = None
        self.peerings = None
        self.management_groups = management_groups
        self.subscriptions = subscriptions
        self.virtual_networks = virtual_networks
        self.subnets = subnets


class ManagedNetworkGroup(Resource):
    """The Managed Network Group resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. Ex- Microsoft.Compute/virtualMachines or
     Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param location: The geo-location where the resource lives.
    :type location: str
    :ivar kind: Responsibility role under which this Managed Network Group will be created. Default
     value: "Connectivity".
    :vartype kind: str
    :ivar provisioning_state: Provisioning state of the ManagedNetwork resource. Possible values
     include: "Updating", "Deleting", "Failed", "Succeeded".
    :vartype provisioning_state: str or ~managed_network_management_client.models.ProvisioningState
    :ivar etag: A unique read-only string that changes whenever the resource is updated.
    :vartype etag: str
    :param management_groups: The collection of management groups covered by the Managed Network.
    :type management_groups: list[~managed_network_management_client.models.ResourceId]
    :param subscriptions: The collection of subscriptions covered by the Managed Network.
    :type subscriptions: list[~managed_network_management_client.models.ResourceId]
    :param virtual_networks: The collection of virtual nets covered by the Managed Network.
    :type virtual_networks: list[~managed_network_management_client.models.ResourceId]
    :param subnets: The collection of  subnets covered by the Managed Network.
    :type subnets: list[~managed_network_management_client.models.ResourceId]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'kind': {'constant': True},
        'provisioning_state': {'readonly': True},
        'etag': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'etag': {'key': 'properties.etag', 'type': 'str'},
        'management_groups': {'key': 'properties.managementGroups', 'type': '[ResourceId]'},
        'subscriptions': {'key': 'properties.subscriptions', 'type': '[ResourceId]'},
        'virtual_networks': {'key': 'properties.virtualNetworks', 'type': '[ResourceId]'},
        'subnets': {'key': 'properties.subnets', 'type': '[ResourceId]'},
    }

    kind = "Connectivity"

    def __init__(
        self,
        *,
        location: Optional[str] = None,
        management_groups: Optional[List["ResourceId"]] = None,
        subscriptions: Optional[List["ResourceId"]] = None,
        virtual_networks: Optional[List["ResourceId"]] = None,
        subnets: Optional[List["ResourceId"]] = None,
        **kwargs
    ):
        super(ManagedNetworkGroup, self).__init__(location=location, **kwargs)
        self.provisioning_state = None
        self.etag = None
        self.management_groups = management_groups
        self.subscriptions = subscriptions
        self.virtual_networks = virtual_networks
        self.subnets = subnets


class ManagedNetworkGroupListResult(msrest.serialization.Model):
    """Result of the request to list Managed Network Groups. It contains a list of groups and a URL link to get the next set of results.

    :param value: Gets a page of ManagedNetworkGroup.
    :type value: list[~managed_network_management_client.models.ManagedNetworkGroup]
    :param next_link: Gets the URL to get the next set of results.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ManagedNetworkGroup]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["ManagedNetworkGroup"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(ManagedNetworkGroupListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class ManagedNetworkGroupProperties(ResourceProperties):
    """Properties of a Managed Network Group.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar provisioning_state: Provisioning state of the ManagedNetwork resource. Possible values
     include: "Updating", "Deleting", "Failed", "Succeeded".
    :vartype provisioning_state: str or ~managed_network_management_client.models.ProvisioningState
    :ivar etag: A unique read-only string that changes whenever the resource is updated.
    :vartype etag: str
    :param management_groups: The collection of management groups covered by the Managed Network.
    :type management_groups: list[~managed_network_management_client.models.ResourceId]
    :param subscriptions: The collection of subscriptions covered by the Managed Network.
    :type subscriptions: list[~managed_network_management_client.models.ResourceId]
    :param virtual_networks: The collection of virtual nets covered by the Managed Network.
    :type virtual_networks: list[~managed_network_management_client.models.ResourceId]
    :param subnets: The collection of  subnets covered by the Managed Network.
    :type subnets: list[~managed_network_management_client.models.ResourceId]
    """

    _validation = {
        'provisioning_state': {'readonly': True},
        'etag': {'readonly': True},
    }

    _attribute_map = {
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'management_groups': {'key': 'managementGroups', 'type': '[ResourceId]'},
        'subscriptions': {'key': 'subscriptions', 'type': '[ResourceId]'},
        'virtual_networks': {'key': 'virtualNetworks', 'type': '[ResourceId]'},
        'subnets': {'key': 'subnets', 'type': '[ResourceId]'},
    }

    def __init__(
        self,
        *,
        management_groups: Optional[List["ResourceId"]] = None,
        subscriptions: Optional[List["ResourceId"]] = None,
        virtual_networks: Optional[List["ResourceId"]] = None,
        subnets: Optional[List["ResourceId"]] = None,
        **kwargs
    ):
        super(ManagedNetworkGroupProperties, self).__init__(**kwargs)
        self.management_groups = management_groups
        self.subscriptions = subscriptions
        self.virtual_networks = virtual_networks
        self.subnets = subnets


class ManagedNetworkListResult(msrest.serialization.Model):
    """Result of the request to list Managed Network. It contains a list of Managed Networks and a URL link to get the next set of results.

    :param value: Gets a page of ManagedNetworks.
    :type value: list[~managed_network_management_client.models.ManagedNetwork]
    :param next_link: Gets the URL to get the next page of results.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ManagedNetwork]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["ManagedNetwork"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(ManagedNetworkListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class ManagedNetworkPeeringPolicy(Resource):
    """The Managed Network Peering Policy resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. Ex- Microsoft.Compute/virtualMachines or
     Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param location: The geo-location where the resource lives.
    :type location: str
    :param properties: Gets or sets the properties of a Managed Network Policy.
    :type properties:
     ~managed_network_management_client.models.ManagedNetworkPeeringPolicyProperties
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'ManagedNetworkPeeringPolicyProperties'},
    }

    def __init__(
        self,
        *,
        location: Optional[str] = None,
        properties: Optional["ManagedNetworkPeeringPolicyProperties"] = None,
        **kwargs
    ):
        super(ManagedNetworkPeeringPolicy, self).__init__(location=location, **kwargs)
        self.properties = properties


class ManagedNetworkPeeringPolicyListResult(msrest.serialization.Model):
    """Result of the request to list Managed Network Peering Policies. It contains a list of policies and a URL link to get the next set of results.

    :param value: Gets a page of Peering Policies.
    :type value: list[~managed_network_management_client.models.ManagedNetworkPeeringPolicy]
    :param next_link: Gets the URL to get the next page of results.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ManagedNetworkPeeringPolicy]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["ManagedNetworkPeeringPolicy"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(ManagedNetworkPeeringPolicyListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class ManagedNetworkProperties(ResourceProperties):
    """Properties of Managed Network.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar provisioning_state: Provisioning state of the ManagedNetwork resource. Possible values
     include: "Updating", "Deleting", "Failed", "Succeeded".
    :vartype provisioning_state: str or ~managed_network_management_client.models.ProvisioningState
    :ivar etag: A unique read-only string that changes whenever the resource is updated.
    :vartype etag: str
    :ivar groups: The collection of connectivity related Managed Network Groups within the Managed
     Network.
    :vartype groups: list[~managed_network_management_client.models.ManagedNetworkGroup]
    :ivar peerings: The collection of Managed Network Peering Policies within the Managed Network.
    :vartype peerings: list[~managed_network_management_client.models.ManagedNetworkPeeringPolicy]
    :param management_groups: The collection of management groups covered by the Managed Network.
    :type management_groups: list[~managed_network_management_client.models.ResourceId]
    :param subscriptions: The collection of subscriptions covered by the Managed Network.
    :type subscriptions: list[~managed_network_management_client.models.ResourceId]
    :param virtual_networks: The collection of virtual nets covered by the Managed Network.
    :type virtual_networks: list[~managed_network_management_client.models.ResourceId]
    :param subnets: The collection of  subnets covered by the Managed Network.
    :type subnets: list[~managed_network_management_client.models.ResourceId]
    """

    _validation = {
        'provisioning_state': {'readonly': True},
        'etag': {'readonly': True},
        'groups': {'readonly': True},
        'peerings': {'readonly': True},
    }

    _attribute_map = {
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'groups': {'key': 'connectivity.groups', 'type': '[ManagedNetworkGroup]'},
        'peerings': {'key': 'connectivity.peerings', 'type': '[ManagedNetworkPeeringPolicy]'},
        'management_groups': {'key': 'scope.managementGroups', 'type': '[ResourceId]'},
        'subscriptions': {'key': 'scope.subscriptions', 'type': '[ResourceId]'},
        'virtual_networks': {'key': 'scope.virtualNetworks', 'type': '[ResourceId]'},
        'subnets': {'key': 'scope.subnets', 'type': '[ResourceId]'},
    }

    def __init__(
        self,
        *,
        management_groups: Optional[List["ResourceId"]] = None,
        subscriptions: Optional[List["ResourceId"]] = None,
        virtual_networks: Optional[List["ResourceId"]] = None,
        subnets: Optional[List["ResourceId"]] = None,
        **kwargs
    ):
        super(ManagedNetworkProperties, self).__init__(**kwargs)
        self.groups = None
        self.peerings = None
        self.management_groups = management_groups
        self.subscriptions = subscriptions
        self.virtual_networks = virtual_networks
        self.subnets = subnets


class ManagedNetworkUpdate(msrest.serialization.Model):
    """Update Tags of Managed Network.

    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        *,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(ManagedNetworkUpdate, self).__init__(**kwargs)
        self.tags = tags


class MeshPeeringPolicyProperties(ManagedNetworkPeeringPolicyProperties):
    """Properties of a Mesh Peering Policy.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar provisioning_state: Provisioning state of the ManagedNetwork resource. Possible values
     include: "Updating", "Deleting", "Failed", "Succeeded".
    :vartype provisioning_state: str or ~managed_network_management_client.models.ProvisioningState
    :ivar etag: A unique read-only string that changes whenever the resource is updated.
    :vartype etag: str
    :param type: Required. Gets or sets the connectivity type of a network structure
     policy.Constant filled by server.  Possible values include: "HubAndSpokeTopology",
     "MeshTopology".
    :type type: str or ~managed_network_management_client.models.Type
    :param hub: Gets or sets the hub virtual network ID.
    :type hub: ~managed_network_management_client.models.ResourceId
    :param spokes: Gets or sets the spokes group IDs.
    :type spokes: list[~managed_network_management_client.models.ResourceId]
    :param mesh: Gets or sets the mesh group IDs.
    :type mesh: list[~managed_network_management_client.models.ResourceId]
    """

    _validation = {
        'provisioning_state': {'readonly': True},
        'etag': {'readonly': True},
        'type': {'required': True},
    }

    _attribute_map = {
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'hub': {'key': 'hub', 'type': 'ResourceId'},
        'spokes': {'key': 'spokes', 'type': '[ResourceId]'},
        'mesh': {'key': 'mesh', 'type': '[ResourceId]'},
    }

    def __init__(
        self,
        *,
        hub: Optional["ResourceId"] = None,
        spokes: Optional[List["ResourceId"]] = None,
        mesh: Optional[List["ResourceId"]] = None,
        **kwargs
    ):
        super(MeshPeeringPolicyProperties, self).__init__(hub=hub, spokes=spokes, mesh=mesh, **kwargs)
        self.type: str = 'MeshTopology'


class Operation(msrest.serialization.Model):
    """REST API operation.

    :param name: Operation name: {provider}/{resource}/{operation}.
    :type name: str
    :param display: The object that represents the operation.
    :type display: ~managed_network_management_client.models.OperationDisplay
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        display: Optional["OperationDisplay"] = None,
        **kwargs
    ):
        super(Operation, self).__init__(**kwargs)
        self.name = name
        self.display = display


class OperationDisplay(msrest.serialization.Model):
    """The object that represents the operation.

    :param provider: Service provider: Microsoft.ManagedNetwork.
    :type provider: str
    :param resource: Resource on which the operation is performed: Profile, endpoint, etc.
    :type resource: str
    :param operation: Operation type: Read, write, delete, etc.
    :type operation: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        provider: Optional[str] = None,
        resource: Optional[str] = None,
        operation: Optional[str] = None,
        **kwargs
    ):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = provider
        self.resource = resource
        self.operation = operation


class OperationListResult(msrest.serialization.Model):
    """Result of the request to list Managed Network operations. It contains a list of operations and a URL link to get the next set of results.

    :param value: List of Resource Provider operations supported by the Managed Network resource
     provider.
    :type value: list[~managed_network_management_client.models.Operation]
    :param next_link: URL to get the next set of operation list results if there are any.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Operation]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["Operation"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(OperationListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class ProxyResource(Resource):
    """The resource model definition for a ARM proxy resource. It will have everything other than required location and tags.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. Ex- Microsoft.Compute/virtualMachines or
     Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param location: The geo-location where the resource lives.
    :type location: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        location: Optional[str] = None,
        **kwargs
    ):
        super(ProxyResource, self).__init__(location=location, **kwargs)


class ResourceId(msrest.serialization.Model):
    """Generic pointer to a resource.

    :param id: Resource Id.
    :type id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        **kwargs
    ):
        super(ResourceId, self).__init__(**kwargs)
        self.id = id


class ScopeAssignment(Resource):
    """The Managed Network resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. Ex- Microsoft.Compute/virtualMachines or
     Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param location: The geo-location where the resource lives.
    :type location: str
    :ivar provisioning_state: Provisioning state of the ManagedNetwork resource. Possible values
     include: "Updating", "Deleting", "Failed", "Succeeded".
    :vartype provisioning_state: str or ~managed_network_management_client.models.ProvisioningState
    :ivar etag: A unique read-only string that changes whenever the resource is updated.
    :vartype etag: str
    :param assigned_managed_network: The managed network ID with scope will be assigned to.
    :type assigned_managed_network: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'etag': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'etag': {'key': 'properties.etag', 'type': 'str'},
        'assigned_managed_network': {'key': 'properties.assignedManagedNetwork', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        location: Optional[str] = None,
        assigned_managed_network: Optional[str] = None,
        **kwargs
    ):
        super(ScopeAssignment, self).__init__(location=location, **kwargs)
        self.provisioning_state = None
        self.etag = None
        self.assigned_managed_network = assigned_managed_network


class ScopeAssignmentListResult(msrest.serialization.Model):
    """Result of the request to list ScopeAssignment. It contains a list of groups and a URL link to get the next set of results.

    :param value: Gets a page of ScopeAssignment.
    :type value: list[~managed_network_management_client.models.ScopeAssignment]
    :param next_link: Gets the URL to get the next set of results.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ScopeAssignment]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["ScopeAssignment"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(ScopeAssignmentListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class ScopeAssignmentProperties(ResourceProperties):
    """Properties of Managed Network.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar provisioning_state: Provisioning state of the ManagedNetwork resource. Possible values
     include: "Updating", "Deleting", "Failed", "Succeeded".
    :vartype provisioning_state: str or ~managed_network_management_client.models.ProvisioningState
    :ivar etag: A unique read-only string that changes whenever the resource is updated.
    :vartype etag: str
    :param assigned_managed_network: The managed network ID with scope will be assigned to.
    :type assigned_managed_network: str
    """

    _validation = {
        'provisioning_state': {'readonly': True},
        'etag': {'readonly': True},
    }

    _attribute_map = {
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'assigned_managed_network': {'key': 'assignedManagedNetwork', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        assigned_managed_network: Optional[str] = None,
        **kwargs
    ):
        super(ScopeAssignmentProperties, self).__init__(**kwargs)
        self.assigned_managed_network = assigned_managed_network
