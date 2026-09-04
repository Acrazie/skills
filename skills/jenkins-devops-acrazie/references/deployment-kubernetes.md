# Kubernetes Deployment

Detect the authoritative version-controlled deployment model: raw manifests, Helm, Kustomize, GitOps, or another approved interface. Do not mix models or generate an unrequested migration.

Verify before generation:

- cluster/context and namespace per environment;
- Jenkins credential ID or approved workload identity, RBAC, and trust boundary;
- immutable image digest/version consumed by the deployment model;
- render, schema, dry-run, or server-side validation supported by that model;
- bounded rollout status and deployed-revision verification;
- rollback through a known-good release, manifest revision, or image identity;
- availability and versions of required CLIs on the selected agent.

Do not assume the Jenkins Kubernetes plugin is needed. Provisioning Jenkins agents as pods is separate from deploying an application with `kubectl`, Helm, Kustomize, or GitOps.

References:

- Jenkins Kubernetes plugin: https://plugins.jenkins.io/kubernetes/
- kubectl rollout status: https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_status/
- kubectl apply: https://kubernetes.io/docs/reference/kubectl/generated/kubectl_apply/
