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

This repository uses **<selected branch model>**. Full policy: [docs/git-workflow.md](docs/git-workflow.md).

- <list only actual base, environment, and PR target branches>

### Branch Naming Conventions
- <selected convention, or link to existing organization rule>

## Parallel Development

<Describe selected required/situational/no-worktree policy. Include this example only if the generated helper and `.worktrees/` location were selected.>

```bash
./scripts/worktree.sh add feat/<branch-name>
```

Before removing a worktree, verify no task, process, unmerged PR, or unpreserved changes still need it.

## Commit Conventions

<Describe selected staging, commit granularity, and message convention. Include Conventional Commits examples only if selected or already enforced.>

*Note: Never add automated co-author attributions.*

## Pull Request Process

1. Verify the remote base where one exists, then create the work branch or worktree according to policy.
2. Run local tests and linters before committing:
   ```bash
   <lint-command>
   <test-command>
   ```
3. Before push/PR, fetch and compare with the selected target. On failure or divergence, ask how to proceed rather than silently merge/rebase.
4. Follow the selected push approval, PR state/target, review, and merge policy in `docs/git-workflow.md`.
5. Ensure remote CI checks pass before claiming PR readiness.
```

---

## 3. Git Delivery & Workflow Specification (`docs/git-workflow.md`)

```markdown
# Repository Git & Delivery Workflow

This document serves as the authoritative source of truth for Git operations, branching strategy, commit standards, quality gates, and Pull Request procedures on this repository. Coding agents and contributors must adhere to these policies.

Adapt every policy below to discovered constraints and explicit interview answers. Omit inapplicable sections rather than publishing contradictory defaults. `AGENTS.md` and `CONTRIBUTING.md` must point to or accurately summarize this document. It must remain usable without invoking any Git skill.

---

## 1. Branching Model & Environments

- **Base Branch / PR Target**: <selected branches, by change type if needed>.
- **Direct Commit/Push Policy**: <selected rule, consistent with organization and branch protection>.
- **Branch Naming**: <selected prefixes or existing convention>.
- **Before New Work**: If a remote exists, fetch the base branch and verify the remote ref before creating a work branch. If verification fails, stop and ask whether to work offline; never claim that the base is current. A new repository without a remote can begin from its local initial branch.

## 2. Parallel Development with Git Worktrees

<Include only when worktrees are selected. State required or situational use, location, and whether a clean dedicated checkout suffices. If using `.worktrees/`, ignore it and reference the generated helper. Do not remove a worktree while a task, process, unmerged PR, or unpreserved change still needs it. Do not force removal.>

## 3. Commit Conventions

- **Staging**: <selected targeted-path or reviewed-tree policy>. Review status and diff first; exclude secrets, generated artifacts, and unrelated changes.
- **Commit Granularity**: <selected coherent-intent, per-task, or case-by-case rule>.
- **Message Convention**: <selected convention; describe Conventional Commits only if selected or already enforced>.
- **Attribution Invariant**: NEVER include co-author trailers (`Co-authored-by: ...` or equivalent automated attributions).

## 4. Pre-Commit Quality Gates

Before committing code:
1. **Hygiene**: Ensure no secrets, `.env*` files, build caches, or temporary directories are staged.
2. **Quality Verification**: Execute the repository quality checks:
   - `<lint-command>` (e.g. `npx lefthook run pre-commit` or linter/formatter)
   - `<test-command>` (e.g. test suite)
3. Do not bypass hooks or use `--no-verify`.

## 5. Delivery & Pull Request Protocol

When a task is complete:
1. **Remote Check**: Fetch and compare the work branch with the selected PR target before push/PR; repeat if a long task may have made this stale. On fetch failure or target divergence, report it and ask how to proceed. Do not silently merge, rebase, or force-push.
2. **Push Authorization**: <selected policy>. Never push directly to a branch where repository or organization rules prohibit it.
3. **PR Creation**: <selected authorization, Draft/ready default, target, required checks/review, and template>. Do not claim local checks prove remote CI passed.
4. **Merge Strategy**: <selected method consistent with branch rules; do not assume squash merge>.

## 6. Agent Autonomy Boundaries

- **Autonomous Actions**: <selected local actions, within repository/organization constraints>.
- **Approval-Gated Actions**: <selected publication actions>. Destructive Git operations require explicit confirmation. If an external skill or configuration conflicts with this policy, present both sources and ask the user to choose; never edit that external source by implication.
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
- [ ] My commits follow the repository's selected message convention
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

Always combine common OS / Editor ignores with stack-specific ignores. Add `.worktrees/` only if that location was selected:

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

# Common build & logs
logs
*.log
dist/
build/
coverage/
```
