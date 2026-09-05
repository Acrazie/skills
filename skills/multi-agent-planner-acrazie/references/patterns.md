# Patterns (v1)

Three patterns only. Anything else is out of scope: propose single-agent instead.

## Decision table

| Signal | Single sequential | Fan-out / fan-in | Verified pipeline |
|---|---|---|---|
| Subtasks independent | no | yes | partially (ordered) |
| Shared contracts across slices | n/a (one writer) | yes, frozen in central spec | yes, passed stage to stage |
| Context fits one window | yes | no | sometimes |
| Error in one slice contaminates others | n/a | must be contained by spec | must be caught at stage gate |

Default: single sequential. Choose multi only when independence is real and coordination cost is lower than the gain.

## 1. Single sequential

One agent, minimal scope, verify at the end. Use for small volume, dependent tasks, coherence-dominated work, or when delegation overhead exceeds the gain.

## 2. Fan-out / fan-in behind a central spec

Phases:

1. One writer produces a short central spec (one page max): goal, shared conventions, interfaces, done-criteria.
2. N workers (max ~5) execute slices constrained by the spec. Each receives the spec pointer plus its local scope only.
3. One conformance pass checks every slice against the spec before declaring done.

Never fan out before phase 1. Use for multi-repository or multi-module work with shared conventions.

## 3. Verified pipeline

Ordered stages; each stage's output handle is verified before the next starts. Use for dependent work that still benefits from separation (reconnaissance, then isolated fixes, then validation).

## Worker contract (minimal)

Every worker prompt contains: goal, included/excluded paths, minimal context, bounded numbered steps, return contract (changed files, diff, verifiable handles, test output), stop condition, forbidden actions (no cascade spawning, no unrelated refactors, no secret exfiltration).

## Token rules (hybrid)

- Central spec: short, shared once.
- Per worker: detailed local scope only, never full history.
- Returns: synthetic by default (files, diffs, handles, test lines). Full logs on orchestrator request only.
