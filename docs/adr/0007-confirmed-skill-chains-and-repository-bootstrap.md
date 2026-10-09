# Confirm skill chains and keep repository bootstrap under one owner

> Revision (2026-10-09): [ADR 0008](0008-explicit-project-kits-and-policy-preauthorization.md)
> supersedes the single-confirmation chain mechanism with explicit invocation for
> every skill in activated project kits, following host-documentation discovery.
> The original decision and its ownership rationale remain below for provenance.

On 2026-10-09, the user approved specialist-first software engineering workflows
with confirmation before implicit skill loading. One confirmation covers the
announced chain, including conditional dependencies; an unannounced skill requires
another confirmation. Explicitly naming a skill confirms that skill only. This
partially supersedes [ADR 0006](0006-separate-skill-selection-from-action-authorization.md):
natural-language discovery remains useful, but no longer suffices for unconfirmed
loading. Selection, scope approval and action authorization remain distinct.

We retain the ownership boundary of
[ADR 0003](0003-separate-task-interview-from-feature-execution.md). Interview
documents and stops; an approved contract can explicitly authorize the specialist
to resume scoped realization. Reuse settled decisions rather than require a
universal interview or duplicate specialist interviews. Executors own their tests;
mandatory dependencies have verifiable gates rather than advisory references.

Repository activation belongs to the existing Repo Init owner, through a future
engineering activation mode for populated repositories, not another configuration
skill or a new CLI product. It proposes an adaptable kit, installs the approved
selection locally, preserves existing agent instructions, and records approved
configuration and identified versions for explicit updates and reapplication.
Repository policy independently specifies forbidden, confirmation-required or
conditionally preauthorized actions; no skill can grant itself permission.

We reject unrestricted implicit loading, a universal development orchestrator,
duplicated configuration ownership and automatic installation or updates. These
alternatives either weaken user control or increase lifecycle complexity without
a demonstrated need. A priority for relevant Acrazie skills is not exclusivity.
Readable repository policy must remain usable without installed skills.

This is an accepted target architecture, not a change to active instructions,
metadata or runtime. Existing gates remain effective until separately approved
implementation harmonizes them. In particular, confirmation before loading must
be established upstream and verified per host; a rule inside an already loaded
skill cannot provide that guarantee. Exact installation/configuration mechanisms
are deferred to implementation discovery. See the
[approved architecture contract](../specs/software-engineering-skill-architecture.md).
