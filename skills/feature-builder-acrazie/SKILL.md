---
name: feature-builder-acrazie
description: >-
  Implement a new application feature from an explicitly approved task contract,
  with scoped tests, an optional independent adversarial review, and criterion-linked
  delivery evidence. Use only when the user invokes feature-builder-acrazie.
  Not for bug fixes, behavior-preserving refactors,
  repository setup, tooling migrations, Jenkins, README design, specialized visual
  workflows, or reviewing another agent's work.
disable-model-invocation: true
---

# Feature Builder / Acrazie

Deliver only the requested new behavior, with enough proof to avoid handing the
user untested, misinterpreted, or gratuitously expanded work. One sequential
workflow, not a general orchestrator. Implement and test the feature; delegate any
user-approved independent review to `adversarial-reviewer-acrazie`, never review
your own work under that role or duplicate its rubric.

## Entry and ownership

Run only after explicit human invocation. If activated implicitly, ask the user to
invoke `$feature-builder-acrazie`; do not interview or edit yet.

Read repository instructions and inspect relevant behavior, invariants, tests,
manifests, Git state, and existing task documents before editing. Reuse behavior
that already satisfies the request instead of rebuilding it. Keep unrelated or
pre-existing changes untouched and obey repository worktree requirements.

Do not turn a bug fix, refactor, tooling migration, pipeline change, or primary
README task into a feature. Refer those to their responsible workflows. Specialized
Canvas/hero/SVG design belongs to the corresponding visual skill; ordinary UI
features remain in scope and retain accessibility and responsive requirements.
Do not implement a domain specialist's excluded workflow under this entry point.

## Obtain the contract

Reuse an explicitly approved Task Contract if it covers the current request, has
approval evidence beyond a status label, and no material discovery invalidates it.
Use its criteria as the acceptance boundary; do not interview again for ceremony.

Otherwise use `$interview-acrazie`. Supply the requested feature, verified context,
scope exclusions, material decisions still needed, and expected handoff: an approved
persisted contract with observable criteria and planned test evidence. Let that
skill own the interview and documentation; do not embed a second interview here.

If `interview-acrazie` is unavailable, stop before implementation. Ask the user to
install it and provide this command; do not install silently or substitute a copy:

```bash
npx skills add Acrazie/skills@interview-acrazie
```

Availability means the installed skill can be located and its instructions read.
Use the harness's supported skill invocation, or read the installed `SKILL.md`
and follow it when no Skill tool exists. Do not assume a tool named `Skill` exists.
If installation is unsuccessful or the skill is not yet published, report that
condition and remain stopped. After installation, resume from existing answers.

Approval of the feature contract allows scoped implementation under the user's
request, not dependency installation, Git shipping, production changes, or other
actions requiring separate permission.

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
   approved choice, pause and return only affected decisions to `interview-acrazie`.
   Obtain renewed approval before implementing that change, not for ordinary
   internal choices already within the contract.

## Offer independent review

After implementation and targeted checks, always offer an independent review
before declaring delivery complete. Recommend either running or skipping it based
on the actual diff, affected invariants, regression exposure, and remaining test
gaps. Explain the concrete benefit and additional cost briefly. Small, well-tested
changes can justify skipping; concurrency, resource lifetimes, permissions, data
integrity, and cross-boundary behavior warrant stronger scrutiny. Do not claim
review is universally necessary or that tests guarantee correctness.

Wait for the user's explicit choice; feature approval alone does not activate
review. Record the recommendation, rationale, and choice in the same Task Contract.
If declined, continue ordinary delivery with its existing proof requirements.

If accepted, review becomes a completion gate:

1. Locate and read `adversarial-reviewer-acrazie`. If unavailable, stop and offer
   user-approved installation using `npx skills add Acrazie/skills@adversarial-reviewer-acrazie`
   or a manual handoff to a separate context where that skill is available.
   Never install silently.
   If a separate context cannot be created, disclose that limitation and stay
   blocked unless the user explicitly withdraws the review requirement. Reading
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
   reviewed snapshot; subsequent task changes require another review.
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
   of the review gate must be recorded; it does not waive unmet feature criteria or
   make known defects disappear.

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
