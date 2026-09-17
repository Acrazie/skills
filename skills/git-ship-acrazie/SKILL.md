---
name: git-ship-acrazie
description: Finalize, commit, push, and open Pull Requests for completed tasks based on repository Git rules and governance. Use when explicitly invoked by the user to ship changes, commit completed work, publish a branch, or create a draft PR.
disable-model-invocation: true
---

# Git Ship / Acrazie

Safely finalize a completed task by validating repository hygiene, enforcing governance rules, creating a Conventional Commit, pushing the feature branch, and opening a Pull Request (defaulting to Draft).

---

## 1. Invocation Guard & Autonomy Boundaries

- **Invocation Mode**: Explicit user invocation only (`/git-ship-acrazie`, `$git-ship-acrazie`, or explicit instruction to ship/commit current task).
- **Semi-Autonomous Execution with Approval Gate**:
  - The agent autonomously conducts discovery, runs pre-flight quality gates, drafts the commit message, and prepares the PR description.
  - **Hard Invariant (Approval Gate)**: The agent must **NEVER** run `git commit`, `git push`, or `gh pr create` without first presenting the consolidated delivery recap and receiving explicit user confirmation ("Go" or adjustments).

---

## 2. Core Invariants

1. **Rule Discovery & Strict Fallback**:
   - Inspect `docs/git-workflow.md` (or pointers in `AGENTS.md` / `CONTRIBUTING.md`) before taking any action.
   - If NO git governance or delivery rules exist on the repository: **HALT** and offer to invoke `github-repo-init-acrazie` to initialize the repository rules. Do not invent arbitrary rules.
2. **Branch Protection**:
   - Never commit or push directly to `main` or `master`. If on the default branch, halt and offer to create a feature branch or dedicated worktree.
3. **Zero Secret Leaks**:
   - Never stage `.env*`, credentials, private keys, or transient development artifacts (`.worktrees/`, cache directories).
4. **Conventional Commits**:
   - All commits must strictly follow Conventional Commits (`feat:`, `fix:`, `chore:`, `docs:`, `refactor:`, `test:`).
5. **No Co-Author Attributions**:
   - **HARD INVARIANT**: Never add `Co-authored-by:` or any automated co-author trailer to commit messages.
6. **PR Defaults**:
   - Pull Requests default to **Draft** mode (`gh pr create --draft`) for review safety, unless the user explicitly requests a ready-to-review PR.
   - Pull Requests must follow the repository template (`.github/pull_request_template.md`).

---

## 3. Workflow Overview

```mermaid
flowchart TD
  A["1. User Invocation ($git-ship-acrazie)"] --> B["2. Discover Governance (docs/git-workflow.md)"]
  B -->|Rules Missing| C["Offer /github-repo-init-acrazie"]
  B -->|Rules Present| D["3. Pre-Flight Safety & Quality Gates"]
  D -->|Failed (main branch or dirty secrets)| E["Halt & Guide User"]
  D -->|Passed| F["4. Synthesize Recap (Diff, Commit, PR Draft)"]
  F --> G{"5. Approval Gate: Wait for 'Go'"}
  G -->|Go| H["6. Execute: Stage -> Commit -> Push -> gh pr create"]
  G -->|Adjustments| F
  H --> I["7. Delivery Report & PR Link"]
```

---

## 4. Step-by-Step Procedure

### Step 1: Discover Repository Governance & Rules
Read [references/inspection.md](references/inspection.md).
1. Check for `docs/git-workflow.md`:
   - If present, read and extract branching policies, commit formats, quality gate commands, worktree guidelines, and PR rules.
2. If absent, check `AGENTS.md` and `CONTRIBUTING.md` for a referenced git workflow document.
3. **Fallback Condition**:
   - If no delivery rules or git workflow documentation exist:
     - Stop execution immediately.
     - Display:
       > "⚠️ **Aucune règle de gouvernance Git trouvée** (`docs/git-workflow.md` manquant)."
       > "Souhaitez-vous invoquer `/github-repo-init-acrazie` pour configurer le dépôt, établir les conventions de commit, les quality gates et le workflow de PR ?"
     - End turn and await user decision.

### Step 2: Pre-Flight Safety & Quality Checks
Read [references/pre-flight.md](references/pre-flight.md).
1. **Branch Check**:
   - Run `git branch --show-current`.
   - If on `main` or `master`:
     - Halt immediately.
     - Warn that direct commits to the default branch violate repository policy.
     - Propose creating a new feature branch (`feat/<topic>`) or provisioning a worktree (`.worktrees/<topic>`).
2. **Hygiene & Secrets Audit**:
   - Run `git status -s` and inspect untracked and modified files.
   - Flag any sensitive or transient files: `.env*`, `*.key`, `*.pem`, `.worktrees/`, IDE files, or debug logs.
   - Ensure these files are excluded from staging and added to `.gitignore` if needed.
3. **Quality Gates Verification**:
   - Run the pre-commit quality gate command defined in `docs/git-workflow.md` (e.g. `npx lefthook run pre-commit`, `pnpm test`, or repository linters).
   - If quality checks fail, report the exact errors and stop. Do not commit failing code unless explicitly commanded with a waiver. Never pass `--no-verify`.

### Step 3: Synthesize Delivery Plan & Approval Gate
Read [references/pr-delivery.md](references/pr-delivery.md).
1. Inspect the staged / modified diff (`git diff HEAD`).
2. Draft a precise Conventional Commit message:
   - Determine type (`feat`, `fix`, `chore`, `docs`, `refactor`, `test`).
   - Identify scope (e.g. `feat(auth): add OAuth2 refresh token handling`).
   - Write concise summary in imperative mood.
   - Verify NO `Co-authored-by:` line exists.
3. Draft the Pull Request:
   - Title: matches the Conventional Commit title.
   - State: **Draft** (`--draft`) by default.
   - Body: fill `.github/pull_request_template.md` sections (Summary, Changes list, Test plan, Checklist).
4. **Present the Delivery Recap**:
   ```markdown
   ### 📦 Récapitulatif de livraison (git-ship)

   - **Branche** : `<current-branch>` ➔ `origin/<current-branch>`
   - **Fichiers ciblés** :
     - `path/to/file1`
     - `path/to/file2`
   - **Message de commit proposé** :
     ```text
     <type>(<scope>): <description>
     ```
   - **Pull Request proposée** :
     - **Titre** : `<type>(<scope>): <description>`
     - **Mode** : Draft PR (`--draft`)
     - **Corps** :
       [Aperçu du corps basé sur le template]

   ---
   👉 **Attente de confirmation** : Tapez **"Go"** pour effectuer le commit, le push et ouvrir la Draft PR, ou indiquez vos ajustements.
   ```
5. **Stop and wait for user response**. Do NOT proceed without confirmation.

### Step 4: Execute Delivery upon "Go"
1. **Targeted Staging**:
   - Stage ONLY the files relevant to the completed task:
     ```bash
     git add <file1> <file2> ...
     ```
   - Never run blanket `git add .` if untracked files or scratch artifacts exist.
2. **Commit**:
   ```bash
   git commit -m "<commit-message>"
   ```
3. **Push with Upstream Tracking**:
   ```bash
   git push -u origin <current-branch>
   ```
4. **Create Pull Request**:
   ```bash
   gh pr create --draft --title "<pr-title>" --body "<pr-body>"
   ```
   *(Omit `--draft` only if the user explicitly asked for a ready-to-review PR).*
5. **Final Delivery Report**:
   - Output the commit hash, remote branch URL, and the created Pull Request URL.
   - Provide next steps (e.g., CI workflow tracking or review request).
