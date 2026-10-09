---
name: feature-builder-acrazie
description: >-
  Implement a new application feature from an explicitly approved task contract,
  with scoped tests, an optional independent adversarial review, and criterion-linked
  delivery evidence. Use when the user requests new application behavior.
  Not for bug fixes, behavior-preserving refactors,
  repository setup, tooling migrations, Jenkins, README design, specialized visual
  workflows, or reviewing another agent's work.
---

# Feature Builder / Acrazie

Deliver only the requested new behavior, with enough proof to avoid handing the
user untested, misinterpreted, or gratuitously expanded work. One sequential
workflow, not a general orchestrator. Implement and test the feature; delegate any
user-approved independent review to `adversarial-reviewer-acrazie`, never review
your own work under that role or duplicate its rubric.

## Project loading boundary

Published-library defaults remain model-invocable within the requested task. An
explicit project kit or stricter current instruction takes precedence: propose
this skill from available metadata and wait for the user's explicit command before
reading its instructions. Apply the same gate to each dependency, including a
reviewer dispatched to another context. One invocation does not activate the chain.
Use `$skill-name` in Codex or `/skill-name` in Claude Code; do not silently read a
missing or unactivated dependency as a workaround. These gates are not filesystem
access controls and do not prove live host behavior. Global homonyms may remain a
blocker. Loading approval never grants execution, installation, spawning or shipping
permission. Under ordinary library defaults, retain scoped implicit handoffs.

## Entry and ownership

Select this skill when the user requests a new application feature or authorizes
a scoped feature handoff. Under published defaults no named skill command is
required; the project loading boundary above governs explicit kits. Selection permits
relevant discovery, not implementation before contract approval, new objectives,
or separately restricted actions.

Read repository instructions and inspect relevant behavior, invariants, tests,
manifests, Git state, and existing task documents before editing. Reuse behavior
that already satisfies the request instead of rebuilding it. Keep unrelated or
pre-existing changes untouched and obey repository worktree requirements.

Do not turn a bug fix, refactor, tooling migration, pipeline change, or primary
README task into a feature. Refer those to their responsible workflows. Specialized
Canvas/hero/SVG design belongs to the corresponding visual skill; ordinary UI
features remain in scope and retain accessibility and responsive requirements.
Do not implement a domain specialist's excluded workflow under this entry point.

## User decision format

For any user-owned choice, including execution/setup permission, review and model
selection, display only Current state, numbered Options, Recommendation and
Response. Translate labels/content into the user's language; do not add question
IDs, preselect an answer as consent or treat a recommendation as approval. Ask only
unresolved decisions, with their verified context and concrete consequences.

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

## Obtain the contract

Reuse an explicitly approved Task Contract if it covers the current request, has
approval evidence beyond a status label, and no material discovery invalidates it.
Use its criteria as the acceptance boundary; do not interview again for ceremony.

If material discovery invalidates the contract, reopen only affected decisions.
Interview is mandatory only when no applicable approved contract can be reused.
When required, propose `interview-acrazie`, applying the project loading boundary before
reading or invoking it. Supply the requested feature, verified context,
scope exclusions, material decisions still needed, and expected handoff: an approved
persisted contract with observable criteria and planned test evidence. Let that
skill own the interview and documentation; do not embed a second interview here.

When required Interview is unavailable or not activated under the applicable gate,
block implementation only, explain the missing prerequisite, and request activation
or separately approved installation. Do not install silently or substitute a copy.
A reusable approved contract does not require Interview to be installed or loaded.
In an explicit kit, use Repo Init's approved project update flow and the project's
pinned selection; do not bypass its managed packages with an unpinned install.
Outside a managed kit, this command is a proposal, not execution permission:

```bash
npx skills add Acrazie/skills@interview-acrazie
```

Availability means the approved installed dependency can be located; discover that
from metadata without loading its body when a loading gate applies. After required
activation, use the harness's supported skill invocation, or read its installed
`SKILL.md` and follow it when no Skill tool exists. Do not assume a tool named `Skill` exists.
If installation is unsuccessful or the skill is not yet published, report that
condition and remain stopped. After installation, resume from existing answers.

Approval of the feature contract allows scoped implementation only when its
independently evidenced final approval authorizes that realization under the user's
request and the applicable loading gate is satisfied. Otherwise ask for scoped
execution authorization before editing. It does not authorize dependency
installation, Git shipping, production changes or other separately restricted actions.

## Implement and prove

1. Map each criterion to the smallest sufficient test or check. Cover requested
   behavior, relevant errors and edge cases, and existing behavior exposed to
   regression. Do not retest the entire project or chase arbitrary 100% coverage;
   narrower scope never excuses missing security, data integrity, or access checks.
2. Use the existing test runner and repository patterns. Add targeted tests before
   or alongside code. Where feasible, run a new test before implementation and
   verify its expected failure concerns the missing behavior, not a broken setup.
   Tests must express approved behavior, not merely mirror the implementation.
3. If no adequate test tooling exists, ask before adding a dependency. Use a native
   or existing equivalent when it provides sufficient evidence. If permission is
   refused or checks are unavailable, disclose the gap; do not silently downgrade
   acceptance criteria or declare the feature complete without sufficient proof.
4. Implement in the responsible layer using existing abstractions and conventions.
   Keep every change attributable to the approved scope. No opportunistic cleanup,
   extra UI, configurable scaffolding, or speculative extension points.
5. Run targeted tests and the smallest additional checks needed for affected
   boundaries, such as type checking, build, integration, or accessibility checks.
   Attribute pre-existing failures separately; do not expand scope to fix them.
6. Compare the diff to the contract. Remove unrequested additions. If discovery
   changes user-facing behavior, scope, data/security guarantees, or a material
   approved choice, pause and propose returning only affected decisions to
   `interview-acrazie`, respecting its separate activation gate. Obtain renewed
   approval before implementing that change, not for ordinary
   internal choices already within the contract.

## Offer independent review

After implementation and targeted checks, always offer an independent review
before declaring delivery complete. Recommend either running or skipping it based
on the actual diff, affected invariants, regression exposure, and remaining test
gaps. Explain the concrete benefit and additional cost briefly. Small, well-tested
changes can justify skipping; concurrency, resource lifetimes, permissions, data
integrity, and cross-boundary behavior warrant stronger scrutiny. Do not claim
review is universally necessary or that tests guarantee correctness.

If repository policy requires review, report it as a mandatory gate rather than
an optional offer; a decline cannot waive that policy. Otherwise wait for the
user's explicit choice. Accepting review is not a skill activation in an explicit
project kit: request the reviewer's separate command before reading or dispatching
its instructions. Keep skill activation, review authorization and model selection
separate. Record recommendation, rationale, requirement and choice in the same
Task Contract. If optional review is declined, continue ordinary delivery with its
existing proof requirements. Never silently activate another skill for review.

If accepted, review becomes a completion gate:

Validate the reviewer lot through the subagent model-selection gate before creating
its fresh context. Accepting review is not selecting its model. Approval may cover
the already-bounded re-review cycles when role, mission/scope, risk, and model stay
unchanged; each review still requires a fresh context and a fixed snapshot.

1. Locate and read `adversarial-reviewer-acrazie`. If unavailable, stop and offer
   user-approved installation using `npx skills add Acrazie/skills@adversarial-reviewer-acrazie`
   or a manual handoff to a separate context where that skill is available.
   Never install silently.
   If a separate context cannot be created, disclose that limitation and stay
   blocked unless the user explicitly withdraws an optional review requirement.
   A policy-required review remains blocked pending approved policy resolution. Reading
   the skill in the implementer's context is not an independent review.
2. Invoke that skill in a fresh agent context without inherited conversation
   history, or use the approved manual handoff. Supply a fixed snapshot of the
   task's complete diff (including new files), its base revision or before-state,
   and the authoritative contract/criteria. Exclude unrelated user changes and
   author explanations. Permit read-only access to relevant surrounding code,
   tests, repository instructions, and API documentation; freeze the task changes
   during review. The reviewer does not edit or implement fixes.
3. Preserve the report and the reviewed snapshot identity in the contract's
   delivery evidence. An incomplete review or missing verdict is not `ACCEPT`.
   `ACCEPT` means no demonstrated defect within the reviewed scope, not proof of
   absence of bugs, and never replaces test evidence. It applies only to the
   reviewed snapshot; subsequent task changes require another review. In an explicit
   project kit, each re-review handoff needs a new reviewer activation; a bounded
   review/model approval can remain applicable, but is not that activation.
4. For `REJECT`, correct demonstrated defects introduced by the task only within
   the approved contract, without requiring approval for each ordinary correction.
   Add targeted regression evidence, rerun affected checks, and request review of
   the updated complete task diff in a fresh context. Allow at most two correction
   and re-review cycles after the initial review. If rejection persists, stop and
   report the outstanding proofs of flaw for user arbitration; do not loop forever.
5. Report pre-existing or out-of-scope findings separately without fixing them or
   treating them as newly introduced defects. For disputed findings or changes
   requiring a new scope/guarantee, pause for user arbitration and, when needed,
   renewed contract approval. Never silently override `REJECT`. Explicit withdrawal
   of an optional accepted review gate must be recorded; it does not waive a review
   required by repository policy, unmet feature criteria or known defects. Resolve
   policy changes separately rather than treating withdrawal as a bypass.

## Delivery

Update the same contract's delivery evidence with checks actually executed, results,
criterion mappings, limitations, and review status (pending choice, declined,
accepted, rejected, blocked, or explicitly withdrawn). Report changed behavior,
proof for each
criterion, relevant regressions checked, and remaining gaps. Distinguish local
validation, CI, deployment, and live verification; do not infer one from another.

Declare complete only when the approved behavior is implemented, every criterion
has sufficient evidence, no unrequested changes remain, and the review offer has
an explicit user decision. If review remains required, also require `ACCEPT` on
the final task snapshot. Otherwise identify
what is incomplete or blocked. Do not commit, push, open a PR, or deploy merely
because implementation is finished; follow the user's and repository's separate
authorization for shipping.
