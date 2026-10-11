# AWS Deployment

This checklist concerns an existing authorized deployment interface, not infrastructure
provisioning or platform administration. Examples are illustrative, not certified
commands: verify current documentation, actual versions and project interfaces
before applying them. Follow the entry skill's contract and separate remote-operation
envelope; artifact promotion, environment authorization and read-back proof remain
required. Jenkins-specific integrations apply only when Jenkins is actually used.


Identify the actual target before designing commands: EC2/SSH, ECS, EKS, Lambda, Elastic Beanstalk, S3/CloudFront, or another approved service are not interchangeable.

Verify:

- AWS account, region, service, resource, and environment boundary;
- authoritative deployment interface and immutable artifact identity;
- least-privilege CI/runtime credential reference or approved short-lived workload identity;
- runner-side CLI/integration availability and version;
- service-native deployment status, health signal, timeout, and rollback mechanism;
- read-back that proves the deployed version/digest.

Use current official AWS documentation for the selected service. Workload identity is a provider/platform decision that requires evidence about both AWS and the CI runner environment; do not present it as automatic CI-provider behavior. Never infer an AWS service from a generic Dockerfile.
