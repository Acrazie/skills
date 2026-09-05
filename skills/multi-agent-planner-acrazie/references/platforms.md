# Platform notes

The skill core stays platform-agnostic. Apply these notes only at copy time, when adapting worker prompts to where they will run.

## Generic fallback (unknown platform)

Present each worker as a fenced block with goal, scope, context, steps, return contract, and stop condition. The user spawns workers with whatever mechanism their agent offers. Never invent platform syntax.

## Claude Code

Workers run through the Task tool or Subagent mechanism. Keep prompts self-contained: include the spec pointer inline since workers may not share conversation history. Ask the user to run workers with the project's documented subagent command.

## Codex

Workers run as separate agent turns or background tasks per the project's Codex setup. Same rule: self-contained prompts, minimal context, explicit return contract with file paths and diffs.

## OpenCode and others (including Antigravity-class tools)

Same treatment: self-contained fenced prompts, no assumed shared memory between workers. If the platform lacks true parallelism, present the workflow as an ordered pipeline the user runs sequentially — the split and contracts still save tokens by bounding each step.

## What never changes per platform

Verdict logic, coherence rule, token rules, guardrails (max ~5 workers, no cascade, one retry), and verification on handles. Only the spawning gesture adapts.
