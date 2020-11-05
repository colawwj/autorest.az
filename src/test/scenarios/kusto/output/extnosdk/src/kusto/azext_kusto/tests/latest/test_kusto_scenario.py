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
from .example_steps import step__attacheddatabaseconfigurations_put
from .example_steps import step__attacheddatabaseconfigurations_get
from .example_steps import step__attacheddatabaseconfigurations_get2
from .example_steps import step__clusters_put_kustoclusterscreateorupdate
from .example_steps import step__clusters_get_kustoclustersget
from .example_steps import step__clusters_get_kustoclusterslist
from .example_steps import step__clusters_get
from .example_steps import step__clusters_get_kustoclusterslistresourceskus
from .example_steps import step__clusters_get_kustoclusterslistskus
from .example_steps import step__clusters_patch_kustoclustersupdate
from .example_steps import step__clusters_post
from .example_steps import step__clusters_post2
from .example_steps import step__clusters_post3
from .example_steps import step__clusters_post4
from .example_steps import step__clusters_post5
from .example_steps import step__clusters_post6
from .example_steps import step__clusters_post_kustoclustersstart
from .example_steps import step__clusters_post_kustoclustersstop
from .example_steps import step__clusterprincipalassignments_put
from .example_steps import step__clusterprincipalassignments_get
from .example_steps import step__clusterprincipalassignments_get2
from .example_steps import step__databaseprincipalassignments_put
from .example_steps import step__databaseprincipalassignments_get
from .example_steps import step__clusterprincipalassignments_get2
from .example_steps import step__databaseprincipalassignments_delete
from .example_steps import step__databases_put_kustodatabasescreateorupdate
from .example_steps import step__databases_get_kustodatabasesget
from .example_steps import step__databases_get_kustodatabaseslistbycluster
from .example_steps import step__databases_patch_kustodatabasesupdate
from .example_steps import step__databases_post_kustodatabaseaddprincipals
from .example_steps import step__databases_post_kustodatabaselistprincipals
from .example_steps import step__databases_post_kustodatabaseremoveprincipals
from .example_steps import step__databases_delete_kustodatabasesdelete
from .example_steps import step__dataconnections_put
from .example_steps import step__databases_get_kustodatabaseslistbycluster
from .example_steps import step__dataconnections_get_kustodataconnectionsget
from .example_steps import step__dataconnections_patch
from .example_steps import step__dataconnections_post
from .example_steps import step__dataconnections_delete
from .example_steps import step__clusters_delete_kustoclustersdelete
from .example_steps import step__attacheddatabaseconfigurations_delete
from .example_steps import step__clusterprincipalassignments_delete
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
    step__attacheddatabaseconfigurations_put(test, rg, checks=[
        test.check("location", "westus", case_sensitive=False),
        test.check("clusterResourceId", "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Kusto"
                   "/Clusters/{myCluster3}", case_sensitive=False),
        test.check("defaultPrincipalsModificationKind", "Union", case_sensitive=False),
    ])
    step__attacheddatabaseconfigurations_get(test, rg, checks=[
        test.check("location", "westus", case_sensitive=False),
        test.check("defaultPrincipalsModificationKind", "Union", case_sensitive=False),
    ])
    step__attacheddatabaseconfigurations_get2(test, rg, checks=[
        test.check('length(@)', 1),
    ])
    step__clusters_put_kustoclusterscreateorupdate(test, rg, checks=[
        test.check("name", "{myCluster}", case_sensitive=False),
        test.check("identity.type", "SystemAssigned", case_sensitive=False),
        test.check("location", "westus", case_sensitive=False),
        test.check("enableDoubleEncryption", False),
        test.check("enablePurge", True),
        test.check("enableStreamingIngest", True),
        test.check("sku.name", "Standard_L8s", case_sensitive=False),
        test.check("sku.capacity", 2),
        test.check("sku.tier", "Standard", case_sensitive=False),
    ])
    step__clusters_get_kustoclustersget(test, rg, checks=[
        test.check("name", "{myCluster}", case_sensitive=False),
        test.check("identity.type", "SystemAssigned", case_sensitive=False),
        test.check("location", "westus", case_sensitive=False),
        test.check("enableStreamingIngest", True),
        test.check("sku.name", "Standard_L8s", case_sensitive=False),
        test.check("sku.capacity", 2),
        test.check("sku.tier", "Standard", case_sensitive=False),
    ])
    step__clusters_get_kustoclusterslist(test, rg, checks=[
        test.check('length(@)', 1),
    ])
    step__clusters_get(test, rg, checks=[
        test.check('length(@)', 1),
    ])
    step__clusters_get_kustoclusterslistresourceskus(test, rg, checks=[])
    step__clusters_get_kustoclusterslistskus(test, rg, checks=[])
    step__clusters_patch_kustoclustersupdate(test, rg, checks=[
        test.check("name", "{myCluster}", case_sensitive=False),
        test.check("identity.type", "SystemAssigned", case_sensitive=False),
        test.check("location", "westus", case_sensitive=False),
        test.check("enablePurge", True),
        test.check("enableStreamingIngest", True),
        test.check("sku.name", "Standard_L8s", case_sensitive=False),
        test.check("sku.capacity", 2),
        test.check("sku.tier", "Standard", case_sensitive=False),
        test.check("keyVaultProperties.keyName", "keyName", case_sensitive=False),
        test.check("keyVaultProperties.keyVaultUri", "https://dummy.keyvault.com", case_sensitive=False),
        test.check("keyVaultProperties.keyVersion", "keyVersion", case_sensitive=False),
    ])
    step__clusters_post(test, rg, checks=[])
    step__clusters_post2(test, rg, checks=[])
    step__clusters_post3(test, rg, checks=[])
    step__clusters_post4(test, rg, checks=[])
    step__clusters_post5(test, rg, checks=[])
    step__clusters_post6(test, rg, checks=[])
    step__clusters_post_kustoclustersstart(test, rg, checks=[])
    step__clusters_post_kustoclustersstop(test, rg, checks=[])
    step__clusterprincipalassignments_put(test, rg, checks=[])
    step__clusterprincipalassignments_get(test, rg, checks=[])
    step__clusterprincipalassignments_get2(test, rg, checks=[])
    step__databaseprincipalassignments_put(test, rg, checks=[])
    step__databaseprincipalassignments_get(test, rg, checks=[])
    step__clusterprincipalassignments_get2(test, rg, checks=[])
    step__databaseprincipalassignments_delete(test, rg, checks=[])
    step__databases_put_kustodatabasescreateorupdate(test, rg, checks=[])
    step__databases_get_kustodatabasesget(test, rg, checks=[])
    step__databases_get_kustodatabaseslistbycluster(test, rg, checks=[])
    step__databases_patch_kustodatabasesupdate(test, rg, checks=[])
    step__databases_post_kustodatabaseaddprincipals(test, rg, checks=[])
    step__databases_post_kustodatabaselistprincipals(test, rg, checks=[])
    step__databases_post_kustodatabaseremoveprincipals(test, rg, checks=[])
    step__databases_delete_kustodatabasesdelete(test, rg, checks=[])
    step__dataconnections_put(test, rg, checks=[])
    step__databases_get_kustodatabaseslistbycluster(test, rg, checks=[
        test.check('length(@)', 1),
    ])
    step__dataconnections_get_kustodataconnectionsget(test, rg, checks=[
        test.check("location", "westus", case_sensitive=False),
        test.check("consumerGroup", "testConsumerGroup1", case_sensitive=False),
        test.check("eventHubResourceId", "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Even"
                   "tHub/namespaces/eventhubTestns1/eventhubs/eventhubTest1", case_sensitive=False),
    ])
    step__dataconnections_patch(test, rg, checks=[])
    step__dataconnections_post(test, rg, checks=[])
    step__dataconnections_delete(test, rg, checks=[])
    step__clusters_delete_kustoclustersdelete(test, rg, checks=[])
    step__attacheddatabaseconfigurations_delete(test, rg, checks=[])
    step__clusterprincipalassignments_delete(test, rg, checks=[])
    cleanup_scenario(test, rg)


# Test class for ${scenarioName}
@try_manual
class KustoScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='clitestkusto_kustorptest'[:7], key='rg', parameter_name='rg')
    def test_kusto(self, rg):

        self.kwargs.update({
            'subscription_id': self.get_subscription_id()
        })

        self.kwargs.update({
            'myCluster4': 'default',
            'myAttachedDatabaseConfiguration3': 'default',
            'myCluster2': 'leader4',
            'myCluster3': 'KustoClusterLeader',
            'myCluster': 'kustoclusterrptest4',
            'myAttachedDatabaseConfiguration': 'myAttachedDatabaseConfiguration',
            'myAttachedDatabaseConfiguration2': 'attachedDatabaseConfigurations1',
            'myDataConnection': 'DataConnections8',
            'myDataConnection2': 'kustoeventhubconnection1',
        })

        call_scenario(self, rg)
        calc_coverage(__file__)
        raise_if()

