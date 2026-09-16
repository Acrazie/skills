# Stack Scaffolding Recipes

Deterministic, battle-tested scaffolding commands and recipes for each supported technology stack.

---

## 1. JavaScript / TypeScript

### 1.1 Vite + React (TypeScript)
```bash
# Using pnpm (or npm / yarn / bun)
pnpm create vite . --template react-ts
pnpm install
```

### 1.2 Vite + Vue 3 (TypeScript)
```bash
pnpm create vite . --template vue-ts
pnpm install
```

### 1.3 Next.js (App Router, TypeScript, Tailwind)
```bash
pnpm create next-app . --typescript --tailwind --eslint --app --src-dir --import-alias "@/*" --use-pnpm
```

### 1.4 Node.js / TypeScript Library or CLI (tsup)
```bash
pnpm init
pnpm add -D typescript @types/node tsup vitest
# Initialize tsconfig
pnpm tsc --init --target ES2022 --module NodeNext --moduleResolution NodeNext --outDir dist
```
Add to `package.json`:
```json
{
  "type": "module",
  "scripts": {
    "build": "tsup src/index.ts --format esm,cjs --dts",
    "dev": "tsup src/index.ts --watch",
    "test": "vitest run"
  }
}
```

---

## 2. Python

### 2.1 Python with `uv` (Recommended)
`uv` is an extremely fast Python package and project manager written in Rust.

```bash
# Initialize uv project
uv init --app # or --lib
# Add dev tools
uv add --dev ruff pytest
# Optional: Add framework
uv add fastapi uvicorn
```

Generated `pyproject.toml` integration with Ruff:
```toml
[project]
name = "<project-name>"
version = "0.1.0"
description = "<project-description>"
readme = "README.md"
requires-python = ">=3.11"
dependencies = []

[dependency-groups]
dev = [
    "pytest>=8.0.0",
    "ruff>=0.9.0",
]

[tool.ruff]
line-length = 88
target-version = "py311"

[tool.ruff.lint]
select = ["E", "F", "W", "I", "UP", "B", "SIM"]
ignore = []

[tool.pytest.ini_options]
testpaths = ["tests"]
```

---

## 3. Go

```bash
go mod init github.com/<owner>/<repo-name>
mkdir -p cmd/<repo-name> internal pkg
touch cmd/<repo-name>/main.go
```

Minimal `cmd/<repo-name>/main.go`:
```go
package main

import "fmt"

func main() {
	fmt.Println("Hello from <repo-name>!")
}
```

---

## 4. Rust

```bash
# For a binary application:
cargo init --bin .

# For a library:
cargo init --lib .
```

Standard `Cargo.toml`:
```toml
[package]
name = "<repo-name>"
version = "0.1.0"
edition = "2021"
authors = ["<owner>"]
description = "<project-description>"
license = "MIT"

[dependencies]

[dev-dependencies]
```

---

## 5. Custom / Stack-Agnostic Mode

When the user chooses "Custom" or "None":
1. Check if the user specified a custom CLI generator (e.g. `npx create-remix@latest`, `mix phx.new`, `dotnet new webapi`).
2. Run the custom command if approved.
3. If no framework is needed ("None" / empty repo):
   - Set up the standard directory hierarchy:
     ```bash
     mkdir -p src tests docs
     ```
   - Proceed directly to git hooks, documentation, and CI/CD workflow configuration.
