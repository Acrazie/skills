# GitHub Actions Workflows Reference

Standard, secure GitHub Actions workflows for continuous integration, release automation, and dependency management.

---

## 1. Continuous Integration (`.github/workflows/ci.yml`)

Adapts to the selected branching model (e.g. `[main]` for trunk-based, or `[main, staging, develop]` for multi-environment branches).

### 1.1 Node.js / TypeScript (pnpm + Biome)
```yaml
name: CI

on:
  push:
    branches: [main, staging, develop] # adjust to selected environment branches
  pull_request:
    branches: [main, staging, develop]

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

jobs:
  validate:
    name: Lint, Test & Build
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Install pnpm
        uses: pnpm/action-setup@v4
        with:
          version: 9

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 24
          cache: 'pnpm'

      - name: Install dependencies
        run: pnpm install --frozen-lockfile

      - name: Run Biome (Lint & Format check)
        run: pnpm biome check .

      - name: Typecheck
        run: pnpm tsc --noEmit
        if: hashFiles('tsconfig.json') != ''

      - name: Run Tests
        run: pnpm test
        if: hashFiles('vitest.config.*', 'jest.config.*') != ''

      - name: Build
        run: pnpm build
        if: hashFiles('vite.config.*', 'next.config.*', 'tsup.config.*') != ''
```

### 1.2 Python (`uv` + Ruff)
```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

jobs:
  validate:
    name: Lint & Test
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Install uv
        uses: astral-sh/setup-uv@v5
        with:
          enable-cache: true
          version: "latest"

      - name: Set up Python
        run: uv python install

      - name: Install dependencies
        run: uv sync --all-extras --dev

      - name: Check formatting with Ruff
        run: uv run ruff format --check

      - name: Lint with Ruff
        run: uv run ruff check

      - name: Run Tests
        run: uv run pytest
```

---

## 2. Automated Releases (`.github/workflows/release-please.yml`)

Automates semver versioning, changelog generation, and GitHub release creation based on Conventional Commits.

```yaml
name: Release Please

on:
  push:
    branches:
      - main

permissions:
  contents: write
  pull-requests: write

concurrency:
  group: release-please
  cancel-in-progress: false

env:
  FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true

jobs:
  release-please:
    runs-on: ubuntu-latest
    steps:
      - uses: googleapis/release-please-action@v4
        with:
          release-type: node # or python, simple, go, rust
```

Optional `release-please-config.json` at repository root:
```json
{
  "packages": {
    ".": {
      "release-type": "node",
      "changelog-path": "CHANGELOG.md"
    }
  }
}
```

---

## 3. Dependabot Configuration (`.github/dependabot.yml`)

Automated weekly dependency maintenance:

```yaml
version: 2
updates:
  # Maintain GitHub Actions dependencies
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"
    groups:
      actions:
        patterns:
          - "*"

  # Maintain package manager dependencies (e.g. npm, pip, gomod, cargo)
  - package-ecosystem: "npm" # replace with 'pip', 'gomod', or 'cargo' as needed
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 10
    groups:
      dependencies:
        patterns:
          - "*"
```
