## CLI

These settings apply only when `--cli` is specified on the command line.

``` yaml $(cli)
cli:
  test-scenario:
    - name: Create or update a workspace
    - name: Create or update a Big Data pool
    - name: List Big Data pools in a workspace
    - name: Update a Big Data pool
    - name: Create integration runtime
    - name: Get integration runtime
    - name: List integration runtimes
    - name: Start integration runtime
    - name: Stop integration runtime
    - name: Upgrade integration runtime
    - name: Update integration runtime
    - name: List auth keys
    - name: Regenerate auth key
    - name: Get connection info
    - name: Sync credentials
    - name: Get monitoring data
    - name: Get integration runtime node IP address
    - name: Get integration runtime node
    - name: Update integration runtime node
    - name: Get integration runtime object metadata
    - name: Refresh object metadata
    - name: Get status
    - name: Create an IP firewall rule
    - name: Create an IP firewall rule
    - name: List IP firewall rules in a workspace
    - name: Replace all IP firewall rules in a workspace
    - name: Get azure async operation header result
    - name: Get location header result
    - name: Approve private endpoint connection
    - name: Get private endpoint connection
    - name: List private endpoint connections in workspace
    - name: Create or update a privateLinkHub
    - name: Get a privateLinkHub
    - name: List privateLinkHubs in resource group
    - name: List privateLinkHubs in subscription
    - name: Update a privateLinkHub
    - name: Get a Big Data pool
    - name: Get a workspace
    - name: List workspaces in resource group
    - name: List workspaces in subscription
    - name: Update a workspace
    - name: Get private link resources for workspace
    - name: Get private link resources for workspace
    - name: Create a SQL Analytics pool
    - name: Get a SQL Analytics pool
    - name: List SQL Analytics pools in a workspace
    - name: List SQL Analytics pools in a workspace with filter
    - name: Pause a SQL Analytics pool
    - name: Rename a SQL Analytics pool
    - name: Resume a SQL Analytics pool
    - name: Update a SQL Analytics pool
    - name: Create or update a database's blob auditing policy with all parameters
    - name: Create or update a database's blob auditing policy with minimal parameters
    - name: Get blob auditing policy of a SQL Analytics pool
    - name: Get a connection policy of a SQL Analytics pool
    - name: Get a SQL Analytics pool user activity
    - name: Get Sql pool geo backup policy
    - name: Set metadata sync config for a SQL Analytics pool
    - name: Get metadata sync config for a SQL Analytics pool
    - name: Get the result of an operation on a SQL Analytics pool
    - name: List the Sql Analytics pool management operations
    - name: Lists a Sql Analytic pool's replication links
    - name: Get a list of restore points of a SQL Analytics pool
    - name: Creates Sql pool restore point.
    - name: List the schema in a SQL Analytics pool
    - name: Update a Sql pool's threat detection policy with all parameters
    - name: Update a Sql pool's threat detection policy with minimal parameters
    - name: Get a security alert of a SQL Analytics pool
    - name: Updates the sensitivity label of a given column with all parameters
    - name: Gets the current sensitivity labels of a given SQL Analytics pool
    - name: Gets the recommended sensitivity labels of a given SQL Analytics pool
    - name: Disables sensitivity recommendations on a given column
    - name: Enables sensitivity recommendations on a given column
    - name: List the columns in a table of a given schema in a SQL Analytics pool
    - name: List the tables of a given schema in a SQL Analytics pool
    - name: Create or update a Sql pool's transparent data encryption configuration
    - name: Get transparent data encryption configuration of a SQL Analytics pool
    - name: List the usages of a SQL Analytics pool
    - name: Creates or updates a database's vulnerability assessment rule baseline.
    - name: Get a vulnerability scan record of a SQL Analytics pool
    - name: Executes a Sql pool's vulnerability assessment scan.
    - name: Export a database's vulnerability assessment scan results.
    - name: Create a database's vulnerability assessment with all parameters
    - name: Create a database's vulnerability assessment with minimal parameters, when storageAccountAccessKey is specified
    - name: Create a database's vulnerability assessment with minimal parameters, when storageContainerSasKey is specified
    - name: Get a Sql pool's vulnerability assessment
    - name: Get a vulnerability assessment of a SQL Analytics pool
    - name: Deletes the sensitivity label of a given column
    - name: Create or update workspace active directory admin
    - name: Get workspace active directory admin
    - name: Create or update managed identity sql control settings
    - name: Get managed identity sql control settings
    - name: Delete a Big Data pool
    - name: Delete integration runtime node
    - name: Delete integration runtime
    - name: Delete an IP firewall rule from a workspace
    - name: Delete private endpoint connection
    - name: Removes a database's vulnerability assessment rule baseline.
    - name: Delete a privateLinkHub
    - name: Remove a database's vulnerability assessment
    - name: Delete a SQL Analytics pool
    - name: Delete workspace active directory admin
    - name: Delete a workspace
