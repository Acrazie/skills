---
name: multi-agent-planner-acrazie
description: Decide single-agent vs multi-agent execution through a short option-driven interview and produce a verified copy-paste workflow. Use only when the user explicitly invokes multi-agent-planner-acrazie before spawning parallel subagents, multi-repository work, or large debugging; never for single-file edits, trivial tasks, or execution itself.
---

# Multi-Agent Planner / Acrazie

Help the user decide whether a task needs one sequential minimalist agent or a multi-agent workflow, then produce a workflow the user can execute on any coding-agent platform. Token savings come from refusing unjustified parallelism, not from clever orchestration.

Use generic vocabulary only in the core (orchestrator / worker / contract / verification). Never emit platform-specific spawn syntax in the core; delegate that to `references/platforms.md`.

## Invocation guard

Run only after explicit user invocation. If activated implicitly, do not plan; ask the user to invoke `$multi-agent-planner-acrazie` (or the platform-equivalent explicit command).

## Scope and invariants

- Plan, do not execute. This skill produces a decision plus an executable workflow; it never spawns workers itself.
- Default to a single sequential agent. Multi-agent must earn its place against the arbitration criteria below.
- Cover three patterns only in v1: single sequential, fan-out/fan-in behind a central spec, verified pipeline. No hierarchical supervisors, no free cascades, no worker-spawns-worker.
- Keep worker count low (max ~5). One retry max per worker. No silent re-delegation.
- Require verifiable worker contracts. A worker claiming success without a checkable handle (absolute path, diff, URL, ID, test output) has not succeeded.
- Never expose secrets. Contracts carry only minimal excerpts, never credentials.
- Do not commit or push. Present the workflow and wait for approval before the user executes it elsewhere.
- Write SKILL.md in English; conduct the interview and write the deliverable in the user's language (French by default when the user writes French).

## Inspect before interviewing

Determine facts the environment can answer before asking: repository roots involved, file counts, languages, test setups, current Git state, existing specs or ADRs, and whether subagents are even available on the current platform. Read [references/interview-tree.md](references/interview-tree.md) before the first round. Do not ask the user for anything discoverable.

## Interview as a decision tree

Separate verified facts from user-owned decisions. The frontier is every unresolved decision whose prerequisites are settled. Ask the whole frontier in one round.

Interview rules:

1. Short rounds only (3-5 questions max per round).
2. Every question proposes 2-3 concrete options (labelled Option A/B/C), then gives exactly one recommendation with a short reason why it is the best for this case.
3. Normally one round settles the verdict. Ask a second round only when answers unblock a material dependent decision (coherence mechanism, worker split, verification path).
4. Stop as soon as verdict (single vs multi) plus task split plus worker contracts are settled. Remaining details fall back to sensible defaults; state them plainly.
5. Offer a fast path once per campaign: "décide seul avec des défauts raisonnables" for users in a hurry. If chosen, decide autonomously and mark every assumption as such.
6. Never continue interviewing for completeness after the decision is clear. Interaction is cheap but not free.

Stop criterion: verdict plus split plus contracts settled, or user chose the fast path. Then emit the deliverable and wait for explicit approval.

## Arbitration (single vs multi)

Decide on four axes. See [references/patterns.md](references/patterns.md) for the decision table.

1. Independence: can subtasks run without reading each other's output?
2. Context volume: does the whole task fit one agent window without drowning the signal?
3. Dependencies: do repos or files share contracts, schemas, or conventions that must stay coherent?
4. Error cost: if one worker drifts, is recovery cheap or contaminating?

Refuse multi-agent when subtasks are dependent, volume is small, coherence dominates, or coordination costs more than it saves. Say so plainly and produce the single-agent plan instead. An unjustified fan-out is the most expensive outcome.

## Coherence rule

- Multi-repository or shared-convention work: phase 1 writes one short central spec (one page max), phase 2 runs workers constrained by that spec, phase 3 runs a conformance pass. Never fan out blindly.
- Large debugging: one agent does global reconnaissance first (symptoms, call paths, suspects), then parallelize only on already-isolated independent leads.
- Shared spec stays short. Full history never ships to every worker.

## Token economy

Apply the hybrid rule: one short central spec plus detailed local scope per worker. Workers return synthetic summaries (changed files, diffs, handles, test results); full logs only on orchestrator request. See [references/patterns.md](references/patterns.md).

## Guardrails

- Max ~5 workers, no cascade, one retry max.
- Each worker prompt states its perimeter, forbidden paths, and stop condition.
- Parent (orchestrator or user) verifies every success claim against its handle before declaring done.
- If verification fails, fix with one bounded retry or fall back to single-agent for that slice. Never loop silently.

## Deliverable

ALWAYS use this exact three-block template, in the user's language:

```markdown
# Workflow decision

## 1. Verdict
Single-agent | Multi-agent + pattern name. Two to four sentences: why, on which arbitration axes, and what was rejected.

## 2. Workflow architecture
Pattern, phases in order, per-phase agent, inputs, outputs, and where verification happens.

## 3. Worker prompts (copy-paste)
One fenced block per worker:
- Goal (one sentence)
- Scope (included / excluded paths)
- Context (minimal excerpts or spec pointer only)
- Steps (numbered, bounded)
- Return contract (changed files, diff, verifiable handles, test output)
- Stop condition and forbidden actions
```

Adapt spawn syntax per platform only at copy time using [references/platforms.md](references/platforms.md). Show two worked examples in [references/examples.md](references/examples.md) when the user's case matches them.

## Verification before handoff

Before presenting, check: verdict follows the four axes, every worker has a bounded scope plus a return contract, no platform syntax leaked into the core, coherence phase present when needed, worker count and retry limits respected. Fix silently, then present. Wait for explicit user approval before any execution.
