---
name: diagnostic-queue-runner-acrazie
description: >-
  Ingest, partition, and systematically resolve mass compiler and linter diagnostic queues
  through bottom-up topological module ordering, isolated worker guardrails, and closed
  adversarial verification. Use when resolving hundreds or thousands of static analysis,
  type-checker, or compiler errors across large refactors, framework migrations, or cross-language ports.
  Not for single-line debugging or running uncoordinated workspace builds.
---

# Diagnostic Queue Runner / Acrazie

Resolve a selected mass diagnostic backlog through bounded batches, observed
dependency ordering and independent verification. Do not turn a backlog request
into an architectural rewrite or an automatic Git delivery workflow.

## Project loading boundary

Published-library defaults remain model-invocable within the requested task. An
explicit project kit or stricter current instruction takes precedence: propose
this skill from available metadata and wait for the user's explicit command before
reading its instructions. Apply the same gate to each dependency before reading
or dispatching its instructions. Use `$skill-name` in Codex or `/skill-name` in
Claude Code. One invocation does not activate a chain; do not read or delegate
an unactivated skill as a bypass. Each re-review of a new snapshot requires a new
reviewer activation in an explicit kit, and returning to the implementer requires
its explicit activation. Ordinary library defaults retain scoped implicit handoffs.
These gates are not filesystem access controls or proof of live host behavior;
unresolved global homonyms may block a strict gate claim.

Loading grants no writing, execution, installation, network, spawning, staging or
shipping permission. An unavailable mandatory dependency blocks only its dependent
step; never imitate it or silently install a substitute. In a managed kit, propose
Repo Init's separately approved project update and pinned selection after its own
activation, not copied or unpinned substitutes.

## User decision format

For user-owned choices, display only Current state, numbered Options,
Recommendation and Response. Translate labels/content into the user's language;
do not add question IDs, preselect an answer as consent or treat a recommendation
as approval. Ask only unresolved decisions, not a fixed survey. Reports and
verification records retain their own structures.

## Contract and permissions

Start with read-only discovery of instructions, repository state, selected paths,
existing tests and relevant tools. Do not execute unfamiliar commands for discovery.
Reuse a current applicable Task Contract or agreement with independently evidenced
approval, not a status label. It must cover outcome, paths, preserved behavior,
checks, acceptance gates and allowed actions. Reopen only materially invalidated
user decisions through bounded clarification; no new mandatory Interview dependency
or duplicate contract for ceremony. Obtain explicit scoped realization approval
before editing, unless a current applicable agreement already covers it.

Approve artifact content/destinations and write scope before creating specifications,
backlogs or reports; preserve existing files and unrelated work. Execution may have
filesystem, network or destructive effects: inspect commands and obtain applicable
permission. Installation, lockfile changes, credentials, network and destructive
fixtures are separate permissions, not consequences of an approved plan. No implicit
staging, commit, push, PR, merge or deployment. Follow applicable repository action
policy for any separately authorized delivery; never bypass hooks or protections.

## Independent verification gate

Every affected unit/fix needs `adversarial-reviewer-acrazie` evidence before it is
accepted. A review may cover a coherent batch only if it explicitly covers every
changed unit/fix; omission is not acceptance. Provide base and exact candidate
snapshot, authoritative contract, scoped diff and relevant read-only technical
context to a fresh agent context without inherited author conversation, or a
separate manual reviewer context. Never substitute implementer self-review.
Validate required spawning permissions and the separate reviewer model lot first.
If isolation or the activated reviewer is unavailable, report review as blocked.

Require `ACCEPT` for that exact snapshot. `REJECT` or `INCOMPLETE` blocks affected
acceptance/progression; missing review is not `ACCEPT`. Corrections invalidate
review of affected content and require fresh verification before proceeding. The
reviewer reports demonstrated introduced violations without implementing fixes;
empty returns, comments, test doubles or low-level operations are not defects by
syntax alone. Review and passing checks reduce risk, not guarantee zero defects.

## Subagent model selection

Apply this gate only when the workflow calls for an authorized subagent; loading a
skill in the current context is not a spawn. A planner carries the gate into its
generated workflow without executing it.

1. Verify available models and explicit model-selection support in the current
   runtime/account, using exposed tools/configuration and current official
   documentation when needed. Do not infer availability from a provider's catalog.
2. Propose 2–3 verified options in the user's language, with exactly one recommended option
   justified by the lot's work, complexity, risk, and required capabilities. Compare
   cost, capacity, and latency only where supported by evidence; disclose unknowns.
   Prefer an economical model when sufficient; never apply a fixed two-tier downgrade
   or equate generation, price, and capability. If fewer options are verified, show only those.
   If no selectable option can be verified, ask rather than inventing a recommendation.
3. Wait for explicit user validation before spawning. A homogeneous lot comprises
   agents with the same role, bounded mission/scope, risk level, and selected model.
   State that boundary and the proposed agent count. Validation covers that lot,
   including already-scoped retries, not unrelated later work. Request new validation
   if the role, mission/scope, risk level, or model changes.
4. If the chosen model is unavailable or model selection is unsupported or unverifiable, stop and ask
   whether to use a verified alternative, explicitly accept inheritance, or use a
   permitted non-spawn path. Never silently inherit, substitute, or claim an override.
5. Model validation does not authorize delegation or waive contracts, permissions,
   tests, worker limits, or fresh-context reviewer isolation. Pass only the approved
   model through the runtime's supported mechanism; preserve required context isolation.
   Record the lot, options/recommendation, user choice, and actual model if the runtime reports it
   in the existing task/workflow evidence. If actual model identity is not reported,
   record it as unverified rather than claiming the requested model ran.
   If the runtime reports a different model, stop the lot and ask before further delegation.


## Queue and worker invariants

- Ingest once per snapshot/checkpoint, not once forever. Record tool/version,
  configuration, command, environment, snapshot, exit status, raw output and parse
  coverage. Revalidate diagnostics after affected changes and between approved batches/checkpoints; never
  dispatch stale diagnostics as current failures. A lower count alone is not proof
  of correction when checks, inputs or configuration changed.
- Select worker checks by required coverage, actual tooling, cost and isolation.
  Prefer approved scoped checks preserving project configuration; a guessed
  single-file compiler command is not proof of a module build. Whole-project checks
  may be necessary when no valid scoped check exists, but require an explicitly
  approved schedule, execution owner and isolated/serialized shared build effects.
  Coordinator performs approved checkpoint and final project validations. Do not
  repeat expensive whole-project checks per file without a coverage/cost reason,
  and never drop required final checks to save time.
- Workers may edit only assigned paths under approved realization. Preserve shared
  interfaces, others' work and repository isolation. Ban `git stash`, `git reset`,
  `git checkout .` and `git clean`. Scoped editing never authorizes staging/commits.
- The independent verification gate covers every fix; reject demonstrated stubs,
  swallowed errors or unauthorized bypasses that violate the contract, not syntax
  alone. Do not suppress diagnostics, loosen checks or change expected behavior to
  fake progress.

## Execution workflow

Follow [queue guardrails](references/queue-guardrails.md). Obtain the contract and
execution/write permissions before ingestion or correction.

### 1. Ingest and normalize

Use repository-supported installed tools and current documented options. Historical
recipes are illustrations, not certified commands or approval to execute/install.
Do not use `npx` or similar resolution as a silent download. Capture stdout/stderr
and expected diagnostic exit codes without masking tool failure as an empty queue.
Persist only at approved destinations; protect secrets in captured output.
Prefer supported machine-readable formats. Text parsing is tool/version-specific,
not universal: preserve raw output and unmatched/multiline diagnostics, Windows
paths and paths with spaces. Report parse coverage and block assignments dependent
on missing/unrecognized data rather than dropping it silently.

### 2. Establish dependency order

Trace actual imports/build configuration as well as manifests.
Order approved batches by observed causal and build dependencies; use leaves
before consumers when that order removes cascading failures. Do not force a fixed
four-layer architecture or an order contradicted by the actual dependency graph.
Manifests or directory names alone
are not a complete graph. Detect strongly connected components; do not assume the
whole project is a DAG or that every cycle is illegal in the target toolchain.
If a cycle prevents safe ordering, block that component and propose a separately
approved cycle-breaking task. Do not automatically extract types, invert interfaces
or violate a mechanical port's 1:1 boundary. Unaffected independent components may
proceed under their existing approval and checks.

### 3. Resolve bounded batches

Approve separate worker and reviewer lots through the subagent model-selection
gate before dispatch; model choice is not delegation permission. Declare assigned
paths, diagnostics/snapshot, permitted checks, interfaces, concurrency constraints
and acceptance criteria. Avoid overlapping writes; dependent changes are sequential
or coordinated under explicit ownership, not concurrent shared-file edits.
Workers implement root-cause corrections only within the approved behavior contract.
Submit a scoped candidate to the independent gate; `ACCEPT` plus required checks
permits affected progress, not a commit. A permitted non-spawn implementation path
still needs independent review; if required worker capability is absent, disclose
and obtain approval for a changed execution plan rather than silently substituting.

### 4. Refresh and close

At each approved batch/checkpoint, rerun relevant validations and refresh the queue
against the current snapshot. Separate resolved, remaining, new, blocked and not
revalidated diagnostics; record changes of tool/configuration so counts remain
interpretable. New out-of-scope causes require new scope approval.
Perform required final project checks and behavioral regression tests on the final
snapshot, with fresh review covering any later changes. No backlog closure on
stale counts, disabled rules, parser gaps, pending review or failed/unavailable
required checks. Shipping remains separately authorized.

## Delivery evidence

Report in chat by default; files require approved content/destination. Include
initial/current snapshot and tool/configuration, raw/parsed/unmatched counts,
actual commands/exit results, observed tier progress, scoped corrections, review
snapshot/verdict and required final checks. Distinguish resolved, remaining, new,
blocked and not revalidated states. Report actual guardrail evidence and limits,
not assumed `ZERO (clean)` compliance or invented burn-down progress.
