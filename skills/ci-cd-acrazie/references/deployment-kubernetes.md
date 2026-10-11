# Kubernetes Deployment

This checklist concerns an existing authorized deployment interface, not infrastructure
provisioning or platform administration. Examples are illustrative, not certified
commands: verify current documentation, actual versions and project interfaces
before applying them. Follow the entry skill's contract and separate remote-operation
envelope; artifact promotion, environment authorization and read-back proof remain
required. Jenkins-specific integrations apply only when Jenkins is actually used.


Detect the authoritative version-controlled deployment model: raw manifests, Helm, Kustomize, GitOps, or another approved interface. Do not mix models or generate an unrequested migration.

Verify before generation:

- cluster/context and namespace per environment;
- CI/runtime credential reference or approved workload identity, RBAC, and trust boundary;
- immutable image digest/version consumed by the deployment model;
- render, schema, dry-run, or server-side validation supported by that model;
- bounded rollout status and deployed-revision verification;
- rollback through a known-good release, manifest revision, or image identity;
- availability and versions of required CLIs on the selected agent.

Do not assume the Jenkins Kubernetes plugin is needed. Provisioning CI runners as pods is separate from deploying an application with `kubectl`, Helm, Kustomize, or GitOps.

References:

- Jenkins Kubernetes plugin: https://plugins.jenkins.io/kubernetes/
- kubectl rollout status: https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_status/
- kubectl apply: https://kubernetes.io/docs/reference/kubectl/generated/kubectl_apply/
