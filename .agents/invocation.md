# Dual-Harness Invocation Model (Claude Code, Codex, Hermes)

Every skill in this repository defines how it can be invoked: by a human user only, or autonomously by the agent model.

## 1. User-Invoked Skills

Reachable **only when explicitly triggered by a human** (e.g. typing `$audit-repository-acrazie` or `/skill-refiner-acrazie`).

Configuration:
- In `SKILL.md` frontmatter:
  ```yaml
  disable-model-invocation: true
  ```
- In `agents/openai.yaml`:
  ```yaml
  policy:
    allow_implicit_invocation: false
  ```
- Description: Human-facing concise summary of the action.

*Examples*: `audit-repository-acrazie`, `skill-refiner-acrazie`.

## 2. Model-Invoked Skills

Reachable **both autonomously by models and explicitly by users**.

Configuration:
- In `SKILL.md` frontmatter: omit `disable-model-invocation`.
- In `agents/openai.yaml`: omit `policy.allow_implicit_invocation` (or set to `true`).
- Description: Model-facing trigger phrases ("Use when the user wants to...").

*Examples*: `svg-icon-designer-acrazie`.

## 3. Consistency Invariant

Both harnesses must stay strictly synchronized:
- Never set `disable-model-invocation: true` in `SKILL.md` while leaving `policy.allow_implicit_invocation: true` in `openai.yaml`.
- Never disable model invocation in `openai.yaml` without mirroring it in `SKILL.md`.
