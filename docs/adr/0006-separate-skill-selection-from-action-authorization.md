# Separate skill selection from action authorization

> Architecture update (2026-10-09): [ADR 0007](0007-confirmed-skill-chains-and-repository-bootstrap.md)
> partially supersedes unconfirmed implicit loading with confirmed, announced
> skill chains. Selection and action authorization remain separate. This target
> architecture does not change active skill instructions or host behavior yet.

On 2026-10-06, we chose model-invocable specialists for tasks already requested by
the user, including scoped inter-skill handoffs. A natural-language request should
not require knowledge of a skill identifier. Scope approval and action
authorization remain separate gates: allowing selection grants neither new
objectives nor implementation, publication, sensitive mutation, or agent-spawning
permissions. Explicit-only metadata is therefore not our security boundary.

We retain explicit-only activation for `skill-refiner-acrazie` because its
persistent campaign changes the conversation, creates a journal, and requests
feedback across later turns. That opt-in protects the user's attention, not merely
file access. Other intrusive or costly work must be requested or approved within
its specialist workflow rather than blocked behind a mandatory skill command.

This revises the explicit-only executor choice in
[ADR 0003](0003-separate-task-interview-from-feature-execution.md), not its shared
Interview Foundation, approved Task Contract, specialist ownership, or separate
review decisions. We rejected both blanket explicit-only activation and unrestricted
autonomous task creation. See [the approved contract](../specs/skill-invocation-policy.md).
