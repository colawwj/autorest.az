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
# pylint: disable=too-many-statements

from azure.cli.core.commands.parameters import (
    tags_type,
    resource_group_name_type,
    get_location_type
)
from azure.cli.core.commands.validators import get_default_location_from_resource_group
from azext_attestation.action import AddPolicySigningCertificatesKeys


def load_arguments(self, _):

    with self.argument_context('attestation create-provider') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('provider_name', type=str, help='Name of the attestation service')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), required=False,
                   validator=get_default_location_from_resource_group)
        c.argument('tags', tags_type)
        c.argument('attestation_policy', type=str, help='Name of attestation policy.')
        c.argument('policy_signing_certificates_keys', action=AddPolicySigningCertificatesKeys, nargs='+', help='The '
                   'value of the "keys" parameter is an array of JWK values.  By default, the order of the JWK values '
                   'within the array does not imply an order of preference among them, although applications of JWK '
                   'Sets can choose to assign a meaning to the order for their purposes, if desired.')

    with self.argument_context('attestation attestation-provider provider list') as c:
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('attestation attestation-provider show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('provider_name', type=str, help='Name of the attestation service instance', id_part='name')

    with self.argument_context('attestation attestation-provider update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('provider_name', type=str, help='Name of the attestation service', id_part='name')
        c.argument('tags', tags_type)

    with self.argument_context('attestation attestation-provider delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('provider_name', type=str, help='Name of the attestation service', id_part='name')
