# Task Contract

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
glossary, or ADR when relevant. Separate unknowns from established facts.>

## Approval
Status: draft | approved | blocked | superseded
<Who approved which contract, when, and a verifiable conversation/ticket reference
or the user's exact approval with enough context to identify the approved version.
Do not fabricate identifiers, timestamps, approval, or a signature.>

## Delivery evidence
<Initially pending. The executor later records checks actually run, their results,
criterion mappings, and residual limitations. Expected evidence is not proof.>
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
the same contract. Record the responsible specialist and whether the final user
approval explicitly permits its scoped realization; do not infer authority from a
status label or from approval of an unrelated snapshot. A contract may authorize
realization under the user's request, but does not activate a dependency or waive
installation, spawning, Git shipping or production permissions.

Interview persists the contract and stops. In an explicit project kit, disclose
the next specialist's command and wait for a new explicit invocation to resume.
This also applies when returning to a specialist used before Interview. Reuse the
same approved contract and answers at that return, unless material facts changed.

A mandatory dependency has a trigger, named owner, required result, success proof
and a blocked step. For Feature Builder and Test Retrofitter, missing/stale contract
triggers Interview; its approved persisted contract is the required result. A
current applicable contract with independent approval evidence satisfies that gate
without loading Interview. Unavailable or unactivated Interview blocks realization,
not authorized read-only discovery or unrelated work. Do not duplicate the missing
workflow or silently install it. Optional review becomes mandatory if accepted or
required by repository policy, with independent proof on the final task snapshot;
review activation and agent/model authorization remain separate.
