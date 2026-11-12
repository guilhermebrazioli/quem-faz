# __generated__ by Terraform
# Please review these resources and move them into your main configuration files.

# __generated__ by Terraform from "/subscriptions/ee814bcb-a5d8-479a-bb7f-415353458729/resourceGroups/rg-quem-faz"
resource "azurerm_resource_group" "main" {
  location   = "eastus"
  managed_by = null
  name       = "rg-quem-faz"
  tags       = {}
}
resource "azurerm_log_analytics_workspace" "main" {
  allow_resource_only_permissions         = true
  cmk_for_query_forced                    = false
  daily_quota_gb                          = -1
  data_collection_rule_id                 = null
  immediate_data_purge_on_30_days_enabled = false
  internet_ingestion_access_type          = "Enabled"
  internet_query_access_type              = "Enabled"
  local_authentication_enabled            = null
  location                                = "eastus"
  name                                    = "workspace-rgquemfazArrv"
  reservation_capacity_in_gb_per_day      = null
  resource_group_name                     = "rg-quem-faz"
  retention_in_days                       = 30
  sku                                     = "PerGB2018"
  tags                                    = {}

  lifecycle {
    ignore_changes = [local_authentication_enabled]
  }
}


# __generated__ by Terraform
resource "azurerm_container_app" "main" {
  container_app_environment_id = "/subscriptions/ee814bcb-a5d8-479a-bb7f-415353458729/resourceGroups/rg-quem-faz/providers/Microsoft.App/managedEnvironments/env-quem-faz"
  max_inactive_revisions       = 100
  name                         = "quem-faz"
  resource_group_name          = "rg-quem-faz"
  revision_mode                = "Multiple"
  tags                         = {}
  workload_profile_name        = "Consumption"

  ingress {
    allow_insecure_connections = false
    client_certificate_mode    = null
    external_enabled           = true
    session_affinity_enabled   = false
    target_port                = 8000
    transport                  = "auto"

    traffic_weight {
      label           = null
      latest_revision = true
      percentage      = 100
      revision_suffix = null
    }
  }

  template {
    cooldown_period_in_seconds       = 300
    max_replicas                     = 1
    min_replicas                     = 0
    polling_interval_in_seconds      = 30
    termination_grace_period_seconds = 0

    container {
      args    = []
      command = []
      cpu     = 0.25
      image   = "docker.io/guibrazioli/quem-faz:v1"
      memory  = "0.5Gi"
      name    = "quem-faz"
    }
  }
}

# __generated__ by Terraform
resource "azurerm_container_app_environment" "main" {
  dapr_application_insights_connection_string = null # sensitive
  infrastructure_resource_group_name          = null
  infrastructure_subnet_id                    = null
  location                                    = "eastus"
  log_analytics_workspace_id                  = "/subscriptions/ee814bcb-a5d8-479a-bb7f-415353458729/resourceGroups/rg-quem-faz/providers/Microsoft.OperationalInsights/workspaces/workspace-rgquemfazArrv"
  logs_destination                            = "log-analytics"
  mutual_tls_enabled                          = false
  name                                        = "env-quem-faz"
  public_network_access                       = "Enabled"
  resource_group_name                         = "rg-quem-faz"
  tags                                        = {}

  workload_profile {
    maximum_count         = 0
    minimum_count         = 0
    name                  = "Consumption"
    workload_profile_type = "Consumption"
  }
}
