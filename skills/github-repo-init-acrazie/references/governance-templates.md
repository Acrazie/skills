# Repository Governance & Documentation Templates

Standard templates for repository health, security policies, contribution guidelines, and community governance.

---

## 1. Security Policy (`SECURITY.md`)

```markdown
# Security Policy

## Supported Versions

Only the latest stable release receives active security updates and patches.

| Version | Supported          |
| ------- | ------------------ |
| >= 1.0  | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

We take the security of this project seriously. If you discover a security vulnerability, please do **NOT** open a public issue.

Instead, please report it privately:

1. **GitHub Security Advisory** (Recommended): Go to the **Security** tab of this repository, select **Advisories**, and click **Report a vulnerability**.
2. **Email**: Alternatively, send an email to `<security-email>` with:
   - A clear description of the vulnerability
   - Steps or proof-of-concept to reproduce the issue
   - Impact assessment
```

---

## 2. Contribution Guidelines (`CONTRIBUTING.md`)

```markdown
# Contributing Guide

Thank you for your interest in contributing!

## Code of Conduct

Please be respectful and constructive in all interactions.

## Development Setup

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd <repo-name>
   ```
2. Run the automated setup script (or install manually):
   ```bash
   ./scripts/setup.sh
   # Or manually:
   # <install-command>
   # <hooks-install-command>
   ```

## Branching Strategy & Environments

This repository uses **<Trunk-Based Development | Environment Branches>**:

- `main`: <Production stable branch | Production deployment>
- `staging` *(if applicable)*: Pre-production QA and staging deployment
- `develop` *(if applicable)*: Integration branch for daily development

### Branch Naming Conventions
- `feat/<topic>`: New features or capabilities
- `fix/<topic>`: Bug fixes and patches
- `chore/<topic>`: Dependencies, tooling, or refactoring
- `docs/<topic>`: Documentation only changes

## Parallel Development with Git Worktrees

If you work on multiple features or with AI coding agents in parallel, use Git Worktrees to prevent branch collision:

```bash
# Using the helper script:
./scripts/worktree.sh add feat/<branch-name>

# Or manually:
git worktree add .worktrees/<branch-name> -b feat/<branch-name> origin/main
cd .worktrees/<branch-name>
```

When work is finished and the PR is merged:
```bash
./scripts/worktree.sh remove feat/<branch-name>
```

## Commit Conventions

This project enforces [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` A new user-facing feature
- `fix:` A bug fix
- `docs:` Documentation only changes
- `refactor:` Code change that neither fixes a bug nor adds a feature
- `test:` Adding or updating tests
- `chore:` Routine tasks, dependency updates, tooling

*Note: Never add automated co-author attributions.*

## Pull Request Process

1. Create your branch or worktree (`feat/<branch-name>` or `fix/<branch-name>`).
2. Run local tests and linters before committing:
   ```bash
   <lint-command>
   <test-command>
   ```
3. Open a Pull Request targeting `<main | develop>`.
4. Ensure CI checks pass.
```

---

## 3. Git Delivery & Workflow Specification (`docs/git-workflow.md`)

```markdown
# Repository Git & Delivery Workflow

This document serves as the authoritative source of truth for Git operations, branching strategy, commit standards, quality gates, and Pull Request procedures on this repository. Coding agents and contributors must adhere to these policies.

---

## 1. Branching Model & Environments

- **Default / Trunk Branch**: <main | master> (reflects production-ready code).
- **Direct Commits Prohibited**: Committing directly or pushing directly to the default branch is strictly forbidden.
- **Branch Naming**:
  - `feat/<topic>`: New features or capabilities
  - `fix/<topic>`: Bug fixes and patches
  - `chore/<topic>`: Dependencies, tooling, and refactoring
  - `docs/<topic>`: Documentation changes only

## 2. Parallel Development with Git Worktrees

To isolate concurrent tasks and avoid dirty working tree collisions (especially when working with AI agents):
- All feature work should be conducted inside dedicated worktrees under `.worktrees/<branch-name>`.
- The directory `.worktrees/` is gitignored.
- Use `./scripts/worktree.sh add <branch-name>` (or standard `git worktree add .worktrees/<branch-name> -b <branch-name> origin/<default-branch>`).
- Remove the worktree once the PR is merged: `./scripts/worktree.sh remove <branch-name>`.

## 3. Commit Conventions

This repository strictly enforces [Conventional Commits](https://www.conventionalcommits.org/):
- **Format**: `<type>(<optional-scope>): <concise description>`
- **Types**: `feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `ci`, `perf`.
- **Imperative Mood**: Use present tense ("add feature" instead of "added feature").
- **Attribution Invariant**: NEVER include co-author trailers (`Co-authored-by: ...` or equivalent automated attributions).

## 4. Pre-Commit Quality Gates

Before staging or committing any code:
1. **Hygiene**: Ensure no secrets, `.env*` files, build caches, or temporary directories are staged.
2. **Quality Verification**: Execute the repository quality checks:
   - `<lint-command>` (e.g. `npx lefthook run pre-commit` or linter/formatter)
   - `<test-command>` (e.g. test suite)
3. Do not bypass hooks or use `--no-verify`.

## 5. Delivery & Pull Request Protocol

When a task is complete:
1. **Push**: Push the feature branch to the remote: `git push -u origin <branch-name>`.
2. **PR Creation**: Open a Pull Request using GitHub CLI:
   - **Default State**: Open as **Draft** (`gh pr create --draft`) for review and verification unless explicitly requested as ready.
   - **Template**: Populate all sections defined in `.github/pull_request_template.md`.
   - **Target**: PR must target <main | develop>.
3. **Merge Strategy**: Squash-merge into the default branch with a clean Conventional Commit title.

## 6. Agent Autonomy Boundaries

- **Autonomous Actions**: Creating local branches or worktrees, staging relevant files, running tests/linters, and creating local commits.
- **Approval-Gated Actions**: Pushing to remote (`git push`), opening Pull Requests (`gh pr create`), deleting branches, or any destructive git operations require explicit confirmation.
```

---

## 4. Agent Guidelines Entrypoint (`AGENTS.md`)

```markdown
# <project-name> — Agent Guidelines

Instructions and standards for AI coding agents (Hermes, Codex, Claude Code, Cursor) working on this repository.

## Mission & Architecture
<concise-mission-and-architecture-overview>

## Git & Delivery Protocol
Follow the repository delivery workflow, commit rules, and branch policies defined in [docs/git-workflow.md](docs/git-workflow.md).
```

*Note: Maintain `CLAUDE.md` as a relative symlink to `AGENTS.md` (`ln -s AGENTS.md CLAUDE.md`).*

---

## 5. GitHub Issue Templates (`.github/ISSUE_TEMPLATE/`)

### Bug Report (`.github/ISSUE_TEMPLATE/bug_report.yml`)
```yaml
name: Bug Report
description: Report an issue or unexpected behavior
labels: ["bug"]
body:
  - type: markdown
    attributes:
      value: Thank you for reporting a bug! Please fill out the details below.
  - type: textarea
    id: description
    attributes:
      label: Description
      description: Clear and concise description of the bug.
    validations:
      required: true
  - type: textarea
    id: reproduction
    attributes:
      label: Steps to Reproduce
      description: Minimal reproducible steps.
      placeholder: |
        1. Run '...'
        2. Click on '...'
        3. See error
    validations:
      required: true
  - type: textarea
    id: environment
    attributes:
      label: Environment
      description: OS version, runtime/browser, package version.
```

### Feature Request (`.github/ISSUE_TEMPLATE/feature_request.yml`)
```yaml
name: Feature Request
description: Propose an idea or enhancement
labels: ["enhancement"]
body:
  - type: textarea
    id: problem
    attributes:
      label: Problem Statement
      description: What problem does this feature solve?
    validations:
      required: true
  - type: textarea
    id: solution
    attributes:
      label: Proposed Solution
      description: Clear description of what you want to happen.
    validations:
      required: true
```

---

## 6. Pull Request Template (`.github/PULL_REQUEST_TEMPLATE.md`)

```markdown
## Summary

Provide a concise description of the changes introduced by this PR.

## Related Issue

Closes #

## Type of Change

- [ ] Bug fix (non-breaking change fixing an issue)
- [ ] New feature (non-breaking change adding functionality)
- [ ] Breaking change (fix or feature that alters existing behavior)
- [ ] Documentation update
- [ ] Maintenance / Chore

## Checklist

- [ ] My code follows the project's style guidelines
- [ ] I have executed local linters and tests successfully
- [ ] I have updated documentation where appropriate
- [ ] My commit messages follow Conventional Commits
```

---

## 7. Licenses (`LICENSE`)

### MIT License
```text
MIT License

Copyright (c) <YEAR> <COPYRIGHT_HOLDER>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 8. Curated `.gitignore` Base

Always combine common OS / Editor ignores with stack-specific ignores:

```gitignore
# OS
.DS_Store
Thumbs.db

# Editors
.vscode/*
!.vscode/extensions.json
!.vscode/settings.json
.idea/
*.suo
*.ntvs*
*.njsproj

# Environment & Secrets
.env
.env.local
.env.*.local
*.pem
*.key

# Worktrees for parallel development
.worktrees/

# Common build & logs
logs
*.log
dist/
build/
coverage/
```
