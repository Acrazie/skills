---
name: script-portability-acrazie
description: >-
  Audit, refactor, and harden cross-platform automation commands and package scripts (package.json,
  shell scripts) across Linux, macOS, and Windows. Eliminate brittle polyfills (rimraf, cross-env,
  shx), remove subprocess spawning overhead, and prevent shell command injection. Use when scripts
  fail on Windows runners, build steps contain OS-specific syntax, or projects seek to slim down
  developer tooling dependencies. Not for whole-toolchain upgrades or Jenkins pipeline authoring.
---

# Script Portability & Shell Hardening / Acrazie

Transform brittle, OS-dependent automation scripts into rock-solid, cross-platform commands while purging
redundant polyfill dependencies (`cross-env`, `rimraf`, `shx`) and eliminating subshell spawning latency.

## Core principles & portability invariants

1. **Universal OS Invariance**:
   Every script declared in `package.json` or `scripts/` must produce identical side effects and exit codes
   across POSIX (Linux, macOS) and Windows (Command Prompt, PowerShell, CI runners) without requiring developers
   to configure bespoke shell wrappers.
2. **Polyfill Purge Axiom**:
   Third-party npm compatibility polyfills (`rimraf`, `cross-env`, `shx`, `mkdirp`, `which`) represent
   millions of wasted weekly downloads, bloated lockfiles, and avoidable supply-chain attack surfaces. Replace
   them with standard runtime capabilities:
   - Modern Node.js built-ins (`node --run`, `node --env-file`, standard library one-liners with `fs.rmSync`), or
   - The integrated native Bun Shell (`$`) which parses shell ASTs in-process with zero subprocess overhead.
3. **Command Injection Hardening**:
   Never allow raw string concatenation or unescaped variables inside shell execution strings. All interpolated
   values must be passed through parameterized APIs or template tag escapes.
4. **Minimal Subprocess Overhead**:
   Avoid chaining multiple subshell forks (`sh -c "foo && bar"`) which trigger costly kernel transitions
   (1,000–1,500 clock cycles per syscall). Group execution into single-process flows or in-memory streams.

## Portability workflow

Follow [references/portable-scripting-guide.md](./references/portable-scripting-guide.md) across all phases:

### Phase 1: Script inventory & OS hazard detection

1. **Extract all script targets**:
   - Inspect `scripts` in root and workspace `package.json` manifests.
   - Inspect standalone utility scripts (`scripts/*.sh`, `scripts/*.js`, `scripts/*.ts`).
2. **Scan for OS-specific hazards**:
   - **Environment variables**: Inline prefix syntax (`FOO=bar cmd` fails on Windows `cmd.exe`).
   - **Path separators**: Hardcoded forward slashes or backslashes in shell arguments (e.g. `dist\bundle.js`).
   - **Filesystem mutations**: Shell-specific commands (`rm -rf`, `mkdir -p`, `cp -r`, `del /s /q`).
   - **Chaining operators**: Platform differences with `;`, `&&`, and wildcard expansions (`*/**`).
3. **Catalog polyfill dependencies**:
   Identify devDependencies that can be safely eliminated:
   `cross-env`, `rimraf`, `shx`, `mkdirp`, `which`, `npm-run-all`, `touch`.

### Phase 2: Refactoring strategy selection

Select the target refactoring strategy based on the project's runtime environment:

| Feature | Strategy A: Runtime-Neutral (Node / pnpm / yarn) | Strategy B: Bun-Native (Bun Shell `$`) |
| :--- | :--- | :--- |
| **Env Variables** | `node --env-file=.env` or standard export script | Inline syntax parsed natively: `FOO=bar cmd` |
| **Filesystem Clean** | `node -e "fs.rmSync('dist', { recursive: true, force: true })"` | `rm -rf dist` (handled in-process by Bun Shell) |
| **Directory Creation** | `node -e "fs.mkdirSync('dist', { recursive: true })"` | `mkdir -p dist` (handled in-process by Bun Shell) |
| **Cross-Platform CLI** | Dedicated micro-script in `scripts/clean.js` | Direct script in `package.json` using `bun $` |
| **Subprocess Spawns** | Standard OS subshell per script step | Zero fork/spawn; in-process C-level execution |

### Phase 3: Manifest cleanup & dependency purge

1. **Update `package.json` scripts**:
   Replace hazard commands with the chosen portable strategy.
2. **Remove obsolete polyfills**:
   Remove `cross-env`, `rimraf`, `shx`, etc. from `devDependencies`.
3. **Synchronize lockfile**:
   Run the project's native package manager install command to prune dependencies cleanly.

### Phase 4: Cross-platform verification

Verify that all refactored scripts execute correctly:
1. Dry-run commands under POSIX shell emulation.
2. Validate syntax compatibility against Windows command rules (escaping quotes with `\"`, avoiding bash-only expansions).
3. Confirm clean zero exit codes on clean trees and non-zero exit codes on failure states.

## Deliverable format

Emit a markdown diagnostic artifact `script-portability-report.md` structured as:

```markdown
# Script Portability & Shell Hardening Report

## 1. Executive Summary
- **Audited Manifests**: `package.json`, `scripts/*`
- **Strategy Selected**: [Runtime-Neutral | Bun-Native]
- **Polyfill Dependencies Purged**: [e.g. cross-env, rimraf, shx]
- **OS Compatibility**: Verified across Linux, macOS, and Windows

## 2. Identified Hazards & Anti-Patterns
| Script Name | Hazard Detected | Platform Failure Risk |
| :--- | :--- | :--- |
| `clean` | `rm -rf dist/` | Fails on Windows (`cmd.exe`) |
| `build:dev` | `NODE_ENV=dev vite` | Fails on Windows (`NODE_ENV` not recognized) |

## 3. Refactored Scripts (Diff)
\`\`\`diff
--- a/package.json
+++ b/package.json
@@ -10,8 +10,8 @@
   "scripts": {
-    "clean": "rimraf dist",
-    "build": "cross-env NODE_ENV=production vite build"
+    "clean": "node -e \"fs.rmSync('dist', { recursive: true, force: true })\"",
+    "build": "node --env-file=.env.production vite build"
   }
\`\`\`

## 4. Supply-Chain & Performance Impact
- **Dependencies Removed**: 3 packages (`rimraf`, `cross-env`, `shx`).
- **Disk / Syscall Savings**: ~450 fewer files in `node_modules`, 0 subprocess spawns during clean step.
- **Verification Result**: Exit code 0 across POSIX and Windows test matrix.
```
