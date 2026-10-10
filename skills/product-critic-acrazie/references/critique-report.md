# Critique Report

Write one concise English report in `docs/critics/<subject>.md` after the user
approves its content and exact destination. Keep evidence proportional to the
decision. Do not reproduce sensitive data or turn this report into a transcript.

## Report structure

```markdown
# <Product or subject> Critique

## Scope and status
- Repository and assessed revision; relevant local changes:
- Approved Task Contract:
- Selected priorities and exclusions:
- Report status: proposed / validated / superseded
- Report approval evidence:

## Product panorama
<Intended users, jobs, features, implementation costs, and selected priorities.
Identify observed evidence, declared needs, and unknowns separately.>

## Verdict and elements to retain
<Prioritized conclusion, including why no change may be the best option.>

## Priority: <specific mismatch>
- User job and affected users:
- Current behavior and implementation evidence:
- Claim type, source, confidence, and limitations:
- Concrete impact and constraints:
- Options: retain current / simplify / retire / replace, as applicable.
- Comparison: expected benefit, performance evidence or hypothesis, total cost,
  dependencies, migration, maintenance, risks, and compatibility obligations.
- Recommendation and conditions that could change it:
- Smallest verification method, baseline, and success criterion:
- Accepted decision and approval evidence, or pending user decision:

## Checks performed and evidence gaps
<Only actual checks and observations. Missing analytics, benchmarks, or access
remain explicit limitations, not proof of failure or success.>

## Next decisions and optional handoff
<Accepted options, unresolved decisions, suitable implementation owners, and
required targeted contracts. Report approval is not implementation authorization.>
```

Repeat the priority section only for selected material issues. Compare credible
options rather than forcing every issue into all four categories. Do not assign
invented numerical scores to sparse evidence. Effort estimates are estimates,
not measured implementation costs; name their assumptions.

For an existing report, preserve accepted decisions and approval evidence. If
new facts invalidate a prior conclusion, explain the change and obtain renewed
approval for affected content; do not silently retain an obsolete status.

An applicable Task Contract needs independent approval evidence beyond a status
label and current scope; preserve it rather than repeating settled questions.
Record loading and execution permissions separately when a handoff is requested.
In an explicit project kit, each required skill and the returning specialist need
their own activation before instructions are read or dispatched. Report approval
is not implementation authorization, a skill activation or installation permission.
