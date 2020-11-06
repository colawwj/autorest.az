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
from .example_steps import step_create
from .example_steps import step_list
from .example_steps import step_show
from .example_steps import step_list
from .example_steps import step_regenerate_key
from .example_steps import step_regenerate_key
from .example_steps import step_update
from .example_steps import step_delete
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
    step_create(test, rg, checks=[])
    # STEP NOT FOUND: Get remote rendering account key
    # STEP NOT FOUND: Get spatial anchor account key
    # STEP NOT FOUND: List spatial anchor accounts by resource group
    step_list(test, rg, checks=[])
    # STEP NOT FOUND: Get spatial anchors account
    step_show(test, rg, checks=[])
    step_list(test, rg, checks=[])
    # STEP NOT FOUND: List spatial anchors accounts by subscription
    # STEP NOT FOUND: List available operations
    step_regenerate_key(test, rg, checks=[])
    step_regenerate_key(test, rg, checks=[])
    step_update(test, rg, checks=[])
    # STEP NOT FOUND: Update spatial anchors account
    # STEP NOT FOUND: CheckLocalNameAvailability
    # STEP NOT FOUND: Delete spatial anchors account
    step_delete(test, rg, checks=[])
    cleanup_scenario(test, rg)


# Test class for Scenario
@try_manual
class Mixed_realityScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='clitestmixed_reality_MyResourceGroup'[:7], key='rg', parameter_name='rg')
    def test_mixed_reality_Scenario(self, rg):

        call_scenario(self, rg)
        calc_coverage(__file__)
        raise_if()

