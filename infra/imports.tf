import {
  to = azurerm_resource_group.main
  id = "/subscriptions/ee814bcb-a5d8-479a-bb7f-415353458729/resourceGroups/rg-quem-faz"
}

import {
  to = azurerm_log_analytics_workspace.main
  id = "/subscriptions/ee814bcb-a5d8-479a-bb7f-415353458729/resourceGroups/rg-quem-faz/providers/Microsoft.OperationalInsights/workspaces/workspace-rgquemfazArrv"
}

import {
  to = azurerm_container_app_environment.main
  id = "/subscriptions/ee814bcb-a5d8-479a-bb7f-415353458729/resourceGroups/rg-quem-faz/providers/Microsoft.App/managedEnvironments/env-quem-faz"
}

import {
  to = azurerm_container_app.main
  id = "/subscriptions/ee814bcb-a5d8-479a-bb7f-415353458729/resourceGroups/rg-quem-faz/providers/Microsoft.App/containerApps/quem-faz"
}
