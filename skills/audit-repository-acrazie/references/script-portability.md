# Selected-script portability assessment

Read this guide only for a precise portability question about selected automation
scripts in one repository. It supplements the owner's targeted read-only assessment,
not a separate implementation workflow, security audit or fixed recipe catalogue.
Audit may recommend keeping the current implementation or helper.

## Contract and behavior evidence

Identify exact selected scripts, callers, repository snapshot and approved target
OS/shell/runtime/runner matrix. Inspect relevant instructions, manifests/lockfiles,
actual versions, call sites and existing tests without running unfamiliar scripts.
Trace required inputs/outputs, side effects, working directory, environment precedence,
success/failure exit codes and error propagation. Unknowns remain evidence gaps.
Consult official documentation for the actual target version when changing technical
facts matter; model memory, a latest-version recipe or syntax inspection is not proof.

Compare keeping current helpers with fitting native or already installed capabilities.
Retain a helper unless replacement equivalence is proven across required environments.
Do not introduce Bun or upgrade Node merely to remove a helper. No mandatory polyfill
purge, recursive/force deletion, preferred runtime or universal performance promise.

## Relevant hazards

Inspect only hazards capable of affecting the selected behavior:
- Shell quoting/interpolation, option-like inputs and executable selection. Parameterized
  arguments or template escaping do not validate executable options, paths, permissions
  or downstream actions. Distinguish shell injection from option injection.
- Wildcards, spaces, Unicode, separators and path handling for the actual target tools;
  symlink traversal, bounded deletion and idempotence. Preserve unrelated work/data.
- Environment precedence, caller cwd, subprocess lifecycle, output and failure propagation.
  An in-process shell is not proof of no external child process.

These are correctness/trust boundaries for the selected scripts, not authority for
penetration testing or a repository-wide security assessment. Do not run unfamiliar
scripts or assume a dry-run is non-mutating. Destructive tests, downloads, network,
installation and manifest/lockfile updates require their separate applicable approvals.
Audit does not obtain mutation authority through a trial: preserve the owner's allowed
read-only checks and separately authorized trial boundaries, never integrate changes.

## Proof and executor handoff

Recommend success/error cases and isolated fixtures for required side effects. Record
actual OS, shell, runtime, runner, command, snapshot, inputs, exit results and limits
for authorized checks actually performed. Syntax inspection or emulation is not native
OS execution; an unexecuted target is not verified. Missing required native proof blocks
affected acceptance, not permission to weaken criteria. Propose separately authorized
native verification when unavailable; do not claim Windows success from macOS checks.
Comparable measurements require baseline/workload/environment evidence. Otherwise
performance, subprocess counts and savings are not measured; upstream claims are not
project measurements.

Audit reports recommendations, not completed refactors. Report in chat by default;
only an approved final Audit Record may be written under the owner's exact
content/destination gate. Handoff includes selected paths/snapshot, target matrix, preserved
behavior, options and recommended strategy, tests, side effects/permissions and gaps.
A capable harness executor needs separate realization authorization and records actual
final-snapshot native proof in the implementation contract. Audit remains read-only:
no editing scripts, removing helpers, installation, runtime migration or shipping.
Substantive pipeline changes belong to CI/CD under its own authorization; do not
broaden a selected-script assessment into pipeline execution or deployment.
