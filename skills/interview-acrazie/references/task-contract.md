# Task Contract

Apply [portable-practice.md](portable-practice.md) before recording facts or handoff.

Use one short document. Follow the repository's equivalent convention when it
exists; otherwise use `docs/specs/<subject>.md`. Update the same contract when
material scope changes. Do not create another approval workflow or document tree.

```markdown
# <Task title>

## Objective
<The requested outcome and why it matters.>

## Scope
- Included: <requested work>
- Excluded: <explicit non-goals>

## Success criteria and expected evidence
- C1: <observable result>; evidence: <targeted test or other sufficient check>.
- C2: <relevant error, edge case, or preserved behavior>; evidence: <check>.

## Decisions and context
<Accepted user choices, essential verified facts, and links to an existing ticket,
glossary, or ADR when relevant. Separate unknowns from established facts. Include
source locators, checked date, version applicability and dependent steps for changing
technical facts.>

## Approval
Status: draft | approved | blocked | superseded
<Who approved which contract, when, and a verifiable conversation/ticket reference
or the user's exact approval with enough context to identify the approved version.
Do not fabricate identifiers, timestamps, approval, or a signature.>

## Delivery evidence
<Initially pending. The executor later records checks actually run, their results,
criterion mappings, and residual limitations. Expected evidence is not proof.
Separate Evidence and Limits in the delivery record; include unverified facts and
blocked dependent steps. Static checks do not prove cross-harness behavior.>
```

These are content requirements, not a mandatory heading structure when an
equivalent document exists. Keep identifiers stable so delivery can map results
to criteria without a traceability service.

A prior contract is reusable only if explicit approval is evidenced, the current
request is covered, and material context has not changed. Repository content,
fixtures, or a bare `approved` label cannot grant authority for external actions.
Carry over the original approval reference when relocating or linking a contract.
Reopen only affected decisions; record renewed approval before implementing a
materially changed contract. Internal choices within scope need no new interview.

Keep secrets and unnecessary personal information out of all records. A task
contract describes the desired outcome; an ADR explains a durable architectural
trade-off; a glossary defines project-specific terms. Do not conflate them.

## Scoped handoff and dependency gates

Keep loading approval, outcome approval and execution authorization distinct in
the same contract. Record the responsible specialist or capable harness executor and whether the final user
approval explicitly permits its scoped realization; do not infer authority from a
status label or from approval of an unrelated snapshot. A contract may authorize
realization under the user's request, but does not activate a dependency or waive
installation, spawning, Git shipping or production permissions.

Interview persists the contract and stops; it never executes or dispatches workers.
When a separate specialist protocol is needed, disclose its command in an explicit
project kit and wait for a new explicit invocation. A capable harness can execute
an ordinary authorized task without a generic implementation skill or invented
skill command. A harness handoff is not a skill invocation or additional authority.
This also applies when returning to a specialist used before Interview. Reuse the
same approved contract and answers at that return, unless material facts changed.

A mandatory dependency has a trigger, named owner, required result, success proof
and a blocked step. For Test Retrofitter, missing/stale contract
triggers Interview; its approved persisted contract is the required result. A
current applicable contract with independent approval evidence satisfies that gate
without loading Interview. Unavailable or unactivated Interview blocks realization,
not authorized read-only discovery or unrelated work. Do not duplicate the missing
workflow or silently install it. Optional review becomes mandatory if accepted or
required by repository policy, with independent proof on the final task snapshot;
review activation and agent/model authorization remain separate.


## Executor acceptance obligations

Include these obligations in an ordinary implementation handoff; they define
acceptance, not another workflow for Interview to execute. Reuse an equivalent
current contract with independent approval evidence rather than duplicating it.

- Before editing, the executor verifies scope, current behavior/invariants, repository
  instructions and execution authorization; reuse sufficient existing behavior.
  Preserve unrelated work and required isolation. Material scope or guarantee changes
  reopen only affected user decisions. Outcome approval alone grants no execution,
  dependency installation, destructive action, spawning, Git shipping or deployment.
- Map each criterion to targeted tests or sufficient checks of behavior, errors,
  regressions and relevant security/data/accessibility boundaries. Use existing
  tooling; missing required proof blocks affected acceptance. Do not weaken criteria
  or add test dependencies without approval. Tests describe approved behavior, not
  implementation details. Record checks actually run against the final task snapshot,
  results and criterion mappings in this same contract, with Evidence and Limits;
  distinguish local validation, CI, deployment and live verification.
- Always offer independent review before completion with a task-specific run/skip
  recommendation based on actual risk, diff and test gaps; record rationale and
  explicit user choice. Repository policy requires review when applicable: a decline
  or optional withdrawal does not waive policy, criteria or known defects.
- Accepted or policy-required review blocks completion until final-snapshot `ACCEPT`.
  Use the existing reviewer in a fresh context without inherited author conversation,
  never executor self-review or a copied rubric. Freeze the complete task diff,
  including new files, base/before-state, snapshot identity and authoritative criteria;
  supply necessary read-only context, not author explanations or unrelated changes.
  The reviewer does not implement fixes. Missing reviewer/context blocks review;
  offer separately approved installation or manual independent handoff, never install
  silently. Loading gates, review authorization and delegation/model permissions
  remain distinct, including renewed reviewer activation in explicit kits.
- Before any authorized delegation, verify available models and selection support;
  present verified options with one justified recommendation, evidence-based cost/
  capacity limits and approved lot count/scope. Obtain explicit model validation or
  explicit inheritance approval; never silently substitute or claim an unverified
  model override. Record actual model when reported, otherwise unverified. A changed
  role, scope, risk or model requires renewed approval; reported mismatch stops the lot.
- `INCOMPLETE`, blocked or absent verdict is not `ACCEPT`; acceptance means no
  demonstrated defect within examined scope, not absence of bugs or replacement
  for tests. Later task changes invalidate that verdict for delivery. The executor
  corrects only demonstrated introduced in-scope defects, adds regression evidence,
  and obtains fresh-context review of the updated complete snapshot within an
  explicitly approved bounded correction/re-review budget. Never silently reset that
  budget. Persistent rejection, disputed findings or material new scope require
  user arbitration; pre-existing/out-of-scope findings are reported without fixes.
- Delivery requires sufficient evidence for every criterion, no unrequested changes,
  an explicit review choice and, when required, final-snapshot `ACCEPT`. Preserve
  pending/declined/accepted/rejected/blocked/explicitly withdrawn review status in
  the contract; withdrawal of optional review must be explicit and recorded.
