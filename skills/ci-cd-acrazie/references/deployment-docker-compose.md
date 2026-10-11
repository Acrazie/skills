# Docker / Compose Deployment

This checklist concerns an existing authorized deployment interface, not infrastructure
provisioning or platform administration. Examples are illustrative, not certified
commands: verify current documentation, actual versions and project interfaces
before applying them. Follow the entry skill's contract and separate remote-operation
envelope; artifact promotion, environment authorization and read-back proof remain
required. Jenkins-specific integrations apply only when Jenkins is actually used.


Distinguish build-time container use from deployment. A Dockerfile does not prove that CI runners have Docker access or that Compose is the deployment mechanism.

Verify before generation:

- the image is published under a non-overwritable digest or version;
- registry authentication uses a least-privilege credential ID;
- Compose or the deployment interface consumes the approved immutable image;
- environment configuration and secrets remain outside the image and SCM;
- pull, rollout, health verification, and rollback commands are authoritative;
- Docker Pipeline syntax is used only when the Docker Pipeline plugin and compatible version are known.

Avoid privileged Docker-in-Docker. Treat access to the host Docker socket as host-equivalent privilege, not container isolation, and require an explicit security decision before using it.

Official Jenkins reference: https://www.jenkins.io/doc/book/pipeline/docker/
