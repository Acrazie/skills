# AWS Deployment

Identify the actual target before designing commands: EC2/SSH, ECS, EKS, Lambda, Elastic Beanstalk, S3/CloudFront, or another approved service are not interchangeable.

Verify:

- AWS account, region, service, resource, and environment boundary;
- authoritative deployment interface and immutable artifact identity;
- least-privilege Jenkins credential ID or approved short-lived workload identity;
- agent-side CLI/plugin availability and version;
- service-native deployment status, health signal, timeout, and rollback mechanism;
- read-back that proves the deployed version/digest.

Use current official AWS documentation for the selected service. Workload identity is a provider/platform decision that requires evidence about both AWS and the Jenkins agent environment; do not present it as Jenkins behavior. Never infer an AWS service from a generic Dockerfile.
