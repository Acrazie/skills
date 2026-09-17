# Adaptive GitHub Repository Initialization Interview Tree

Use this decision map to interview the user adaptively before any scaffolding occurs. Do not treat this as an inflexible robotic questionnaire; skip decisions that the user has already made explicit or that are constrained by existing facts discovered during Step 1. Present questions grouped into at most **2 to 3 progressive rounds**, where every question includes an explicit, contextual recommendation with rationale.

---

## 1. Ground Rules & Sequence

1. **Deep Discovery First (DEC-001)**:
   - Before asking questions, inspect the current working directory, git state, and configuration files.
   - If the repository is already populated or initialized, settle known decisions as established facts and prune redundant questions according to the table below.
2. **Progressive Rounds (DEC-002)**:
   - Never dump all interview themes in a single monolithic questionnaire. Structure the interaction into at most 2 to 3 logical rounds (Identity & Stack -> Quality & CI/CD -> Workflow & DX).
3. **Always Recommend with Rationale**:
   - For every question asked, state available options and provide an explicit recommended default with a concise justification.
4. **Shared Blueprint Approval (DEC-003)**:
   - When all rounds are completed, synthesize a single **Initialization Blueprint** (bulleted summary + visual ASCII directory structure) and require explicit user sign-off before executing any mutating shell commands or writing files.

---

### Automated Pruning Rules

| Artifact / Environment Detected | Established Fact | Pruned Interview Questions |
|---|---|---|
| `pyproject.toml`, `requirements.txt`, `Pipfile` | Stack is **Python** | Do NOT ask between JS/TS, Python, Go, Rust. Recommend `uv` and `Ruff`. |
| `package.json`, `tsconfig.json` | Stack is **TypeScript/JavaScript** | Do NOT ask between JS/TS, Python, Go, Rust. Recommend `pnpm` and `Biome`. |
| `go.mod` | Stack is **Go** | Do NOT ask for general stack choice. Recommend `golangci-lint`. |
| `Cargo.toml` | Stack is **Rust** | Do NOT ask for general stack choice. Recommend `clippy`. |
| `git remote -v` contains `origin` | Remote repository already exists | Do NOT ask to create a new remote with `gh repo create`. Just confirm keeping `origin`. |
| `.github/workflows/ci.yml` exists | CI workflow already configured | Do NOT ask if CI is needed. Ask whether to standardize / upgrade existing CI. |
| `biome.json`, `ruff.toml`, `.eslintrc*` | Linter/formatter already chosen | Do NOT ask to choose between linters. Propose keeping current tool. |
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
- **Recommendation**: Stack-specific modern standard (`uv` for Python, `pnpm` + Vite for JS/TS, standard toolchains for Go/Rust).
- **Pruning Rule**: Prune entirely if an authoritative manifest (`pyproject.toml`, `package.json`, `go.mod`, `Cargo.toml`) was detected during Step 1.

---

### Round 2: Code Quality Gates, CI/CD & Governance

#### 2.1 Git Hooks Manager
- **Question**: Which Git hook manager would you like to configure?
- **Options**: **Lefthook** | Husky | pre-commit | None.
- **Recommendation**: **Lefthook** (language-agnostic, ultra-fast Go binary, zero-dependency pre-commit runner).
- **Pruning Rule**: Prune if `lefthook.yml`, `.husky/`, or `.pre-commit-config.yaml` is already present.

#### 2.2 Linter & Formatter
- **Question**: Which linter and code formatter should be configured?
- **Options**:
  - *JS/TS*: **Biome** (recommended: 30x faster, zero config fatigue) vs ESLint + Prettier.
  - *Python*: **Ruff** (recommended: Rust-powered, all-in-one linter & formatter) vs Black/Flake8.
  - *Go*: `golangci-lint` + `gofmt`.
  - *Rust*: `clippy` + `rustfmt`.
- **Recommendation**: **Biome** for JS/TS; **Ruff** for Python; native linters for Go/Rust.
- **Pruning Rule**: Prune if already configured in existing repo files.

#### 2.3 Commit Linting & Conventions
- **Question**: Do you want to enforce Conventional Commits (`feat:`, `fix:`, `chore:`, etc.) via commit-msg hooks?
- **Options**: Yes (Commitlint hook) | No (Manual conventions).
- **Recommendation**: **Yes** (enables automated release management and clean semver changelogs).

#### 2.4 CI/CD Workflows (GitHub Actions)
- **Question**: Which automated GitHub Actions workflows do you want to enable?
- **Options**:
  - Automated CI (`.github/workflows/ci.yml`: lint, typecheck, test, build).
  - Automated Releases: **Release Please** (recommended) | Changesets | Tag-based | None.
  - Security & Dependency audits: Dependabot (`.github/dependabot.yml`) | None.
- **Recommendation**: Automated CI + **Release Please** (Google Action automating changelogs and semver tags).
- **Pruning Rule**: If `.github/workflows/ci.yml` or `release-please.yml` already exists, offer to update/standardize instead of asking whether to create them from scratch.

#### 2.5 Documentation & Governance
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
- **Recommendation**: **Trunk-Based Development** (simplest, fastest, and most compatible with modern CI/CD and Release Please).

#### 3.2 Git Worktrees Workflow
- **Question**: Do you want to enable a Git Worktrees workflow for isolated parallel development (e.g. `.worktrees/<branch>` directories)?
- **Options**: Yes (`.worktrees/` in `.gitignore` + helper script `scripts/worktree.sh`) | No.
- **Recommendation**: **Yes** (essential if multiple concurrent tasks, features, or AI agents work on the repository simultaneously).

#### 3.3 Runtime Version Pinning & Local Onboarding Automation
- **Question**: Do you want to pin runtime versions and generate a bootstrap setup script?
- **Options**:
  - Runtime version file (`.node-version`, `.python-version`, or `.tool-versions`).
  - Environment variable template (`.env.example`).
  - Onboarding setup script (`scripts/setup.sh`).
- **Recommendation**: **Yes** (pins predictable environment versions and allows one-command onboarding for contributors).

---

## 3. Interview Synthesis: The Blueprint

Once all 3 rounds are resolved, compile the agreed configuration into a concise, structured **Repository Blueprint** followed by an ASCII tree preview and the explicit **Approval Gate** stop:

```markdown
### 📋 Proposed Repository Blueprint

- **Target Directory**: `./my-awesome-app`
- **Remote GitHub**: `owner/my-awesome-app` (Private) via `gh`
- **Stack & Runtime**: TypeScript + React (Vite) with `pnpm` (Node 20 pinned via `.node-version`)
- **Branching & Environments**: Trunk-based (`main`), branch prefixes (`feat/`, `fix/`, `chore/`)
- **Parallel Dev Workflow**: Git Worktrees enabled (`.worktrees/` in `.gitignore`, `scripts/worktree.sh`)
- **Quality & Hooks**: Lefthook + Biome + Commitlint (Conventional Commits)
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
