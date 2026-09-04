# Google Cloud Deployment

Identify the actual target before designing commands: Compute Engine, GKE, Cloud Run, Functions, App Engine, Storage/CDN, or another approved service.

Verify:

- project, region, service/resource, and environment boundary;
- authoritative deployment interface and immutable artifact identity;
- least-privilege Jenkins credential ID or approved workload identity federation;
- agent-side CLI/plugin availability and version;
- service-native status, health verification, timeout, and rollback mechanism;
- read-back that proves the deployed version/digest.

Use current official Google Cloud documentation for the selected service. Workload identity federation is a provider/platform decision requiring environment evidence. Do not embed service-account keys or rely on an interactive human login flow.
