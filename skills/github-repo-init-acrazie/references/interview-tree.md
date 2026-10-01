# Adaptive GitHub Repository Initialization Interview Tree

Use this decision map to interview the user adaptively before any scaffolding occurs. Do not treat this as an inflexible robotic questionnaire; skip decisions that the user has already made explicit or that are constrained by existing facts discovered during Step 1. Present questions grouped into at most **2 to 3 progressive rounds**, where every question includes an explicit, contextual recommendation with rationale.

---

## 1. Ground Rules & Sequence

1. **Deep Discovery First (DEC-001)**:
   - Before asking questions, inspect the current working directory, git state, and configuration files.
   - Inspect applicable organization/repository rules, remote branch protection and merge settings when accessible, hooks, and relevant available Git skills. Record the exact source of each rule; do not treat an installed skill as automatically invoked or authoritative over the repository.
   - For each material conflict, show the competing rules, sources, and practical consequence. Ask the user to preserve the existing rule, adapt the proposed policy, approve a specific configuration/skill change, or omit that policy area. Do not proceed with the affected area until resolved. Never modify an external skill or configuration by implication.
   - If the repository is already populated or initialized, settle known decisions as established facts and prune redundant questions according to the table below.
2. **Progressive Rounds (DEC-002)**:
   - Never dump all interview themes in a single monolithic questionnaire. Structure the interaction into at most 2 to 3 logical rounds (Identity & Stack -> Quality & CI/CD -> Workflow & DX).
3. **Current Discovery, Not Template Defaults**:
   - Read [tool-selection.md](tool-selection.md) before each unresolved package/library/tool choice; use current official evidence and include retaining the current approach or no dependency. Preserve settled choices.
   - Read [github-settings.md](github-settings.md) before proposing Git/GitHub configuration; inventory relevant setting families and access/plan/organization limits, not only `gh repo create` flags.
4. **Always Recommend with Rationale**:
   - For every question asked, state available options and provide an explicit recommended default with a concise justification.
5. **Shared Blueprint Approval (DEC-003)**:
   - When all rounds are completed, synthesize a single **Initialization Blueprint** (bulleted summary + visual ASCII directory structure) and require explicit user sign-off before executing any mutating shell commands or writing files.

---

### Automated Pruning Rules

| Artifact / Environment Detected | Established Fact | Pruned Interview Questions |
|---|---|---|
| `pyproject.toml`, `requirements.txt`, `Pipfile` | Stack is **Python** | Do NOT ask between JS/TS, Python, Go, Rust. Preserve detected package manager/tools; research only unresolved choices. |
| `package.json`, `tsconfig.json` | Stack is **TypeScript/JavaScript** | Do NOT ask between JS/TS, Python, Go, Rust. Preserve detected package manager/tools; research only unresolved choices. |
| `go.mod` | Stack is **Go** | Do NOT ask for general stack choice. Preserve detected tooling; research unresolved quality-tool choices. |
| `Cargo.toml` | Stack is **Rust** | Do NOT ask for general stack choice. Preserve detected tooling; research unresolved quality-tool choices. |
| `git remote -v` contains `origin` | Remote repository already exists | Do NOT ask to create a new remote with `gh repo create`. Just confirm keeping `origin`. |
| `.github/workflows/ci.yml` exists | CI workflow already configured | Do NOT ask if CI is needed. Ask whether to standardize / upgrade existing CI. |
| `biome.json*`, `eslint.config.*`, `.eslintrc*`, `.prettierrc*`, `prettier.config.*`, `.oxlintrc.json`, `oxlint.config.*`, `.oxfmtrc.json*`, `oxfmt.config.*`, `ruff.toml`, manifest tool sections/scripts | Linter/formatter already chosen | Do NOT ask to choose between linters. Propose keeping current tool. |
| Directory non-empty & git initialized | Target path is current repo (`.`) | Do NOT ask to create a new subfolder unless explicitly requested. |

---

## 2. Progressive 3-Round Interview Tree

### Round 1: Repository Identity, Destination & Stack

#### 1.1 Target Path
- **Question**: Should the repository be initialized in the current working directory (`.`) or in a new subfolder (`./<repo-name>`)?
- **Options**: Current directory (`.`) | New subfolder (`./<repo-name>`).
- **Recommendation**: Current directory (`.`) if already named after the project; subfolder otherwise.
- **Pruning Rule**: Prune if the working directory is already an initialized project or if the user explicitly specified the path.

#### 1.2 Repository Name & Description
- **Question**: What is the project / repository name and a one-line description?
- **Options**: Freeform text.
- **Recommendation**: Default to the current directory name or manifest name (e.g. `name` field in `package.json` / `pyproject.toml`).
- **Pruning Rule**: Prune if manifest or directory name already provides an unambiguous name.

#### 1.3 Remote GitHub Repository
- **Question**: Do you want to create and connect a remote repository on GitHub right away, or keep it local-only?
- **Options**: Local git repository only | Remote GitHub repository: **Public** | Remote GitHub repository: **Private**.
- **Recommendation**: Private GitHub remote if `gh auth status` is authenticated and project is private; Public if intended for open-source; Local only if `gh` is unauthenticated.
- **Pruning Rule**: If `git remote -v` already lists an active `origin` remote, do NOT offer `gh repo create`. Ask only whether to keep or replace the existing remote.

#### 1.4 Stack Preset & Package Manager
- **Question**: Which technology stack and package manager do you want to use?
- **Options**:
  - TypeScript / JavaScript (React Vite, Vue Vite, Next.js, Node CLI/tsup) with `pnpm` / `npm` / `bun`.
  - Python (FastAPI, CLI, Library) with `uv` (recommended) or `poetry`.
  - Go module (`go mod init`) with standard Go tooling.
  - Rust binary or library (`cargo`) with Cargo.
  - Custom / Stack-Agnostic (empty skeleton or custom command).
- **Recommendation**: Research current stack-compatible options first; justify runtime/package-manager/scaffold choices from project constraints. Preserve authoritative manifests and explicit choices.
- **Pruning Rule**: Prune entirely if an authoritative manifest (`pyproject.toml`, `package.json`, `go.mod`, `Cargo.toml`) was detected during Step 1.

---

### Round 2: Code Quality Gates, CI/CD & Governance

#### 2.1 Git Hooks Manager
- **Question**: Which Git hook manager would you like to configure?
- **Options**: **Lefthook** | Husky | pre-commit | None.
- **Recommendation**: Compare current compatible managers and no-hooks mode. Lefthook is one language-agnostic candidate; verify installation/runtime and integration costs before recommending.
- **Pruning Rule**: Prune if `lefthook.yml`, `.husky/`, or `.pre-commit-config.yaml` is already present.

#### 2.2 Linter & Formatter
- **Question**: Which linter and code formatter should be configured?
- **Options**:
  - *JS/TS*: **Oxlint + Oxfmt**, **Biome**, **ESLint + Prettier**, and other credible candidates discovered from current official sources. Verify required rules/plugins, type-aware checks, framework syntax, formats and editor/CI support; do not assume one replaces all others.
  - *Python*: Ruff vs Black/Flake8 and other currently relevant candidates; verify required coverage and runtime compatibility.
  - *Go*: `golangci-lint` + `gofmt`.
  - *Rust*: `clippy` + `rustfmt`.
- **Recommendation**: Derive one contextual recommendation from the current comparison, not a fixed winner. Separate upstream benchmark claims from comparable observed results; no unsourced speed multiplier. Research other stacks and all other tooling choices with the same method.
- **Pruning Rule**: Prune if already configured in existing repo files.

#### 2.3 Commit Linting & Conventions
- **Question**: Which existing or new commit-message convention should apply, and should a commit-msg hook enforce it?
- **Options**: Preserve existing convention | Conventional Commits | another specified format | no enforced format. Hook or manual review as a separate choice.
- **Recommendation**: Preserve any enforced convention. For a new repository using automated releases, consider Conventional Commits; do not choose it merely because the template contains it.
- **Ecosystem Fit Invariant (DEC-004)**: Never install Node.js/npm dependencies in a non-JS project solely for commitlint. Always configure Lefthook's native regex hook or repository-local scripts for Python, Go, and Rust.

#### 2.4 CI/CD Workflows (GitHub Actions)
- **Question**: Which automated GitHub Actions workflows do you want to enable?
- **Options**:
  - Automated CI (`.github/workflows/ci.yml`: lint, typecheck, test, build).
  - Automated Releases: Release Please | Changesets | Tag-based | None | other current compatible options.
  - Security & Dependency audits: Dependabot (`.github/dependabot.yml`) | None.
- **Recommendation**: Compare current options against deployment/release needs and selected commit policy. Check Actions enablement/allow-list, `GITHUB_TOKEN` job scopes and whether automation may create PRs; do not assume a workflow file grants those permissions.
- **Pruning Rule**: If `.github/workflows/ci.yml` or `release-please.yml` already exists, offer to update/standardize instead of asking whether to create them from scratch.

#### 2.5 GitHub Settings & Permissions
- **Question**: Which relevant repository options from the discovered inventory should be preserved, configured or deferred?
- **Options**: Access/teams; Actions defaults, allowed actions and fork policy; branch/tag rulesets and checks/reviews; merge controls; security/dependency features; environments/deployment gates; repository metadata/features. See [github-settings.md](github-settings.md) for discovery sources and limits.
- **Recommendation**: Least privilege and existing organization policy first; offer useful available options with rationale, consequences and required authority. Distinguish unavailable from inaccessible/unverified. Do not request every possible toggle or silently enable paid/security/access changes.
- **Pruning Rule**: Prune settled choices, not discovery of effective settings. For local-only mode skip remote settings; for a new remote mark actual values pending post-creation inspection.

#### 2.6 Documentation & Governance
- **Question**: Which repository governance and documentation files should be generated?
- **Options**:
  - Standard governance suite (`README.md`, `SECURITY.md`, `CONTRIBUTING.md`, `LICENSE` [MIT], `docs/git-workflow.md`, `AGENTS.md` [linking to `docs/git-workflow.md`], `.github/ISSUE_TEMPLATE/`, `PULL_REQUEST_TEMPLATE.md`).
  - Minimal governance (`README.md` + `LICENSE`).
- **Recommendation**: Standard governance suite with MIT License.
- **Note on Existing Files**: If any of these files already exist, explicitly ask whether to **preserve** or **overwrite** them.

---

### Round 3: Development Workflow, Branching & Developer Experience (DX)

#### 3.1 Branching Strategy & Environment Branches
- **Question**: Which branching model and environment branches do you require?
- **Options**:
  - **Trunk-Based Development** (All feature branches merge directly into `main`).
  - **Multi-Environment Branches** (`main` for production, `staging` for pre-production, `develop` for integration).
- **Recommendation**: Preserve organization/repository requirements. Otherwise trunk-based development is simplest.
- **Follow-up**: Confirm protected base/PR target, branch prefixes, and whether feature branches are mandatory. Check remote base before creating a work branch; if remote verification fails, stop and ask about offline work. New local-only repositories have no remote to check.

#### 3.2 Git Worktrees Workflow
- **Question**: When should development use Git worktrees?
- **Options**: Required for changes | Situational for isolation/parallel work | Not used.
- **Recommendation**: Decide from organization rules and actual concurrent-work needs, not a universal default. If situational, a clean dedicated checkout may be enough for a small change.
- **Follow-up if used**: Choose location/ignore rule and when removal is allowed. Do not remove while a task, process, unmerged PR, or unpreserved changes still rely on it. Generate a helper only if useful and consistent with the chosen location.

#### 3.3 Staging, Commits, Push & PRs
- **Questions**:
  - Staging: targeted paths after diff review, or broad staging only after reviewing the entire tree?
  - Commits: coherent commits per intent or one per task; which message convention and hooks apply?
  - Push: who may push and when must approval be requested? Which branches are prohibited as direct push targets?
  - PR: which target branch, Draft/ready default, required checks/review, and merge method?
- **Recommendation**: Inspect applicable rules first. For unconstrained new repositories, recommend reviewed targeted staging, coherent commits, no direct push to protected branches, and explicit approval before remote publication. Treat other choices as interview answers, not fixed template rules.
- **Preflight**: Re-fetch and compare with the PR target before push/PR, and again if a long task may have made the result stale. If remote verification fails or target advanced, report the state and ask how to integrate; do not silently merge, rebase, or rewrite history. Preserve an explicit case-by-case policy choice if the user does not want a fixed rule.

#### 3.4 Runtime Version Pinning & Local Onboarding Automation
- **Question**: Do you want to pin runtime versions and generate a bootstrap setup script?
- **Options**:
  - Runtime version file (`.node-version`, `.python-version`, or `.tool-versions`).
  - Environment variable template (`.env.example`).
  - Onboarding setup script (`scripts/setup.sh`).
- **Recommendation**: **Yes** (pins predictable environment versions and allows one-command onboarding for contributors).

#### 3.5 Plain-Language Concept Comparison (DEC-005)
When presenting technical choices that may seem abstract or non-basic, include a compact comparison in plain language without jargon:

| Topic | Recommended Option | Alternative | Why the recommendation is better |
|---|---|---|---|
| **Branching when unconstrained** | **Trunk-Based Development** (single base branch + short-lived feature branches) | **GitFlow** (multiple permanent branches) | Simpler only when organization and repository rules do not require another model. |
| **Parallel Dev** | **Situational worktrees** when concurrent tasks need isolation | **Always / never use worktrees** | Match repository policy and concurrency without imposing extra checkouts. |
| **Commit Validation** | **Ecosystem-Native Hook** (Lefthook regex for Python/Go/Rust, Commitlint for JS/TS) | **Global npm Commitlint** (Installing Node.js everywhere) | **Zero pollution**: prevents adding foreign runtimes and lockfiles into pure Python/Go/Rust projects. |

---

## 3. Interview Synthesis: The Blueprint

Once all rounds are resolved, compile the agreed configuration into a concise, structured **Repository Blueprint** including the plain-language key decisions table, an ASCII tree preview, and the explicit **Approval Gate** stop. The following is an illustrative configuration, not a default; omit worktree and commit-lint artifacts when not selected:

```markdown
### 📋 Proposed Repository Blueprint

- **Target Directory**: `./my-awesome-app`
- **Remote GitHub**: `owner/my-awesome-app` (Private) via `gh`
- **Stack & Runtime**: TypeScript + React (Vite) with `pnpm` (Node 20 pinned via `.node-version`)
- **Branching & Environments**: Trunk-based (`main`), branch prefixes (`feat/`, `fix/`, `chore/`)
- **Parallel Dev Workflow**: Situational worktrees (`.worktrees/` in `.gitignore`, `scripts/worktree.sh`), if selected
- **Git Delivery Policy**: Reviewed targeted staging; coherent commits; approval before push/PR; PR target `main` and Draft default, if selected
- **Policy Conflicts**: <source, rule, consequence, user decision; omit when none>
- **Quality & Hooks**: Lefthook + Biome + Commitlint (Conventional Commits; illustrative approved choice, not default)
- **Evidence & GitHub Settings**: Dated tooling comparison; current/proposed settings, authority/plan limits, approved/deferred changes, and readback checks from the inventory
- **CI/CD Actions**:
  - `ci.yml`: Lint, typecheck, test, build on PR/push
  - `release-please.yml`: Automated semver releases & changelogs
  - `dependabot.yml`: Weekly npm dependencies update
- **Governance & DX**:
  - `README.md`, `SECURITY.md`, `CONTRIBUTING.md`, `LICENSE` (MIT)
  - `.github/ISSUE_TEMPLATE/` (bug & feature), `PULL_REQUEST_TEMPLATE.md`
  - `.editorconfig`, `.gitignore`, `.env.example`, `scripts/setup.sh`

**Directory Structure Preview:**
my-awesome-app/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── PULL_REQUEST_TEMPLATE.md
│   ├── dependabot.yml
│   └── workflows/
│       ├── ci.yml
│       └── release-please.yml
├── .editorconfig
├── .env.example
├── .gitignore
├── .node-version
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── SECURITY.md
├── biome.json
├── lefthook.yml
├── package.json
└── scripts/
    ├── setup.sh
    └── worktree.sh

👉 **Approval Gate**: Please review this blueprint. Should we proceed with scaffolding, or do you want to adjust any choice?
```
