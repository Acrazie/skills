# Cross-Platform Script Portability & Shell Hardening Guide

Hazard categories and illustrative alternatives for the selected scripts only. Apply the entry skill's approved scope, target matrix and separate execution, installation and report-write gates first. Recipes below are not certified by instruction tests: verify current runtime documentation and actual behavior before application. Unknown compatibility remains a gap, not permission to remove a helper.

---

## 1. Operating System Impedance Matrix

Automation scripts written casually on macOS or Linux frequently fail when executed by contributors or CI runners on Windows due to foundational differences in shell semantics:

| Operation | POSIX (`bash`, `zsh`, `sh`) | Windows (`cmd.exe`) | Windows (`PowerShell`) | Cross-Platform Failure Risk |
| :--- | :--- | :--- | :--- | :--- |
| **Inline Env Var** | `FOO=bar command` | `set FOO=bar && command` | `$env:FOO="bar"; command` | Syntax error (`FOO` is not recognized as an internal or external command) |
| **Recursive Delete** | `rm -rf <path>` | `rd /s /q <path>` (or `del /s /q`) | `Remove-Item -Recurse -Force` | Command not found: `rm` |
| **Make Directory** | `mkdir -p <path>` | `mkdir <path>` (errors if exists) | `New-Item -ItemType Directory` | Flag not recognized: `-p` |
| **Sequential Exec** | `cmd1; cmd2` | `cmd1 & cmd2` | `cmd1; cmd2` | Syntax error with `;` in `cmd.exe` |
| **Path Separators** | `/` (always valid) | `\` (required by some native tools) | `/` or `\` | Mismatched slashes break argument parsing |
| **Empty File Touch** | `touch <file>` | `type nul > <file>` | `New-Item -ItemType File` | Command not found: `touch` |

---

## 2. The Cost of Polyfills & The Modern Alternatives

Compatibility helpers may still be needed for supported runtimes, external commands or behavior not covered by a proposed replacement. Retain a compatibility dependency when equivalence is unproven. The candidates below are not a mandatory purge list; any removal and lockfile synchronization require applicable approval.

### 1. `rimraf` (Elimination)
* **Assessment**: Inspect the installed dependency tree and required deletion semantics; popularity alone is not an adoption or removal criterion.
* **The Native Alternative** (Available since Node.js v14.14.0):
  ```json
  "clean": "node -e \"fs.rmSync('dist', { recursive: true, force: true })\""
  ```
  Or in Bun:
  ```json
  "clean": "rm -rf dist"
  ```
  *(The Bun Shell implements `rm` internally on all platforms, including Windows).*

### 2. `cross-env` (Elimination)
* **The Problem**: Wraps script execution in a custom Node child process just to set environment variables on Windows.
* **The Native Alternatives**:
  - **Node.js 20.6.0+**: Built-in `.env` file loading:
    ```json
    "build": "node --env-file=.env.production ./build.js"
    ```
  - **Inline JavaScript**:
    ```json
    "start:prod": "node -e \"process.env.NODE_ENV='production'; require('./server')\""
    ```
  - **Bun**: Supports standard inline environment assignment natively on Windows:
    ```json
    "build": "NODE_ENV=production bun build ./src/index.ts"
    ```

### 3. `mkdirp` (Elimination)
* **The Native Alternative** (Available since Node.js v10.12.0):
  ```json
  "prepare": "node -e \"fs.mkdirSync('dist', { recursive: true })\""
  ```

### 4. `shx` (Elimination)
* **Assessment**: Inspect actual helper/runtime use and measure overhead on a comparable workload before claiming a gain.
* **The Native Alternative**: Create a small, dedicated JavaScript script under `scripts/` (e.g. `scripts/bundle.js`) using standard `node:fs` methods.

---

## 3. High-Performance Shell Execution with The Bun Shell (`$`)

An in-process shell can avoid an extra operating-system shell layer for some commands. That is not proof of no external child process, identical behavior on every OS or measured latency savings. Check built-ins and external commands separately against the actual supported runtime and target matrix.

### Key Capabilities of `bun:shell`

```typescript
import { $ } from "bun";

// 1. Illustrative filesystem commands; verify behavior on the approved target matrix
await $`rm -rf ./dist && mkdir -p ./dist`;

// 2. Direct streaming into JavaScript memory without temporary files
const packageJson = await $`cat package.json`.json();
const branch = (await $`git rev-parse --abbrev-ref HEAD`.text()).trim();

// 3. Pipe directly between in-memory JS buffers and CLI tools
const input = Buffer.from("hello world");
const response = await $`gzip < ${input}`;

// 4. In-process environment setting
await $`FOO=bar bun run ./service.ts`;
```

### Syscall Reduction & Performance Impact
Do not assign universal timing, syscall or process-count savings. Record comparable baseline/workload measurements when actually performed; otherwise label expected impacts as hypotheses or not measured.

---

## 4. Security: Hardening Against Command Injection

A major vulnerability in shell automation scripts is the unescaped concatenation of external arguments (e.g. Git commit messages, filenames, URLs):

### ❌ Vulnerable Anti-Pattern
```typescript
import { execSync } from "node:child_process";

// DANGEROUS: If branchName contains '; rm -rf /', command injection occurs!
function checkout(branchName: string) {
  execSync(`git checkout ${branchName}`);
}
```

### ✅ Hardened Pattern (Parameterized API)
```typescript
import { execFileSync } from "node:child_process";

// No shell-string interpolation; validate option-like arguments and operation scope separately
function checkout(branchName: string) {
  execFileSync("git", ["checkout", branchName], { stdio: "inherit" });
}
```

### ✅ Hardened Pattern (The Bun Shell Auto-Escaping)
```typescript
import { $ } from "bun";

// Template escaping is not validation of executable options, paths or operation scope
function checkout(branchName: string) {
  return $`git checkout ${branchName}`;
}
```

---

## 5. Verification Checklist for Cross-Platform Automation

Before approving automation scripts:
- [ ] Validate paths for the actual target tools/shells; do not impose one separator universally.
- [ ] No inline Unix assignments (`FOO=bar`) in `package.json` scripts targeting Node unless wrapped in a cross-platform helper.
- [ ] Retain helpers unless an approved replacement covers required runtime compatibility and behavior.
- [ ] Deletions affect only approved paths; inspect symlink/path effects and preserve required failure behavior. Recursive/force flags are not mandatory.
- [ ] Quotes inside `package.json` scripts are escaped with `\"`.
- [ ] Confirm whether a dry-run actually avoids mutations before using it. Test approved success/error exit codes and side effects only in authorized fixtures.
- [ ] Record actual OS/shell/runtime/runner executions. Syntax or emulation alone is not native OS proof; unexecuted targets remain not verified.
- [ ] Obtain separate installation/network/destructive-test permissions and exact content/destination approval before any report-file write.
