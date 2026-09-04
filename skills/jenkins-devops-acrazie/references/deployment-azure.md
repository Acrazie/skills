# Azure Deployment

Identify the actual target before designing commands: VM, AKS, App Service, Container Apps, Functions, Storage/CDN, or another approved service.

Verify:

- tenant, subscription, region, resource, and environment boundary;
- authoritative deployment interface and immutable artifact identity;
- least-privilege Jenkins credential ID, service principal, or approved workload identity;
- agent-side CLI/plugin availability and version;
- service-native status, health verification, timeout, and rollback mechanism;
- read-back that proves the deployed version/digest.

Use current official Azure documentation for the selected service. Workload identity is a provider/platform decision requiring environment evidence. Never write tenant credentials, client secrets, or certificates into the pipeline or SCM.
