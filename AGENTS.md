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
2. **Git, Worktrees & Parallel Development Protocol**:
   - **Worktree Isolation**:
     - All skill additions, refactoring, evaluations, and updates **MUST** take place within an isolated Git worktree located at `.worktrees/<branch-name>`.
     - Agents must **NEVER** edit, generate, or stage skill files directly in the root repository workspace. Working inside isolated worktrees guarantees that multiple agents and concurrent sessions can develop or update different skills in parallel without branch conflicts or dirty working tree collisions.
   - **Autonomous Git Permissions**:
     - The agent is authorized to autonomously perform routine Git operations on dedicated branches: creating worktrees (`git worktree add`), staging (`git add`), creating commits, pushing branches (`git push -u origin <branch>`), and opening Pull Requests via `gh pr create`.
     - Sensitive or destructive Git operations still require explicit user confirmation (e.g. force-pushing `git push --force`, hard reset `git reset --hard`, branch deletion, or direct pushes to protected branches like `main`).
   - **Commit Conventions**:
     - Use Conventional Commits (`feat:`, `fix:`, `chore:`, `docs:`) so `release-please` can generate changelogs and version bumps automatically.
     - Never add co-author attributions (`Co-authored-by:`) to commit messages.
   - **Mandatory PR Workflow**:
     - All material changes (adding, updating, or deleting a skill) must go through a dedicated branch and Pull Request. Direct commits or pushes to `main` are strictly forbidden (except for emergency hotfixes or automated release PRs).
     - PRs should be **squash-merged** into `main` using a single Conventional Commit message (e.g. `feat(jenkins-go): add go specialist skill`).
     - Release Please tracks commits on `main` and manages the release PR + version tag.
   - **Standard Worktree Lifecycle**:
     ```bash
     # 1. Fetch latest main and provision dedicated worktree
     git fetch origin main
     git worktree add .worktrees/<branch-name> -b <branch-name> origin/main

     # 2. Navigate into worktree and perform work
     cd .worktrees/<branch-name>

     # 3. Validate changes with repository hooks
     ./scripts/hooks/validate-skills.sh skills/<skill>/SKILL.md
     ./scripts/hooks/check-skill-structure.sh

     # 4. Commit and push from worktree
     git add skills/<skill>/
     git commit -m "feat(<skill>): description"
     git push -u origin <branch-name>

     # 5. Open Pull Request
     gh pr create --title "feat(<skill>): description" --body "..."

     # 6. Teardown worktree once work is complete / PR opened
     cd <repo-root>
     git worktree remove .worktrees/<branch-name>
     git worktree prune
     ```
3. **Artifact Isolation & Hygiene**:
   - Internal refinement journals belong in `<skill>/.skill-refiner/campaigns/YYYY-MM-DD-refinement-<N>.json`.
   - Never commit `.worktrees/`, `.hermes/`, `.skill-refiner/`, `.skill-improver/`, `.impeccable/`, `skills/*/docs/`, or temporary HTML previews. They are gitignored and blocked by Lefthook.
4. **Visual Identity**:
   - Logos follow the Acrazie retro-tech design language (modular lettering, orange-to-violet palette `#ff6d00` to `#9d4edd`, southeast echoes).
   - Metaphors must be cleanly integrated into letterforms without lookalike glitches or detached noise.
5. **Invocation Model**:
   - User-invoked skills require `disable-model-invocation: true` in `SKILL.md` frontmatter and `policy.allow_implicit_invocation: false` in `agents/openai.yaml`.
   - Read `.agents/invocation.md` for complete rules.

## Local Development

- Run `scripts/link-skills.sh` to symlink all repository skills into `~/.hermes/skills/` and `~/.agents/skills/`.
- Pre-commit and pre-push validations are configured via `lefthook.yml`.

## Cross-Agent Compatibility

`AGENTS.md` is the universal instruction file. To support harnesses that look for legacy or harness-specific files:
- `CLAUDE.md` is maintained as a symlink to `AGENTS.md` for Claude Code.
- Codex, OpenCode, and Hermes natively read `AGENTS.md` directly.
- Cursor and Windsurf map rules via `.cursorrules` / `.windsurfrules` (or import from `AGENTS.md`).

