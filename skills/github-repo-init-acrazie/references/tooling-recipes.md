# Tooling Recipes: Hooks, Linters, and Quality Guards

Configuration recipes for code quality tools, git hooks, and linters.

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

### 2.1 Biome (Recommended for JS/TS)
Install:
```bash
pnpm add -D --save-exact @biomejs/biome
pnpm biome init
```

Optimized `biome.json`:
```json
{
  "$schema": "https://biomejs.dev/schemas/1.9.4/schema.json",
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

Using Git Worktrees allows multiple branches to be checked out simultaneously in isolated directories under `.worktrees/`. This prevents branch switching thrashing, keeps dirty states separated, and enables parallel AI agent or developer workflows.

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

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
WORKTREES_DIR="$REPO_ROOT/.worktrees"

usage() {
  echo "Usage: $0 {add|list|remove} [branch-name]"
  exit 1
}

cmd="${1:-}"
branch="${2:-}"

case "$cmd" in
  add)
    [ -z "$branch" ] && usage
    clean_name="${branch//\//-}"
    target="$WORKTREES_DIR/$clean_name"
    mkdir -p "$WORKTREES_DIR"
    git fetch origin main 2>/dev/null || true
    echo "Creating worktree at $target for branch $branch..."
    git worktree add "$target" -b "$branch" origin/main 2>/dev/null || git worktree add "$target" "$branch"
    echo "Worktree ready: $target"
    ;;
  list)
    git worktree list
    ;;
  remove)
    [ -z "$branch" ] && usage
    clean_name="${branch//\//-}"
    target="$WORKTREES_DIR/$clean_name"
    echo "Removing worktree at $target..."
    git worktree remove "$target"
    git worktree prune
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

