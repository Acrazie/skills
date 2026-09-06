# Acrazie Skills — Agent Guidelines

Instructions and standards for AI coding agents (Hermes, Codex, Claude Code) working on this repository.

## Mission & Architecture

This repository is a monorepo of specialized agent skills published to [skills.sh](https://skills.sh).
Each skill owns one concrete workflow and maintains its instructions, UI metadata, and supporting references together.

Directory structure:
```text
skills/
├── <skill-name>-acrazie/
│   ├── SKILL.md              # Authoritative instructions and frontmatter
│   ├── agents/
│   │   └── openai.yaml       # Codex UI metadata and invocation policy
│   ├── references/           # Detailed domain guides, schemas, recipes
│   └── assets/               # Logos, visual references
```

## Hard Invariants

1. **Naming**:
   - Every skill directory and identifier must end with the author signature: `-acrazie` (e.g. `svg-icon-designer-acrazie`).
2. **Git & Commit Protocol**:
   - Never commit or push without explicit user authorization.
   - Use Conventional Commits (`feat:`, `fix:`, `chore:`, `docs:`) so `release-please` can generate changelogs and version bumps automatically.
3. **Artifact Isolation & Hygiene**:
   - Internal refinement journals belong in `<skill>/.skill-refiner/campaigns/YYYY-MM-DD-refinement-<N>.json`.
   - Never commit `.skill-refiner/`, `.skill-improver/`, `skills/*/docs/`, or temporary HTML previews. They are gitignored and blocked by Lefthook.
4. **Visual Identity**:
   - Logos follow the Acrazie retro-tech design language (modular lettering, orange-to-violet palette `#ff6d00` to `#9d4edd`, southeast echoes).
   - Metaphors must be cleanly integrated into letterforms without lookalike glitches or detached noise.
5. **Invocation Model**:
   - User-invoked skills require `disable-model-invocation: true` in `SKILL.md` frontmatter and `policy.allow_implicit_invocation: false` in `agents/openai.yaml`.
   - Read `.agents/invocation.md` for complete rules.

## Local Development

- Run `scripts/link-skills.sh` to symlink all repository skills into `~/.hermes/skills/` and `~/.agents/skills/`.
- Pre-commit and pre-push validations are configured via `lefthook.yml`.
