# Tooling Recipes: Hooks, Linters, and Quality Guards

Configuration recipes for code quality tools, git hooks, and linters. Read [tool-selection.md](tool-selection.md) before choosing any tool. These are examples, not defaults: verify current package versions, CLI help, configuration schemas and compatibility before execution; use the approved package manager and keep hooks/scripts/CI consistent.

---

## 1. Git Hooks Managers

### 1.1 Lefthook (Recommended)
Lefthook is a fast, multi-platform, dependency-free Git hooks manager.

Installation:
- Via npm/pnpm: `pnpm add -D lefthook`
- Via Homebrew: `brew install lefthook`
- Via Go: `go install github.com/evilmartians/lefthook@latest`

`lefthook.yml` for JS/TS (with Biome):
```yaml
pre-commit:
  parallel: true
  commands:
    biome-check:
      glob: "*.{js,ts,cjs,mjs,d.cts,d.mts,jsx,tsx,json,jsonc}"
      run: npx @biomejs/biome check --write --no-errors-on-unmatched --files-ignore-unknown=true {staged_files}
      stage_fixed: true

commit-msg:
  commands:
    commitlint:
      run: npx commitlint --edit {1}
```

`lefthook.yml` for Python (with Ruff & Native Conventional Commits):
```yaml
pre-commit:
  parallel: true
  commands:
    ruff-format:
      glob: "*.py"
      run: uv run ruff format {staged_files}
      stage_fixed: true
    ruff-check:
      glob: "*.py"
      run: uv run ruff check --fix {staged_files}
      stage_fixed: true

commit-msg:
  commands:
    conventional-commits:
      run: |
        msg=$(head -n1 "$1")
        pattern="^(feat|fix|docs|style|refactor|perf|test|build|ci|chore|revert)(\([a-zA-Z0-9_\.-]+\))?: .{1,80}$"
        if ! echo "$msg" | grep -Eq "$pattern"; then
          echo "Error: Commit message does not follow Conventional Commits format."
          echo "Example: feat(scope): concise description"
          exit 1
        fi
```

> **Ecosystem Fit Invariant (DEC-004)**: Never install Node.js/npm dependencies (such as `@commitlint/cli`) in a pure Python, Go, or Rust project solely for commit linting. Always use Lefthook's native regex hook or a repository-local script to keep lockfiles and dev dependencies clean.

Activate hooks:
```bash
lefthook install # or npx lefthook install for JS/TS
```

### 1.2 Husky (Alternative for JS/TS)
```bash
pnpm add -D husky
npx husky init
echo "pnpm lint" > .husky/pre-commit
```

---

## 2. Linters & Formatters

### 2.1 Biome (When Selected)
Install:
```bash
pnpm add -D --save-exact @biomejs/biome
pnpm biome init
```

Example `biome.json`: generate with the selected version first and use its schema; merge only approved settings. The placeholder below is not executable as-is:
```json
{
  "$schema": "https://biomejs.dev/schemas/<selected-version>/schema.json",
  "vcs": {
    "enabled": true,
    "clientKind": "git",
    "useIgnoreFile": true
  },
  "files": {
    "ignoreUnknown": false,
    "includes": ["src/**/*", "*.config.*", "*.json"]
  },
  "formatter": {
    "enabled": true,
    "indentStyle": "space",
    "indentWidth": 2,
    "lineWidth": 100
  },
  "linter": {
    "enabled": true,
    "rules": {
      "recommended": true
    }
  },
  "javascript": {
    "formatter": {
      "quoteStyle": "single",
      "semicolons": "always"
    }
  }
}
```

### 2.2 ESLint + Prettier (Flat Config)
Install:
```bash
pnpm add -D eslint prettier eslint-config-prettier @eslint/js typescript-eslint
```

`eslint.config.js`:
```javascript
import js from "@eslint/js";
import tseslint from "typescript-eslint";
import prettier from "eslint-config-prettier";

export default tseslint.config(
  js.configs.recommended,
  ...tseslint.configs.recommended,
  prettier,
  {
    ignores: ["dist", "node_modules", "build"],
  }
);
```

`.prettierrc`:
```json
{
  "semi": true,
  "singleQuote": true,
  "trailingComma": "all",
  "printWidth": 100,
  "tabWidth": 2
}
```

### 2.3 Oxlint + Oxfmt (When Selected)

Oxlint is the linter; Oxfmt is the formatter. Verify required rules/plugins, type-aware linting, framework/file support and Oxfmt unsupported features in current official docs before treating the pair as a replacement for an existing setup. Keep any complementary tool only for a demonstrated coverage gap.

Example for an approved pnpm project (verify compatible versions first):
```bash
pnpm add -D --save-exact oxlint oxfmt
pnpm exec oxlint --init
pnpm exec oxfmt --init
```

Merge into existing `package.json` scripts; do not replace unrelated scripts:
```json
{
  "scripts": {
    "lint": "oxlint",
    "lint:fix": "oxlint --fix",
    "format": "oxfmt",
    "format:check": "oxfmt --check"
  }
}
```

Initialize and review `.oxlintrc.json` and `.oxfmtrc.json` (or supported equivalent for the chosen versions); configure actual source scope, rules and generated-file ignores. Type-aware linting may need additional documented setup/dependencies; it does not replace a required TypeScript typecheck. Do not enable dangerous fixes implicitly.

For approved Lefthook integration, use check-only commands so formatting and linting do not race or restage unrelated work:
```yaml
pre-commit:
  parallel: true
  commands:
    oxlint-check:
      glob: "*.{js,jsx,ts,tsx,mjs,cjs,mts,cts}"
      run: pnpm exec oxlint {staged_files}
    oxfmt-check:
      glob: "*.{js,jsx,ts,tsx,mjs,cjs,mts,cts,json,jsonc,css,md,yaml,yml}"
      run: pnpm exec oxfmt --check {staged_files}
```

Adapt globs and quoting to repository filenames and verified support; unsupported formats need an explicitly selected alternative. CI runs `pnpm run lint` and `pnpm run format:check`, never writing files. Oxfmt without `--check` writes files, so it is not a read-only validation command.

Official sources: [Oxlint quickstart](https://oxc.rs/docs/guide/usage/linter/quickstart.html), [Oxfmt quickstart](https://oxc.rs/docs/guide/usage/formatter/quickstart.html), [compatibility matrix](https://oxc.rs/docs/guide/compatibility.html), [Oxfmt unsupported features](https://oxc.rs/docs/guide/usage/formatter/unsupported-features.html). Commands consulted on 2026-10-01; re-verify at use time.

---

## 3. Commit Message Linting (Conventional Commits)

Install:
```bash
pnpm add -D @commitlint/cli @commitlint/config-conventional
```

`commitlint.config.js`:
```javascript
export default {
  extends: ["@commitlint/config-conventional"],
  rules: {
    "type-enum": [
      2,
      "always",
      [
        "feat",
        "fix",
        "docs",
        "style",
        "refactor",
        "perf",
        "test",
        "build",
        "ci",
        "chore",
        "revert"
      ]
    ],
    "subject-case": [0]
  }
};
```

---

## 4. EditorConfig (`.editorconfig`)

A standard cross-editor configuration at repository root:
```ini
root = true

[*]
charset = utf-8
end_of_line = lf
indent_style = space
indent_size = 2
insert_final_newline = true
trim_trailing_whitespace = true

[*.py]
indent_size = 4

[*.go]
indent_style = tab

[*.rs]
indent_size = 4

[*.md]
trim_trailing_whitespace = false
```

---

## 5. Git Worktrees Workflow & Helpers

Use this recipe only when the interview selects `.worktrees/` and a helper script. Replace `<selected-base-branch>` with the chosen branch and `<selected-remote-name>` with the selected remote name, or an empty string for a local-only repository. Worktrees can be required or situational; do not describe them as mandatory unless that policy was selected.

### 5.1 Ignore Rule
Add to `.gitignore`:
```gitignore
# Worktrees for parallel development
.worktrees/
```

### 5.2 Worktree Helper Script (`scripts/worktree.sh`)
```bash
#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd -P)"
WORKTREES_DIR="$REPO_ROOT/.worktrees"
BASE_BRANCH="<selected-base-branch>"
REMOTE_NAME="<selected-remote-name>"

usage() {
  echo "Usage: $0 {add|list|remove} [branch-name]"
  exit 1
}

cmd="${1:-}"
branch="${2:-}"

case "$cmd" in
  add)
    [ -z "$branch" ] && usage
    git check-ref-format --branch "$branch" >/dev/null
    target="$WORKTREES_DIR/$branch"
    if [ -n "$REMOTE_NAME" ]; then
      git -C "$REPO_ROOT" remote get-url "$REMOTE_NAME" >/dev/null
      git -C "$REPO_ROOT" fetch "$REMOTE_NAME" "+refs/heads/$BASE_BRANCH:refs/remotes/$REMOTE_NAME/$BASE_BRANCH"
      start_ref="refs/remotes/$REMOTE_NAME/$BASE_BRANCH"
    else
      if [ -n "$(git -C "$REPO_ROOT" remote)" ]; then
        echo "Remote exists but no base remote was selected" >&2
        exit 1
      fi
      start_ref="refs/heads/$BASE_BRANCH"
      git -C "$REPO_ROOT" show-ref --verify --quiet "$start_ref" || {
        echo "Local base branch not found: $BASE_BRANCH" >&2
        exit 1
      }
    fi
    mkdir -p "$(dirname "$target")"
    echo "Creating worktree at $target for branch $branch..."
    git -C "$REPO_ROOT" worktree add "$target" -b "$branch" "$start_ref"
    echo "Worktree ready: $target"
    ;;
  list)
    git -C "$REPO_ROOT" worktree list
    ;;
  remove)
    [ -z "$branch" ] && usage
    git check-ref-format --branch "$branch" >/dev/null
    target="$WORKTREES_DIR/$branch"
    [ -d "$target" ] || { echo "Worktree not found: $target" >&2; exit 1; }
    actual_root="$(git -C "$target" rev-parse --show-toplevel)"
    actual_branch="$(git -C "$target" symbolic-ref --quiet --short HEAD)"
    [ "$actual_root" = "$target" ] && [ "$actual_branch" = "$branch" ] || {
      echo "Worktree path/branch mismatch; refusing removal" >&2
      exit 1
    }
    printf 'Confirm PR merged/closed, no task or process uses %s, and all changes are preserved. Remove? [y/N] ' "$target"
    read -r answer
    [ "$answer" = y ] || { echo "Removal cancelled" >&2; exit 1; }
    git -C "$REPO_ROOT" worktree remove "$target"
    git -C "$REPO_ROOT" worktree prune
    echo "Worktree removed."
    ;;
  *)
    usage
    ;;
esac
```
Make executable: `chmod +x scripts/worktree.sh`.

---

## 6. Developer Experience (DX) & Runtime Pinning

### 6.1 Runtime Version Pinning
- **Node.js**:
  - `.node-version`: `20`
  - `.nvmrc`: `20`
- **Python**:
  - `.python-version`: `3.11`
- **Tool-agnostic (asdf / mise)**:
  - `.tool-versions`:
    ```text
    nodejs 20.18.0
    python 3.11.9
    ```

### 6.2 Environment Template (`.env.example`)
Create a sanitized `.env.example` at repository root:
```ini
# Application Environment Configuration
# Copy this file to .env and fill in the values

APP_ENV=development
PORT=3000
API_BASE_URL=http://localhost:3000/api

# Database / External Services (Leave dummy values)
# DATABASE_URL=postgresql://user:password@localhost:5432/app_dev
```
Ensure `.env` and `.env.local` are in `.gitignore`.

### 6.3 All-In-One Setup Script (`scripts/setup.sh`)
```bash
#!/usr/bin/env bash
set -euo pipefail

echo "==> Setting up development environment..."

# 1. Copy environment template if not present
if [ -f ".env.example" ] && [ ! -f ".env" ]; then
  echo "--> Creating .env from .env.example"
  cp .env.example .env
fi

# 2. Install dependencies (auto-detect stack)
if [ -f "pnpm-lock.yaml" ]; then
  pnpm install
elif [ -f "package.json" ]; then
  npm install
elif [ -f "pyproject.toml" ]; then
  uv sync || poetry install
fi

# 3. Setup git hooks
if [ -f "lefthook.yml" ]; then
  npx lefthook install || lefthook install
elif [ -d ".husky" ]; then
  npx husky
fi

echo "==> Setup completed successfully!"
```
Make executable: `chmod +x scripts/setup.sh`.
