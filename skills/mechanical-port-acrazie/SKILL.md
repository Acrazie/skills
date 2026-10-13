---
name: mechanical-port-acrazie
description: >-
  Plan, orchestrate, and execute language-to-language mechanical codebase migrations
  through 1:1 structural mirroring, pre-translation paradigm mapping, canary trial runs,
  and mandatory test oracle verification. Use when migrating a repository or major component
  from one programming language to another. Not for internal refactoring within the same language,
  fixing isolated bugs, or rewriting without an automated test suite.
---

# Mechanical Port / Acrazie

Port a selected source-to-target language boundary with faithful structural
mirroring and an objective test oracle. Do not redesign or introduce hybrid FFI
as an unapproved shortcut.

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


## Migration invariants

- Require an adequate language-independent or black-box automated oracle that
  already exists and passes against the source codebase
  on the identified snapshot before any target code is written. Record command, source
  revision, environment, results and coverage limits. Compilation alone is not an
  oracle; missing, incomplete or compiler-coupled tests block translation.
- Propose `test-retrofitter-acrazie` when oracle work is needed.
  Obtain authorization for that prerequisite testing work; its loading,
  contract and realization permissions remain separate. Do not manufacture a
  passing oracle by changing expected behavior or translating first.
- Preserve directory hierarchy, module boundaries, naming patterns, algorithms,
  observable behavior and resource semantics across the approved boundary. Do not
  change database, architecture or idioms to hide translation problems.
- Respect required isolation. Preserve unrelated files; approve target destinations
  and any necessary language-specific layout exception before implementation.

## Four-phase migration workflow

Follow [migration pipeline](references/migration-pipeline.md) for details.
A same-context skill handoff is not a spawn; pass applicable lot approval to a
recipient without granting new roles, scope or model choices. Apply the subagent
model-selection gate to separately authorized translation, reviewer and diagnostic
worker lots. No automatic worker spawning from migration approval.

1. **Paradigm mapping**: reuse or record traceable paradigm mapping in an
   approved accessible document or contract after artifact/write approval.
   `PARADIGM-MAPPING.md` is an example name, not a required format or destination. Cover memory/resource lifecycle, error model,
   concurrency/asynchrony and types/nullability. Trace actual source semantics;
   examples are prompts for investigation, not universal translations.
2. **Ownership matrix**: reuse or record traceable resource ownership evidence within approved write scope.
   A table in the same approved document may suffice; `OWNERSHIP-MATRIX.tsv` is an example, not a required separate artifact.
   Inventory fields/resources, allocation locus, owner lifetime, cleanup trigger,
   aliases and concurrency boundaries needed for the selected migration.
3. **Canary trial**: select representative units covering the actual semantic risks and
   boundaries of the approved port, not a fixed file count. Explain coverage and gaps
   before translating; a small boundary may need fewer units, while distinct
   lifecycle, error or concurrency risks may need more. Translate according to the mapping, run applicable checks
   and oracle, and obtain independent `ACCEPT` covering every canary. Refine mapping
   on discovered semantic issues and revalidate affected code before full translation.
4. **Full translation**: mirror remaining units, verify each through the independent
   gate and run the authorized target validations plus unchanged behavioral oracle.
   For a mass compiler/linter backlog, propose `diagnostic-queue-runner-acrazie`;
   activate it under the applicable gate and pass snapshot, scope, mapping, queue
   evidence and permissions. A small or empty backlog does not require Queue.
   If required mass-queue dependency is unavailable, block that dependent resolution
   step, not unrelated discovery. Do not silently substitute a generic fixer.

After Queue changes, revalidate affected reviews and run final target checks and
oracle against the final snapshot. Queue completion, fewer errors or a prior
source pass does not prove target equivalence. If checks cannot run, record the
blocked gate; never declare the migration verified or complete.

## Delivery evidence

Report in chat by default; file writing requires approved content/destination.
Include source/target environments, contract and snapshots, oracle command/results
and coverage limits, mapping/ownership/canary evidence, its accessible location and coverage status, reviewed units and exact review
snapshot/verdict, target checks, queue handoff status and remaining authorized step.
Distinguish passed, failed, blocked, not executed and unverified states. Do not
force `VERIFIED` when the oracle is absent or the target was never tested. Report
actual artifacts and outcomes only, not intended actions as completed work.
