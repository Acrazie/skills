# Platform notes

The skill core stays platform-agnostic. Apply these notes only at copy time, when adapting worker prompts to where they will run.

## Model selection at execution time

Carry the core's user-validated homogeneous lot boundary and model choice into
each platform adaptation. Before execution, revalidate available models and override support
for the target runtime/account. Use its actual documented selection mechanism,
not a generic tool name or a prompt merely asking the worker to become a model.
Do not assume an alias or model identifier transfers between platforms or accounts.
If selection or required context isolation cannot be honored, ask for an explicit
alternative or inheritance decision; never silently substitute or relax reviewer
isolation. An unknown target platform leaves this gate pending, not auto-approved.

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
The model-selection and per-lot validation gate also remains unchanged; available
identifiers and the supported selection mechanism are runtime-specific.
