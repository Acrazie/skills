---
name: repo-modernizer-acrazie
description: Audit an existing repository setup, identify outdated tools, frameworks, and runtimes, and guide safe, step-by-step modernizations, upgrades, and paradigm shifts across 6 thematic pillars. Use when the user requests upgrades or modernization of an existing repository; not for opportunistic modernization during another task, greenfield scaffolding, or general code reviews.
---

# Repo Modernizer / Acrazie

Audit an existing repository's setup, dependencies, runtimes, and developer tooling. Structure modernization opportunities into 6 thematic pillars and 3 ambition tiers, then guide safe, automated, step-by-step migrations with AI assistance, strict validation gates, and approval-gated rollback safeguards.

---

## Portable evidence and outputs

Read [references/portable-practice.md](references/portable-practice.md) before
starting this workflow. At each execution, verify changing technical facts used
for decisions or actions against official documentation for the project or target
version, not automatically the latest. Record sources, versions and limits;
inaccessible or contradictory documentation blocks only the dependent step, not
independent work. Model memory is not a substitute for missing proof.
Use the four-field choice format with numbered options and exactly one motivated
recommendation, never prefilled consent. Include Decisions, Evidence and Limits
in the final handoff or report alongside the existing domain-specific sections.
These rules are local to this skill and do not require the repository's AGENTS.md.

## Project loading boundary

Published-library defaults remain model-invocable within the requested task. An
explicit project kit or stricter current instruction takes precedence: propose
this skill from available metadata and wait for the user's explicit command before
reading its instructions. Apply the same gate to each dependency before reading
or dispatching its instructions; one invocation does not activate a chain.
Use `$skill-name` in Codex or `/skill-name` in Claude Code. These gates are not
filesystem access controls or proof of live host behavior. Global homonyms may
remain a blocker. Do not read an unactivated skill or delegate its body as a bypass.
Loading grants no migration, installation, spawning, shipping or recovery permission.
Under ordinary library defaults retain scoped implicit handoffs. Conceptual
references to Repo Init's standards are not a mandatory skill dependency and do
not authorize reading or invoking it; this workflow keeps its specialist interview.

## User decision format

For any user-owned choice, display only Current state, numbered Options,
Recommendation and Response. Provide exactly one recommendation with a short
context-specific reason, using the template in the local portable-practice reference.
Translate labels/content into the user's language;
do not add question IDs, preselect an answer as consent or treat a recommendation
as approval. Apply this to pillar/tier, plan, installation, governance, Git and
recovery decisions. The scorecard, validation evidence and reports retain their
own structures; do not replace them with the question format.

## 1. Entry and Authorization

Select this skill for requested upgrades or repository modernization. Under published defaults no named skill command is required; the project loading boundary governs explicit kits. Start with relevant read-only discovery, limited to the requested target. Do not turn a bug fix or feature into an opportunistic modernization program. Selection does not approve migration, installation, shipping, or destructive recovery; follow the gates below and applicable repository permissions.

---

## 2. Scope, Invariants & Hard Rules

1. **Brownfield Specialization & Complementarity with `github-repo-init-acrazie` :**
   - `github-repo-init-acrazie` owns new-repository scaffolding and approved engineering activation in existing repositories, preserving their stack. Activating a kit is not a stack migration.
   - `repo-modernizer-acrazie` operates at **Day 2+** (taking an existing repository, auditing its setup, modernizing legacy configurations to target the same modern standards, and offering to backfill missing bricks like CI workflows, Lefthook hooks, and governance files).
2. **Read-Only Inspection First :**
   - The initial scan must be strictly passive and non-destructive. Never modify files, install packages, or mutate git state during the diagnosis phase.
3. **Approval Gate Before Any Mutation :**
   - Present a structured **Modernization Scorecard** and obtain explicit user confirmation on the chosen pillar, tier and plan before migration; reuse independently evidenced current approval as described in Step 3. Branch/worktree creation and installation retain their applicable separate permissions.
4. **Strict Git & Worktree Isolation :**
   - **NEVER** modify or commit files directly on `main` or the active working branch. Always perform migrations within a dedicated branch or worktree using the repository-approved naming and isolation rules. Treat `modernize/<theme>` as an example, not an imposed prefix.
5. **Layered Sequencing :**
   - Plan upgrades by logical layers; group inseparable cross-layer changes into one validated commit rather than producing broken intermediate commits:
     1. Runtime & Package Manager (e.g. Node, pnpm, uv)
     2. Developer Tooling & Quality (Linters, formatters, test runners, git hooks)
     3. Core Framework & Application (React, Next.js, FastAPI, Symfony...)
     4. Secondary & utility dependencies.
6. **Hybrid Refactoring Protocol :**
   - Prefer applicable official migration tools and codemods after verifying their version support, documented invocation, effects and coverage; do not assume a tool exists or fully preserves semantics.
   - Mobilize the AI to surgically translate complex configurations, adapt deprecated API calls, and update mocks/tests.
7. **Automated Validation Gates :**
   - Every modification must pass 4 verification gates: Lockfile integrity, Lint/Format, Typecheck, and Test Suite.
8. **AI Self-Healing & Approval-Gated Rollback :**
   - If tests or build fail, the AI may attempt up to 3 targeted auto-repair iterations.
   - Record the SHA and validation evidence for each verified green checkpoint. If failures persist after 3 attempts, stop, preserve the current state, and provide a blocker diagnostic referencing that checkpoint (or explicitly state that none exists). Never infer that `HEAD` is green. For recovery, obtain separate explicit confirmation before destructive rollback, specifying the affected paths, target revision, and consequences; migration approval is not recovery permission.
9. **Mandatory Approved Commit Strategy & ADR Documentation :**
   - Discover existing Git policy, resolve conflicts, and approve the migration commit plan before execution. Read [references/commit-strategy.md](references/commit-strategy.md). Follow the approved strategy before every commit; block non-compliance instead of silently relaxing it. Conventional Commits are an option, not a universal requirement. Never include co-author attributions (`Co-authored-by:`).
   - Control compliance even without hooks or CI; installing enforcement tools and changing remote settings are separate opt-in actions. Commit, push, and PR permissions remain distinct.
   - Any Tier 2 (Major) or Tier 3 (Modern Replacement) migration must generate its formal Architecture Decision Record under `docs/adr/` before validation and the corresponding commit.

---

## 3. Workflow Overview

```mermaid
flowchart TD
  A["1. Passive Inspection (Read-only)"] --> B["2. Thematic Scorecard & 3-Tier Matrix"]
  B --> C["3. Scope, Tier & Commit Strategy Approval"]
  C -->|Approved| D["4. Provision Dedicated Branch / Worktree"]
  D --> E["5. Layered Migration (Codemod + AI Refactoring)"]
  E --> F["6. Automated Validation Gates (Build / Lint / Tests)"]
  F -->|Green| G["7. Strategy Compliance & Authorized Atomic Commit"]
  F -->|Red, repairs remaining| E
  F -->|Red after 3 repairs| H["8. Stop, Diagnose & Request Recovery Approval"]
  G --> I["9. Next Pillar or Completion Summary"]
```

---

## 4. Step-by-Step Operating Guide

### Step 1: Passive Environmental Inspection
Read [references/inspection-checklist.md](references/inspection-checklist.md) before inspecting.
1. Check repository root, current git branch, index and working-tree state using verified read-only inspection.
2. Identify active manifests, lockfiles, and runtimes:
   - Node/JS/TS: `package.json`, lockfile type, `.nvmrc`, `tsconfig.json`.
   - Python: `pyproject.toml`, `requirements.txt`, `poetry.lock`, `uv.lock`.
   - Go / Rust / PHP: `go.mod`, `Cargo.toml`, `composer.json`.
3. Detect existing linters, formatters, bundlers, and test runners (`.eslintrc*`, `biome.json`, `webpack.config.*`, `vite.config.*`, `jest.config.*`, `vitest.config.*`).
4. Inspect CI/CD workflows under `.github/workflows/` and git hooks (`lefthook.yml`, `.husky/`). Inspect Git governance, recent commit messages, release constraints, and accessible remote protections as detailed in [references/commit-strategy.md](references/commit-strategy.md); distinguish inaccessible rules from absent rules.
5. Check for missing governance or DX assets compared to `github-repo-init-acrazie` standards.

---

### Step 2: Thematic Scorecard & 3-Tier Matrix
Read [references/taxonomy-matrix.md](references/taxonomy-matrix.md) and [references/modernization-catalog.md](references/modernization-catalog.md).
Structure findings across the 6 thematic pillars and present a compact Markdown table:

| Pillar | Observed tool / version | Verified status and source | Tier 1 candidate | Tier 2 candidate | Tier 3 candidate | Effort / measured benefit / limits |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `<detected pillar>` | `<local evidence>` | `<version-matched documentation or unverified>` | `<maintenance path, or not applicable>` | `<major path, or not applicable>` | `<replacement, or not justified>` | `<project evidence; unknown if not measured>` |

This is a structural template, not a predetermined tool ranking. Keeping the
existing setup is valid. Do not invent a candidate for every tier or infer
obsolescence from age, a filename, or absence of a preferred tool. Include source,
version applicability and limits for each changing claim. Highlight missing blocks
only when their value or requirement is established for this repository.

---

### Step 3: Interactive Selection & Approval Gate
Reuse an explicitly approved migration plan when pillar, tier, scope, exclusions,
commit strategy and required validations remain applicable, with approval evidence
beyond a status label. Revalidate repository facts and required checks; an approved
plan is not evidence of a green checkpoint. Do not repeat settled choices or
require Interview/Git Ship to recreate this specialist's plan. If new evidence
invalidates it, reopen only affected decisions before the dependent execution.
Plan reuse does not grant loading, installation, staging/commit/push/PR or
destructive recovery permissions; evaluate those independently at their boundaries.

Ask the user only unresolved pillar and ambition-tier choices.
If the user provided explicit scope upfront (e.g. modernization of testing only), confirm the plan for that pillar.
Include the approved commit strategy and proposed commit boundaries in that plan. Preserve existing policy; ask only unresolved choices. If policy is missing, propose `docs/git-workflow.md` and obtain approval before creating it, keeping existing `AGENTS.md` and `CONTRIBUTING.md` consistent without overwriting them. Hooks, dependencies, and GitHub settings require separate choices.
Do **NOT** proceed to file modifications without independently evidenced explicit approval covering the current target plan and realization, including its commit strategy. An unresolved policy conflict blocks the affected execution.

---

### Step 4: Provision Dedicated Branch or Worktree
Read [references/execution-protocol.md](references/execution-protocol.md).
1. Verify the repository root, branch, index, and working-tree state. Preserve unrelated changes; never stash, commit, or discard them implicitly.
2. Provision the approved isolated branch/worktree according to repository policy, using the chosen base, branch name, and path. Respect required worktrees and forbidden branches. If the remote base cannot be refreshed, stop and ask before offline execution; never silently fall back to a stale base.
3. Run the agreed baseline validations and record the SHA with their results as the initial checkpoint only if they pass. If no verified checkpoint exists, report that fact and arbitrate before migration.

---

### Step 5: Execute Migration (Codemods + AI Refactoring)
Follow the layered ordering from [references/execution-protocol.md](references/execution-protocol.md):
1. **Prefer a documented applicable migration tool** after checking source/target support, invocation, mutation scope and limitations. If none is verified, plan bounded manual changes; do not install or run a guessed command.
2. **Translate configuration files** (e.g. `vite.config.ts`, `biome.json`, `lefthook.yml`).
3. **Remove obsolete dependencies and configs** from package manifests.
4. **Refactor codebase call sites** via targeted AI edits (updating deprecated imports, mocks, and type annotations).
5. Prepare required ADRs and governance changes within the same coherent unit before validation. Follow approved commit boundaries, not an automatic one-commit-per-tool rule.

---

### Step 6: Automated Validation Gates & Self-Healing
Use verified actual repository commands for the 4 validation gates in order; the gate descriptions below are not tool installation instructions. Missing, unavailable, or failing required checks block the commit. A genuinely inapplicable gate needs an explicit reason in the approved plan, never an invented success:
1. `Lockfile & Install`: verified repository command and lockfile-preservation expectations.
2. `Linter & Formatter`: verified repository checks, with write effects disclosed.
3. `Typecheck`: verified applicable static-analysis command.
4. `Test Suite`: verified repository suite and agreed acceptance criteria.

Derive exact commands from repository configuration and version-matched official
documentation before use; these gate names are not executable recipes.

**Self-Healing Loop :**
- If an error occurs, analyze the stack trace and apply targeted patches.
- Maximum 3 self-repair attempts allowed.
- If the suite is not 100% green after 3 attempts:
  - Stop, preserve the current state, and present a **Blocker Diagnostic Report** with the failing command, evidence, repair count, and recorded verified checkpoint SHA (or its absence).
  - Inspect and preserve unrelated changes; show exact affected paths and target revision. Obtain separate explicit confirmation before any destructive reset or cleanup. If declined, preserve the current state and await arbitration.

---

### Step 7: Commit, ADR Documentation & Completion
1. Follow [references/commit-strategy.md](references/commit-strategy.md): verify authorization, exact staged scope, coherent boundaries, the selected message convention, and validation evidence for the staged snapshot. Include required ADRs prepared in Step 5. Any failed or unresolved check blocks the commit; do not bypass hooks or weaken policy.
2. Commit only if authorized by applicable user/repository rules; otherwise present the reviewed scope, proposed message, and proof and request approval. Approval of migration or policy alone grants no shipping authority.
3. After a successful commit, record its SHA with validation evidence as a checkpoint. If hooks changed files, recheck scope and validation before marking that revision green.
4. Summarize achieved migration units, compliance, checkpoint SHAs, and actual checks. Apply push and PR permissions separately; do not infer them from commit permission. Distinguish local validation, pending CI, PR state, and deployment. Offer the next pillar or PR only within the authorized scope.

## Repository CI/CD ownership

For substantive CI/CD work beyond minimal bootstrap, propose `ci-cd-acrazie`;
apply its project loading boundary before reading or handing off implementation.
Minimal bootstrap reuses an established simple template with existing decisions;
new provider integration, release/promotion architecture or causal pipeline repair
belongs to the CI/CD owner. Modernization may inspect and plan CI/CD globally,
but does not implement a competing substantive pipeline workflow. Pass the current
approved contract, decisions, evidence and allowed actions; do not repeat settled
interviews or infer recipient activation, remote actions or Git shipping permission.
