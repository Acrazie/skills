---
name: repo-modernizer-acrazie
description: Audit an existing repository setup, identify outdated tools, frameworks, and runtimes, and guide safe, step-by-step modernizations, upgrades, and paradigm shifts across 6 thematic pillars. Use only when explicitly invoked by the user; not for greenfield repository scaffolding or general code reviews.
disable-model-invocation: true
---

# Repo Modernizer / Acrazie

Audit an existing repository's setup, dependencies, runtimes, and developer tooling. Structure modernization opportunities into 6 thematic pillars and 3 ambition tiers, then guide safe, automated, step-by-step migrations with AI assistance, strict validation gates, and automatic rollback safeguards.

---

## 1. Invocation Guard

Run **only after explicit user invocation** (e.g. `$repo-modernizer-acrazie` or `/repo-modernizer-acrazie`).
If the harness activates this skill implicitly, do not start an audit or mutation; ask the user to explicitly invoke `$repo-modernizer-acrazie`.

---

## 2. Scope, Invariants & Hard Rules

1. **Brownfield Specialization & Complementarity with `github-repo-init-acrazie` :**
   - `github-repo-init-acrazie` operates at **Day 0** (scaffolding a brand-new repository from scratch).
   - `repo-modernizer-acrazie` operates at **Day 2+** (taking an existing repository, auditing its setup, modernizing legacy configurations to target the same modern standards, and offering to backfill missing bricks like CI workflows, Lefthook hooks, and governance files).
2. **Read-Only Inspection First :**
   - The initial scan must be strictly passive and non-destructive. Never modify files, install packages, or mutate git state during the diagnosis phase.
3. **Approval Gate Before Any Mutation :**
   - Present a structured **Modernization Scorecard** and obtain explicit user confirmation on the chosen pillar and tier before creating branches, installing tools, or refactoring code.
4. **Strict Git & Worktree Isolation :**
   - **NEVER** modify or commit files directly on `main` or the active working branch. Always perform migrations within a dedicated branch or worktree (`modernize/<theme>`).
5. **Layered Sequencing :**
   - Always order upgrades by logical layers:
     1. Runtime & Package Manager (e.g. Node, pnpm, uv)
     2. Developer Tooling & Quality (Linters, formatters, test runners, git hooks)
     3. Core Framework & Application (React, Next.js, FastAPI, Symfony...)
     4. Secondary & utility dependencies.
6. **Hybrid Refactoring Protocol :**
   - Run official, battle-tested migration tools and codemods first (e.g. `biome migrate`, `vitest-codemod`, `pyupgrade`, `rector process`).
   - Mobilize the AI to surgically translate complex configurations, adapt deprecated API calls, and update mocks/tests.
7. **Automated Validation Gates :**
   - Every modification must pass 4 verification gates: Lockfile integrity, Lint/Format, Typecheck, and Test Suite.
8. **AI Self-Healing & Automatic Rollback :**
   - If tests or build fail, the AI may attempt up to 3 targeted auto-repair iterations.
   - If failures persist after 3 attempts, the skill must execute an **automatic rollback** (`git reset --hard`) to the last green commit, provide a detailed diagnostic of the blocker, and prompt the user for arbitration.
9. **Atomic Conventional Commits & ADR Documentation :**
   - Create atomic commits using Conventional Commits (`build:`, `chore:`, `test:`, `feat:`). Never include co-author attributions (`Co-authored-by:`).
   - Any Tier 2 (Major) or Tier 3 (Modern Replacement) migration must generate a formal Architecture Decision Record under `docs/adr/`.

---

## 3. Workflow Overview

```mermaid
flowchart TD
  A["1. Passive Inspection (Read-only)"] --> B["2. Thematic Scorecard & 3-Tier Matrix"]
  B --> C["3. Interactive Scope & Tier Selection (Approval Gate)"]
  C -->|Approved| D["4. Provision Dedicated Branch / Worktree"]
  D --> E["5. Layered Migration (Codemod + AI Refactoring)"]
  E --> F["6. Automated Validation Gates (Build / Lint / Tests)"]
  F -->|Green| G["7. Atomic Conventional Commit & ADR Generation"]
  F -->|Red (<= 3 attempts)| E
  F -->|Red (> 3 attempts)| H["8. Automatic Rollback & Blocker Diagnostic"]
  G --> I["9. Next Pillar or Completion Summary"]
```

---

## 4. Step-by-Step Operating Guide

### Step 1: Passive Environmental Inspection
Read [references/inspection-checklist.md](references/inspection-checklist.md) before inspecting.
1. Check repository root, current git branch, and clean status (`git status --porcelain`).
2. Identify active manifests, lockfiles, and runtimes:
   - Node/JS/TS: `package.json`, lockfile type, `.nvmrc`, `tsconfig.json`.
   - Python: `pyproject.toml`, `requirements.txt`, `poetry.lock`, `uv.lock`.
   - Go / Rust / PHP: `go.mod`, `Cargo.toml`, `composer.json`.
3. Detect existing linters, formatters, bundlers, and test runners (`.eslintrc*`, `biome.json`, `webpack.config.*`, `vite.config.*`, `jest.config.*`, `vitest.config.*`).
4. Inspect CI/CD workflows under `.github/workflows/` and git hooks (`lefthook.yml`, `.husky/`).
5. Check for missing governance or DX assets compared to `github-repo-init-acrazie` standards.

---

### Step 2: Thematic Scorecard & 3-Tier Matrix
Read [references/taxonomy-matrix.md](references/taxonomy-matrix.md) and [references/modernization-catalog.md](references/modernization-catalog.md).
Structure findings across the 6 thematic pillars and present a compact Markdown table:

| Pilier | Outil Actuel | Statut / Version | Recommandation Tier 1 (Drop-in) | Recommandation Tier 2 (Majeur) | Recommandation Tier 3 (Remplacement Moderne) | Effort / Gain |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Runtime** | Node 18 | EOL proche | Node 20 LTS | Node 22 Current | - | Faible / Fiabilité |
| **Qualité & Lint** | ESLint legacy + Prettier | Format .eslintrc déprécié | Bump patch | ESLint 9 Flat Config | **Biome** (vitesse x25, zéro config) | Moyen / DX x10 |
| **Build & Bundler** | Webpack 4 / CRA | Build lent (>45s) | Bump Webpack 5 | - | **Vite** (HMR instantané, TS natif) | Modéré / Gain maximal |
| **Tests & QA** | Jest (`ts-jest`) | ESM complexe, lent | Jest 29 + SWC | - | **Vitest** (partage config Vite, x5 rapide) | Modéré / Vitesse |
| **CI/CD & DevOps** | GH Actions v2/v3, sans hooks | Actions dépréciées | Bump actions@v4 | - | **Lefthook** + **Release Please** | Faible / Automatisation |
| **Dépendances** | npm standard | Dépendances obsolètes | `npm update` (patch/minor) | Upgrades majeures ciblées | Migration vers **pnpm** ou **uv** | Modéré / Espace disque |

Highlight any **missing essential blocks** (e.g. no git hooks installed, no automated release pipeline, missing security policy).

---

### Step 3: Interactive Selection & Approval Gate
Ask the user which pillar and which ambition tier they wish to execute first.
If the user provided explicit scope upfront (e.g. `$repo-modernizer-acrazie --theme testing`), confirm the plan for that pillar.
Do **NOT** proceed to file modifications until the user explicitly selects and confirms the target plan.

---

### Step 4: Provision Dedicated Branch or Worktree
Read [references/execution-protocol.md](references/execution-protocol.md).
1. Ensure the workspace is clean.
2. If worktrees are supported in the repository:
   ```bash
   git worktree add .worktrees/modernize-<theme> -b modernize/<theme>
   cd .worktrees/modernize/<theme>
   ```
3. Otherwise, create a dedicated branch:
   ```bash
   git checkout -b modernize/<theme>
   ```

---

### Step 5: Execute Migration (Codemods + AI Refactoring)
Follow the layered ordering from [references/execution-protocol.md](references/execution-protocol.md):
1. **Run official codemods / migration CLI first** (e.g. `pnpm biome migrate eslint --write`, `npx vitest-codemod`, `uv init --bare`, `rector process`).
2. **Translate configuration files** (e.g. `vite.config.ts`, `biome.json`, `lefthook.yml`).
3. **Remove obsolete dependencies and configs** from package manifests.
4. **Refactor codebase call sites** via targeted AI edits (updating deprecated imports, mocks, and type annotations).

---

### Step 6: Automated Validation Gates & Self-Healing
Run the 4 validation gates in order:
1. `Lockfile & Install` : `pnpm install --frozen-lockfile` / `uv sync`
2. `Linter & Formatter` : `pnpm biome check .` / `uv run ruff check`
3. `Typecheck` : `pnpm tsc --noEmit` / `cargo check`
4. `Test Suite` : `pnpm test` / `uv run pytest`

**Self-Healing Loop :**
- If an error occurs, analyze the stack trace and apply targeted patches.
- Maximum 3 self-repair attempts allowed.
- If the suite is not 100% green after 3 attempts:
  - Run `git reset --hard HEAD` to revert to the last stable state.
  - Present a **Blocker Diagnostic Report** explaining the failure and request human arbitration.

---

### Step 7: Commit, ADR Documentation & Completion
1. Once all validation gates are green, stage changes and create an atomic Conventional Commit:
   ```bash
   git commit -m "chore(tooling): migrate from jest to vitest"
   ```
2. For Tier 2 and Tier 3 migrations, create a formal Architecture Decision Record under `docs/adr/YYYY-MM-DD-<title>.md` using [references/adr-template.md](references/adr-template.md).
3. If missing governance/CI bricks from `github-repo-init-acrazie` were backfilled, verify their validity.
4. Present a concise summary of the achievements, test execution metrics, and offer to proceed to the next pillar or open a Pull Request.
