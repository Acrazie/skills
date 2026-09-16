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

You will receive an acknowledgment within 48 hours, followed by updates on triage and mitigation.
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
2. Install dependencies:
   ```bash
   <install-command>
   ```
3. Set up pre-commit hooks:
   ```bash
   <hooks-install-command>
   ```

## Commit Conventions

This project enforces [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` A new user-facing feature
- `fix:` A bug fix
- `docs:` Documentation only changes
- `refactor:` Code change that neither fixes a bug nor adds a feature
- `test:` Adding or updating tests
- `chore:` Routine tasks, dependency updates, tooling

## Pull Request Process

1. Create a dedicated branch (`feat/<branch-name>` or `fix/<branch-name>`).
2. Run local tests and linters before committing:
   ```bash
   <lint-command>
   <test-command>
   ```
3. Open a Pull Request referencing any related issues.
4. Ensure CI checks pass.
```

---

## 3. GitHub Issue Templates (`.github/ISSUE_TEMPLATE/`)

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

## 4. Pull Request Template (`.github/PULL_REQUEST_TEMPLATE.md`)

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

## 5. Licenses (`LICENSE`)

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

## 6. Curated `.gitignore` Base

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

# Common build & logs
logs
*.log
dist/
build/
coverage/
```
