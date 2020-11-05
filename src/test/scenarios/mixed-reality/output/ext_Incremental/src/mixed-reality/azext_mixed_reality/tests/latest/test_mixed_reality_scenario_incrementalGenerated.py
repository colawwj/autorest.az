# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import os
from azure.cli.testsdk import ScenarioTest
from azure.cli.testsdk import ResourceGroupPreparer
from .example_steps import step_create_remote_rendering_account
from .example_steps import step_list_remote_rendering
from .example_steps import step_get_remote_rendering_account
from .example_steps import step_list_remote_rendering2
from .example_steps import step_regenerate_remote_rendering_account_keys
from .example_steps import step_regenerate_spatial_anchors_account_keys
from .example_steps import step_update_remote_rendering_account
from .example_steps import step_delete_remote_rendering_account
from .. import (
    try_manual,
    raise_if,
    calc_coverage
)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


# Env setup_scenario
@try_manual
def setup_scenario(test, rg):
    pass


# Env cleanup_scenario
@try_manual
def cleanup_scenario(test, rg):
    pass


# Testcase: Scenario
@try_manual
def call_scenario(test, rg):
    setup_scenario(test, rg)
    # STEP NOT FOUND: Create spatial anchor account
    step_create_remote_rendering_account(test, rg, checks=[])
    # STEP NOT FOUND: Get remote rendering account key
    # STEP NOT FOUND: Get spatial anchor account key
    # STEP NOT FOUND: List spatial anchor accounts by resource group
    step_list_remote_rendering(test, rg, checks=[])
    # STEP NOT FOUND: Get spatial anchors account
    step_get_remote_rendering_account(test, rg, checks=[])
    step_list_remote_rendering2(test, rg, checks=[])
    # STEP NOT FOUND: List spatial anchors accounts by subscription
    # STEP NOT FOUND: List available operations
    step_regenerate_remote_rendering_account_keys(test, rg, checks=[])
    step_regenerate_spatial_anchors_account_keys(test, rg, checks=[])
    step_update_remote_rendering_account(test, rg, checks=[])
    # STEP NOT FOUND: Update spatial anchors account
    # STEP NOT FOUND: CheckLocalNameAvailability
    # STEP NOT FOUND: Delete spatial anchors account
    step_delete_remote_rendering_account(test, rg, checks=[])
    cleanup_scenario(test, rg)


# Test class for ${scenarioName}
@try_manual
class Mixed_realityScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='clitestmixed_reality_MyResourceGroup'[:7], key='rg', parameter_name='rg')
    def test_mixed_reality(self, rg):

        call_scenario(self, rg)
        calc_coverage(__file__)
        raise_if()

