# Worked examples

## Example A — Common testing architecture across N repositories

Request: "create one coherent testing architecture shared by all my repositories."

Verdict: multi-agent, fan-out/fan-in behind a central spec. Reason: slices (repos) are independent to apply but share conventions that must stay identical; blind fan-out guarantees drift.

Workflow:

1. Single writer inspects one representative repo per stack, then writes a one-page testing spec: runner, layout, naming, fixtures, coverage gate, CI hook.
2. One worker per repo (max ~5 per wave) applies the spec to its repo only. Excluded: unrelated refactors, dependency upgrades.
3. Conformance pass: same checklist run against every repo (layout, sample test run output, CI status). Non-conformant slices get one bounded retry.

Worker return contract: changed files, diff stat, test command plus output excerpt, CI file path.

## Example B — Large codebase debugging

Request: "debug this large codebase, failures everywhere."

Verdict: start single, then narrow fan-out. Reason: symptoms may share one root cause; parallelizing before isolation multiplies noise.

Workflow:

1. Single reconnaissance: reproduce, collect failing paths, rank suspects, isolate independent leads.
2. Fan out only on confirmed independent leads (one worker per lead, bounded file set each).
3. Pipeline gate: each fix verified against reproduction plus adjacent tests before merge into the final report.

Worker return contract: root-cause claim with evidence lines, changed files, reproduction result before/after, adjacent test output. No drive-by refactors.
