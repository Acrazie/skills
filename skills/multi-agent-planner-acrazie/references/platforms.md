# Platform adaptation boundaries

Keep the plan platform-neutral until the execution target is verified. No fixed
spawn command, tool alias or model list is guaranteed by this reference.

## Model selection at execution time

Carry the core's user-validated homogeneous lot boundary and model choice into
adaptation. Before execution, revalidate available models and override support
for the target runtime/account using actual exposed capabilities and current
official documentation. A prompt asking a worker to become a model is not a
runtime selection mechanism. Do not assume an alias or model identifier transfers
between platforms or accounts.

If selection or required context isolation cannot be honored, ask for an explicit
alternative or inheritance decision; never silently substitute or relax reviewer
isolation. An unknown target platform leaves this gate pending, not auto-approved.
Record actual model identity only if reported; otherwise mark it unverified.

## Codex and Claude Code

For either host, verify the actual session's agent capability, concurrent capacity,
model selection, context isolation and workspace/artifact access. Do not infer that
separate chats, background tasks and subagents have interchangeable semantics.
Consult current official documentation before producing concrete host commands.
The planner does not call these mechanisms itself.

## Unknown or unsupported host

Deliver portable fenced prompts with a pending capability/selection gate. If true
parallelism is unavailable, propose an explicitly approved sequential schedule or
single-agent plan. Do not silently substitute execution architecture or claim
parallel verification. Unreachable spec pointers must be replaced with authorized
minimal excerpts or an accessible artifact, never credentials or full raw logs.

## Unchanged boundaries

Scope, contracts, isolation, worker/count/retry limits, verification and separate
action permissions remain in force on every host. A copy-paste prompt is a plan,
not proof that the host enforces these boundaries or authorization to execute it.
