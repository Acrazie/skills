# Optional independent review for Feature Builder

## Objective and scope

Extend `feature-builder-acrazie` with an always-offered, user-approved independent
review by the existing `adversarial-reviewer-acrazie`. Preserve specialist ownership
and targeted tests; do not build a general orchestrator or duplicate the rubric.
Extend the reviewer to check affected functional criteria, bugs and regressions,
and correct its JavaScript fallback and Python string-length examples. Align the
existing glossary and split-context ADR, rather than creating redundant decisions.

## Approved decisions

- Offer review after implementation and targeted checks, before completion, with a
  concrete task-specific recommendation to run or skip. Wait for an explicit choice.
- Use the existing reviewer in a fresh context without inherited author history.
  Supply the complete fixed task diff, authoritative contract, and necessary
  read-only technical context, not author explanations or unrelated changes.
- If accepted, review gates completion. A completed `ACCEPT` applies only to the
  final reviewed snapshot and does not replace tests or guarantee absence of bugs.
- The builder may fix demonstrated introduced defects within the approved scope,
  rerun affected checks, and obtain another independent review. After two failed
  correction/re-review cycles, stop for user arbitration.
- Pre-existing and out-of-scope findings are reported separately, not silently
  fixed. Disputes or changed scope require user arbitration.
- Missing skill or independent context blocks an accepted review. Offer authorized
  installation or manual isolated handoff. Only explicit user withdrawal removes
  this gate; unmet feature criteria and known defects remain disclosed.

## Success criteria and expected evidence

- C1: Builder always offers a justified run/skip choice, never invokes review
  without acceptance, and records that choice in the existing Task Contract.
- C2: Reviewer receives an isolated fixed snapshot and authoritative requirements,
  detects demonstrated functional defects, never fixes code, and ties its verdict
  to examined scope and snapshot. Missing evidence is not `ACCEPT`.
- C3: Accepted review blocks completion until final-snapshot acceptance or explicit
  withdrawal. Corrections, fresh review, two-cycle limit, disputes, and missing
  reviewer/context follow the approved boundaries.
- C4: Both metadata policies remain synchronized; documentation preserves distinct
  implementer/reviewer ownership; corrected rubric examples match runtime behavior.
- Evidence: repository hooks, scoped metadata/JSON/link checks, runtime examples,
  and bounded behavioral exercises. Exercises are not live application proof or an
  exhaustive regression benchmark.

## Approval

Approved in the 2026-10-06 Codex conversation. The user requested a systematic,
task-sensitive proposal (Q1), accepted recommendations for scope, independence,
and blocking review (Q2–Q4), accepted bounded corrections and unavailable-review
handling (Q5–Q6), then replied `ok` to the consolidated scope and modification
authorization, including rubric corrections, documentation, and targeted evals.
Repository Git permissions apply separately; no installation or deployment is
authorized by this contract.

## Delivery evidence

- C1/C3: Four bounded builder decision exercises covered a low-risk review decline,
  accepted review without an independent context, rejection/correction/arbitration
  and stale acceptance, and a high-risk asynchronous-cancellation proposal. Revised
  outputs satisfied 15/15 maintained expectations; baseline outputs satisfied 5/15.
  The baseline already respected some prompt-level instructions and ordinary proof
  requirements, but lacked the new review protocol. These are single-run simulated
  state traces, not statistical performance measurements or live feature execution.
- C2: Three independent static reviewer exercises satisfied 9/9 expectations:
  rejected a functional default-filter regression, accepted contract-valid nullish
  fallback and code-point counting, and kept incomplete intake without a binary
  verdict while separating an unchanged pre-existing observation. No tests or
  application changes were executed by these simulated reviewers.
- C4: Repository skill-frontmatter and structure hooks passed. Ruby Psych parsed
  both frontmatters and UI YAML files; name, description limits, prompt references,
  invocation synchronization, eval JSON shape/unique IDs, and changed local Markdown
  links passed assertions. `git diff --check` passed.
- C4: Executed Node assertions verified nullish short-circuiting and falsy-value
  differences; Python assertions verified combining characters and emoji code-point
  counts. Context7 documentation from MDN and CPython corroborated both corrections.
- Raw exercises, baseline snapshots, and the generated static review viewer are
  internal artifacts, not published skill resources. Timing/token telemetry was
  unavailable and is not reported as zero. Site build was not run: this worktree
  has no installed site dependencies, and this task does not install dependencies.
  This evidence establishes local checks only, not CI, deployment, or live usage.
