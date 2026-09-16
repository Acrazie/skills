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

`lefthook.yml` for Python (with Ruff):
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
```

Activate hooks:
```bash
npx lefthook install # or lefthook install
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
