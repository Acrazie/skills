# VM / SSH Deployment

This checklist concerns an existing authorized deployment interface, not infrastructure
provisioning or platform administration. Examples are illustrative, not certified
commands: verify current documentation, actual versions and project interfaces
before applying them. Follow the entry skill's contract and separate remote-operation
envelope; artifact promotion, environment authorization and read-back proof remain
required. Jenkins-specific integrations apply only when Jenkins is actually used.


Require an authoritative, version-controlled deployment interface instead of a long inline SSH program.

Verify before generation:

- target host selection, remote principal, and environment mapping;
- CI/runtime SSH credential reference and least-privilege scope;
- exact known-hosts strategy with host-key verification enabled;
- immutable artifact transfer or pull mechanism;
- atomicity or documented interruption state;
- bounded restart and health verification;
- known-good rollback identity and command.

Do not introduce `StrictHostKeyChecking=no`, embed private keys, pass secrets in command arguments, or place deployment logic directly in the pipeline definition. If the interface lives outside the application repository, record its source, owner, immutable version, review boundary, and availability from the CI runner.
