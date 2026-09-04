# VM / SSH Deployment

Require an authoritative, version-controlled deployment interface instead of a long inline SSH program.

Verify before generation:

- target host selection, remote principal, and environment mapping;
- Jenkins SSH credential ID and least-privilege scope;
- exact known-hosts strategy with host-key verification enabled;
- immutable artifact transfer or pull mechanism;
- atomicity or documented interruption state;
- bounded restart and health verification;
- known-good rollback identity and command.

Do not introduce `StrictHostKeyChecking=no`, embed private keys, pass secrets in command arguments, or place remote shell logic directly in Groovy. If the interface lives outside the application repository, record its source, owner, immutable version, review boundary, and availability from the Jenkins agent.
