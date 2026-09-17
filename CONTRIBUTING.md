# Contributing to Acrazie Skills

Thank you for contributing to **Acrazie Skills**! This repository is a monorepo of specialized AI coding agent skills published to [skills.sh](https://skills.sh).

To ensure stability, reliability, and smooth parallel agent development, all contributions must adhere to the guidelines and invariants described below.

---

## Architecture of a Skill

Each skill lives in its own dedicated directory under `skills/` and owns one concrete workflow:

```text
skills/
└── <skill-name>-acrazie/
    ├── SKILL.md              # Authoritative instructions and YAML frontmatter
    ├── agents/
    │   └── openai.yaml       # Codex UI metadata and invocation policy
    ├── references/           # Detailed domain guides, schemas, recipes
    └── assets/               # Logos and vector icons (retro-tech palette)
```

### Core Invariants

1. **Naming**: Every skill directory and identifier must end with the author signature: `-acrazie` (e.g. `svg-icon-designer-acrazie`).
2. **Directory Structure**: Every skill must contain at least `SKILL.md` and `agents/openai.yaml`.
3. **Invocation Policy**: User-invoked skills require `disable-model-invocation: true` in `SKILL.md` frontmatter and `policy.allow_implicit_invocation: false` in `agents/openai.yaml`.
4. **Visual Identity**: Logos and marks use the Acrazie retro-tech design language (orange-to-violet `#ff6d00` to `#9d4edd`, southeast echoes).

---

## Development & Worktree Protocol

To allow concurrent development across multiple agents and developers without git conflicts, **all development MUST take place in an isolated Git worktree**. Never edit or commit skill files directly in the root workspace.

### Standard Worktree Lifecycle

1. **Provision a dedicated worktree**:
   ```bash
   git fetch origin main
   git worktree add .worktrees/<branch-name> -b <branch-name> origin/main
   cd .worktrees/<branch-name>
   ```

2. **Implement changes and validate locally**:
   ```bash
   # Validate frontmatter and mandatory fields
   ./scripts/hooks/validate-skills.sh skills/<skill-name>-acrazie/SKILL.md

   # Validate directory structure
   ./scripts/hooks/check-skill-structure.sh

   # Check that no forbidden or temporary files are staged
   ./scripts/hooks/check-forbidden-files.sh
   ```

3. **Stage and commit**:
   ```bash
   git add skills/<skill-name>-acrazie/
   git commit -m "feat(<skill-name>): clear description of changes"
   git push -u origin <branch-name>
   ```

4. **Open a Pull Request**:
   ```bash
   gh pr create --title "feat(<skill-name>): clear description" --body "..."
   ```

5. **Clean up worktree**:
   ```bash
   cd ../.. # return to repo root
   git worktree remove .worktrees/<branch-name>
   git worktree prune
   ```

---

## Commit Conventions

This project enforces [Conventional Commits](https://www.conventionalcommits.org/):

- `feat(<scope>): ...` — A new skill or new capability
- `fix(<scope>): ...` — A bug fix or instruction correction
- `docs(<scope>): ...` — Documentation or reference updates
- `chore(<scope>): ...` — Tooling, repository maintenance, or dependencies

### Co-Author Rule
**Never add co-author attributions** (`Co-authored-by: ...`) to commit messages.

### Automated Releases
Commits merged into `main` trigger [Release Please](https://github.com/google-github-actions/release-please-action), which automatically maintains the changelog, bumps semver tags, and creates GitHub releases. Pull requests should be **squash-merged** with a single Conventional Commit message.

---

## Local Testing & Symlinking

To test skills locally with agent runners (Hermes, Codex, Claude Code, Antigravity):
```bash
./scripts/link-skills.sh
```
This script symlinks all skills into your local agent configurations (`~/.hermes/skills/`, `~/.agents/skills/`, and `~/.gemini/config/skills/`).

---

## Hygiene & Forbidden Files

Never stage or commit internal refinement journals, cache files, or worktree folders:
- `.worktrees/`
- `.hermes/`, `.impeccable/`, `.skill-refiner/`, `.skill-improver/`
- `skills/*/docs/`
- Temporary preview HTML files (`assets/*-(preview|variants).html`)

These patterns are blocked automatically by pre-commit hooks configured via `lefthook.yml`.
