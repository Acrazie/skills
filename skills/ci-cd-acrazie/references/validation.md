# Validation and Causal Evidence

Use distinct proof layers. None automatically implies the next:
1. Provenance: actual project commands/interfaces, versions, inputs, expected outputs,
   artifact identity, runner/authentication requirements.
2. Approved local checks: syntax, formatter, lint, tests and scripts using project
   configuration. No installation, downloads or destructive dry-run without permission.
3. Provider-aware structural/model validation using the actual supported interface.
   YAML parsing is not a workflow schema check; Groovy parsing is not Jenkins DSL/CPS.
4. Independently authorized CI run of the identified source with verified run outcome.
5. Published artifact identity/provenance verified at the destination.
6. Authorized target deployment and health/release read-back; rollback unexercised
   remains unverified even if pipeline contains a rollback stage.

Record snapshot, command, environment/tool, exit/result and limits at each reached
layer. Checks invalidated by later edits must rerun for affected behavior. Independent
review when required or accepted needs exact-snapshot ACCEPT and fresh context;
REJECT/INCOMPLETE/unavailable review blocks dependent acceptance.

For diagnosis, preserve sanitized failing-stage context, first causal error, revision,
runner/workspace, artifact and capabilities. Separate deterministic errors from
transient faults. Do not weaken checks, swallow errors or claim a retry fixed cause.
An inaccessible required service/tool is blocked, not verified. Never log secrets.
