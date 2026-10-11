# Azure Deployment

This checklist concerns an existing authorized deployment interface, not infrastructure
provisioning or platform administration. Examples are illustrative, not certified
commands: verify current documentation, actual versions and project interfaces
before applying them. Follow the entry skill's contract and separate remote-operation
envelope; artifact promotion, environment authorization and read-back proof remain
required. Jenkins-specific integrations apply only when Jenkins is actually used.


Identify the actual target before designing commands: VM, AKS, App Service, Container Apps, Functions, Storage/CDN, or another approved service.

Verify:

- tenant, subscription, region, resource, and environment boundary;
- authoritative deployment interface and immutable artifact identity;
- least-privilege CI/runtime credential reference, service principal, or approved workload identity;
- runner-side CLI/integration availability and version;
- service-native status, health verification, timeout, and rollback mechanism;
- read-back that proves the deployed version/digest.

Use current official Azure documentation for the selected service. Workload identity is a provider/platform decision requiring environment evidence. Never write tenant credentials, client secrets, or certificates into the pipeline or SCM.
