# Cross-Platform Script Portability & Shell Hardening Guide

Comprehensive reference for eliminating operating system hazards in `package.json` scripts, purging third-party polyfills, and hardening command execution against shell injection vulnerabilities.

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

For years, the JavaScript ecosystem relied on micro-packages to smooth over these differences. However, modern Node.js and Bun have made these polyfills entirely obsolete:

### 1. `rimraf` (Elimination)
* **The Problem**: Installed tens of millions of times weekly; pulls in transitive dependencies just to delete a directory.
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
* **The Problem**: Bundles ShellJS inside `node_modules`. Invoking `shx` spawns a heavy Node runtime instance for simple file operations, adding 50–150ms per script command.
* **The Native Alternative**: Create a small, dedicated JavaScript script under `scripts/` (e.g. `scripts/bundle.js`) using standard `node:fs` methods.

---

## 3. High-Performance Shell Execution with The Bun Shell (`$`)

When running inside the Bun runtime, Bun integrates a native, cross-platform shell interpreter written in Zig/Rust. It completely bypasses the operating system's subshell (`sh -c` or `cmd.exe`) and executes commands in-process with zero subprocess spawn overhead.

### Key Capabilities of `bun:shell`

```typescript
import { $ } from "bun";

// 1. Cross-platform filesystem commands work identically on Windows and Linux
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
* **OS Fork/Spawn**: Spawning a shell subprocess costs **7 to 10 milliseconds** and thousands of context switches.
* **The Bun Shell**: In-process execution reduces latency to **microseconds** ($O(1)$ syscalls).

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

// SAFE: Arguments are passed as an array to execve, bypassing shell interpolation
function checkout(branchName: string) {
  execFileSync("git", ["checkout", branchName], { stdio: "inherit" });
}
```

### ✅ Hardened Pattern (The Bun Shell Auto-Escaping)
```typescript
import { $ } from "bun";

// SAFE: Bun Shell template literals automatically escape and sanitize variables
function checkout(branchName: string) {
  return $`git checkout ${branchName}`;
}
```

---

## 5. Verification Checklist for Cross-Platform Automation

Before approving automation scripts:
- [ ] No hardcoded backslashes `\` in path arguments; use forward slashes `/` universally.
- [ ] No inline Unix assignments (`FOO=bar`) in `package.json` scripts targeting Node unless wrapped in a cross-platform helper.
- [ ] No deprecated polyfills (`rimraf`, `cross-env`, `shx`, `mkdirp`) present in `devDependencies`.
- [ ] All deletions use recursive force parameters (`fs.rmSync(dir, { recursive: true, force: true })` or `rm -rf`).
- [ ] Quotes inside `package.json` scripts are escaped with `\"`.
- [ ] Dry-run executions return exit code `0` on clean state and appropriately bubble non-zero codes on failure.
