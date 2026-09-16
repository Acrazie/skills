# Adaptive GitHub Repository Initialization Interview Tree

Use this decision map to interview the user adaptively before any scaffolding occurs. Do not treat this as an inflexible robotic questionnaire; skip decisions that the user has already made explicit or that are constrained by existing facts. Present questions grouped by theme with recommended answers and rationales.

---

## 1. Ground Rules & Sequence

1. **Discovery First**: Check if the working directory already contains files, a git repository, or a package manifest. If files exist, confirm whether to initialize in-place or into a new subfolder.
2. **Never Assume Silently**: If the user hasn't specified a tool or framework, ask. Always provide a recommended default with a concise reason.
3. **Prerequisite Gating**: Do not ask tool-specific questions before the stack is chosen (e.g., do not ask between Biome and ESLint before knowing if JS/TS is selected).
4. **Shared Blueprint Approval**: When all questions are resolved, synthesize a single **Initialization Blueprint** and require explicit user sign-off before executing any commands or generating files.

---

## 2. Decision Tree & Themes

### Theme A: Repository Identity & Target Location
Prerequisites: None (Frontier Round 1)

1. **Repository Name & Description**:
   - Question: What is the project / repository name and a one-line description?
   - Default: Current directory name if meaningful, or prompt for name.
2. **Target Path**:
   - Question: Should the repository be created in the current working directory (`.`) or in a new subfolder (`./<repo-name>`)?
   - Recommendation: Current directory if already named after the project and empty; subfolder otherwise.
3. **Remote GitHub Repository**:
   - Question: Do you want to create and connect a remote repository on GitHub (`gh repo create`) right away, or keep it local-only for now?
   - Options:
     - Local git repository only.
     - Remote GitHub repository: **Public**.
     - Remote GitHub repository: **Private**.
   - Note: Verify `gh auth status` before offering GitHub remote creation.

---

### Theme B: Language, Stack & Framework Preset
Prerequisites: Theme A settled

1. **Framework / Technology Preset**:
   - Options:
     - **TypeScript / JavaScript**:
       - *Frontend*: React (Vite / Next.js), Vue (Vite / Nuxt), Svelte.
       - *Backend / Node*: Node.js / TypeScript (tsup / Hono / Express / Fastify / CLI).
     - **Python**:
       - *Package Manager*: `uv` (recommended: ultra-fast, modern) or `poetry`.
       - *Type*: CLI, FastAPI, Library, or minimal script.
     - **Go**:
       - Go module (`go mod init <module-path>`), CLI (Cobra) or HTTP service.
     - **Rust**:
       - Cargo binary (`cargo new --bin`) or library (`cargo new --lib`).
     - **Custom / Stack-Agnostic**:
       - User provides their own initialization command (e.g., custom generator, starter kit) or starts completely empty without code scaffolding.
2. **Package Manager**:
   - JS/TS: `pnpm` (recommended for disk space & speed), `npm`, `yarn`, or `bun`.
   - Python: `uv` (recommended) or `poetry`.

---

### Theme C: Code Quality & Git Hooks
Prerequisites: Stack settled (Theme B)

1. **Git Hooks Manager**:
   - Options:
     - **Lefthook** (Recommended: ultra-fast Go binary, language-agnostic, zero-dependency pre-commit runner).
     - **Husky** (Standard in the JS/TS ecosystem).
     - **pre-commit** (Python-based framework).
     - **None** (Manual scripts only).
2. **Linter & Formatter**:
   - *For JS/TS*:
     - **Biome** (Recommended: 30x faster than ESLint+Prettier, unified linter & formatter, zero configuration fatigue).
     - **ESLint + Prettier** (Legacy standard, maximum plugin ecosystem).
   - *For Python*:
     - **Ruff** (Recommended: Rust-powered linter and formatter, replaces Black/Flake8/isort).
   - *For Go*:
     - `golangci-lint` + `gofmt`.
   - *For Rust*:
     - `clippy` + `rustfmt`.
3. **Commit Convention & Message Linting**:
   - Question: Do you want to enforce Conventional Commits (`feat:`, `fix:`, `chore:`, etc.) via commit-msg hooks?
   - Recommendation: Yes (enables automated changelogs and semver releases).

---

### Theme D: CI/CD & Automation (GitHub Actions)
Prerequisites: Stack & Tools settled (Themes B, C)

1. **Continuous Integration Workflow (`.github/workflows/ci.yml`)**:
   - Triggers: Pull Requests and pushes to `main`.
   - Steps: Checkout, setup environment with caching, dependency installation, lint/format check, typecheck, test, and build.
2. **Automated Releases & Versioning**:
   - Options:
     - **Release Please** (Recommended: Google GitHub Action that creates release PRs and tags automatically from Conventional Commits).
     - **Changesets** (Ideal for monorepos or multi-package JS libraries).
     - **GitHub Release on Tag** (Triggered manually or upon pushing `v*.*.*` tags).
     - **None** (Manual release management).
3. **Security & Dependency Audits**:
   - Question: Add automated security checks?
   - Sub-options:
     - Dependabot configuration (`.github/dependabot.yml`).
     - Automated vulnerability scan in CI (e.g. `npm audit`, `cargo audit`, or CodeQL).

---

### Theme E: Documentation & Repository Governance
Prerequisites: Theme A settled

1. **README.md Structure**:
   - Include: Title, badges, brief overview, prerequisites, quickstart, available commands/scripts, architecture outline, and license mention.
2. **Security Policy (`SECURITY.md`)**:
   - Supported versions table, private disclosure process, reporting email or GitHub Security Advisory instructions.
3. **Contribution Guidelines (`CONTRIBUTING.md`)**:
   - Prerequisites, branch naming conventions, commit guidelines (Conventional Commits), PR process, and local testing instructions.
4. **License (`LICENSE`)**:
   - Choice: MIT (recommended for open source), Apache 2.0, BSD-3-Clause, MPL-2.0, GPL-3.0, Unlicense, or Proprietary / All Rights Reserved.
5. **Issue & Pull Request Templates (`.github/`)**:
   - Bug report template, Feature request template, and standard Pull Request template with checklist.
6. **Code Ownership (`CODEOWNERS`)**:
   - Optional GitHub username or team handle.
7. **Environment & Editor Consistency**:
   - `.editorconfig` (indent style, charset, trim trailing whitespace).
   - `.gitignore` (curated strictly for the selected language, OS, and tools).

---

## 3. Interview Synthesis: The Blueprint

Once all questions are answered, compile the decisions into a **Repository Blueprint** formatted as follows:

```markdown
### 📋 Proposed Repository Blueprint

- **Target Directory**: `./my-awesome-app`
- **Remote GitHub**: `owner/my-awesome-app` (Private) via `gh`
- **Stack & Runtime**: TypeScript + React (Vite) with `pnpm`
- **Quality & Hooks**: Lefthook + Biome + Commitlint (Conventional Commits)
- **CI/CD Actions**:
  - `ci.yml`: Lint, typecheck, test, build on PR/push
  - `release-please.yml`: Automated semver releases & changelogs
  - `dependabot.yml`: Weekly npm dependencies update
- **Governance**:
  - `README.md`, `SECURITY.md`, `CONTRIBUTING.md`, `LICENSE` (MIT)
  - `.github/ISSUE_TEMPLATE/` (bug & feature), `PULL_REQUEST_TEMPLATE.md`
  - `.editorconfig`, `.gitignore`

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
├── .gitignore
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── SECURITY.md
├── biome.json
├── lefthook.yml
└── package.json (and source files)

👉 **Approval Gate**: Please review this blueprint. Should we proceed with scaffolding, or do you want to adjust any choice?
```
