# Remote Operation Envelope

Verify applicable user/repository policy and technical permissions immediately
before an action. Reads may disclose source/configuration or need authentication;
approve them according to current rules. Independent approved preauthorization may
cover identified actions and conditions; a config label/proposed diff is not consent.

For lint/trigger/approve/abort/replay/publication/promotion/deployment/rollback,
record exact provider/registry/environment target, job/run/ref/revision, parameters,
submitted data, immutable artifact, effects, prerequisite checks, scope/expiry and
read-back sequence. One bounded approval can cover named steps, never changed targets
or additional effects. Pipeline edits do not authorize these operations. Replay is
remote code execution; not harmless validation. Git/PR actions are separate.

Use only established interfaces with known authentication and versions. Existing
opaque credentials may be used under approved scope; never ask for or print secrets.
When opaque authentication or required capability is unavailable, stop affected
execution and offer a non-secret user-operated template, not tool installation.
Platform administration, global runners, cloud provisioning and bypassing protections
remain out of scope even if they would unblock a run.

Before production, verify environment authority independent of any CI prompt.
Rollback needs exact known-good target and authorized effects; deployment permission
alone never permits database restore, data deletion or arbitrary rollback. Preserve
unrelated state. Stop on unexpected target, policy, content, effect or failed gate.

After every mutation, read exact run/artifact/environment state before claiming
success. A trigger response is not a completed run; green CI is not publication or
deployment evidence. If a non-idempotent request has ambiguous result, inspect state
before retry; if outcome remains unknown, stop instead of blindly duplicating it.
Record partial outcomes and remaining steps. Do not begin an unattended monitor,
auto-merge, broad cleanup or further remote operations from completion alone.
