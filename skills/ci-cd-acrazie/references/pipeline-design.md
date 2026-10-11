# Pipeline Design

Choose only stages and controls required by the approved capability boundary.
Keep build/test/deploy logic in authoritative, independently testable project
interfaces; the provider definition coordinates triggers, runners, ordering,
identity, trust and evidence. Preserve established syntax/provider unless migration
is explicitly approved. See jenkins.md only for actual Jenkins work.

Separate untrusted contribution validation from credential-bearing release jobs.
Trust includes called scripts and dependencies, not only the pipeline file.
Define least-privilege credential references, protected source revision and event
semantics using current provider docs; do not expose values. Cache keys include
relevant lockfile/runtime/configuration inputs; caches are not release artifacts
or a boundary for secrets. Do not reuse writable caches across trust domains.

Build once; publish with immutable identity and provenance, then promote the same
identity across requested environments. Prevent overwrite/racing publication and
older builds deploying after newer ones. Account for timeouts, retention, reporting,
cleanup, concurrency and retry according to project evidence/approved choices,
not arbitrary numeric defaults. Cleanup must preserve unrelated workspace content
and primary failure. A production prompt does not replace environment permission.

Use verified runner capabilities and workspace isolation. Never assume containers
or Docker sockets isolate untrusted code. Unknown runtime/version/permission facts
block dependent runnable stages. No plugin, global runner or cloud provisioning.
