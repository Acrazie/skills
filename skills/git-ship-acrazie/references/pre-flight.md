# Pre-Flight Safety, Hygiene & Quality Checks

Before any commit or staging takes place, `git-ship-acrazie` performs rigorous safety verification to protect repository integrity.

---

## 1. Branch Safety Check

1. **Detect Current Branch**:
   ```bash
   git branch --show-current
   ```
2. **Default Branch Protection**:
   - If the current branch matches the default branch (`main`, `master`, or production branch):
     - **HALT IMMEDIATELY**.
     - Direct commits to the default branch violate trunk-based stability and branch protection rules.
     - Propose:
       - Creating a new feature branch:
         ```bash
         git checkout -b feat/<topic>
         ```
       - Or provisioning a dedicated Git Worktree:
         ```bash
         git worktree add .worktrees/<topic> -b feat/<topic> origin/main
         ```
     - Await user choice before continuing.

---

## 2. Secrets & Repository Hygiene Audit

1. **Check Status**:
   ```bash
   git status -s
   ```
2. **Scan for Forbidden & Sensitive Files**:
   Inspect untracked (`??`) and modified (`M`) files against known dangerous patterns:
   - **Environment files & secrets**: `.env`, `.env.*`, `*.pem`, `*.key`, `id_rsa*`, `credentials.json`.
   - **Worktrees & internal tool dirs**: `.worktrees/`, `.hermes/`, `.skill-refiner/`, `.skill-improver/`, `.impeccable/`.
   - **Build artifacts & caches**: `node_modules/`, `dist/`, `build/`, `__pycache__/`, `.cache/`, `.pytest_cache/`, `target/`.
   - **OS metadata**: `.DS_Store`, `Thumbs.db`.
3. **Action on Violation**:
   - If a forbidden file is untracked: ensure it is **NEVER** added with `git add`. Add it to `.gitignore` if appropriate.
   - If a sensitive file is already tracked: alert the user immediately and request untracking (`git rm --cached <file>`) before proceeding.

---

## 3. Pre-Commit Quality Gates

1. **Determine Quality Gate Command**:
   - Check `docs/git-workflow.md` for defined pre-commit commands.
   - If not specified in the workflow doc, inspect project configuration:
     - `lefthook.yml` present $\rightarrow$ `npx lefthook run pre-commit` (or `lefthook run pre-commit`).
     - `package.json` with `test` or `lint` scripts $\rightarrow$ `npm test` / `pnpm test` / `pnpm lint`.
     - Python with `pyproject.toml` $\rightarrow$ `uv run ruff check` / `uv run pytest`.
     - Go with `go.mod` $\rightarrow$ `go test ./...` / `golangci-lint run`.
     - Rust with `Cargo.toml` $\rightarrow$ `cargo test` / `cargo clippy`.
2. **Execution & Failure Handling**:
   - Run the command.
   - If the check passes: proceed to Step 3 (Delivery Synthesis).
   - If the check fails:
     - Output the failing test/linter logs clearly.
     - **DO NOT** commit broken code.
     - Ask the user whether they want to fix the issues now, or if an intentional override is requested.
     - Never pass `--no-verify` to `git commit`.
