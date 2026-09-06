# Plan: Extract Lefthook Hook Scripts and Translate CONTEXT.md to English

## Goal
Extract shell commands from `lefthook.yml` into modular, testable bash scripts located in `scripts/hooks/`, reference them cleanly inside `lefthook.yml`, and rewrite `CONTEXT.md` in English to adhere to repository documentation standards.

## Current Context / Assumptions
- `lefthook.yml` currently has inline bash scripts for:
  1. `check-forbidden-files` (pre-commit): prevents committing `.skill-refiner/`, `.skill-improver/`, `.DS_Store`, preview HTML, and internal `skills/*/docs/`.
  2. `validate-skills` (pre-commit): checks YAML frontmatter (`name:`, `description:`) on staged `SKILL.md` files.
  3. `check-skill-structure` (pre-push): checks that every directory under `skills/*/` contains `SKILL.md` and `agents/openai.yaml`.
- Inline multiline scripts in YAML are harder to unit-test independently, lack syntax highlighting/linting (ShellCheck), and clutter the configuration file.
- Lefthook supports two clean extraction patterns:
  - Approach A (Dedicated commands calling standalone scripts): `run: ./scripts/hooks/<script-name>.sh {staged_files}`
  - Approach B (Lefthook native file scripts): placing executable scripts in `.lefthook/pre-commit/<script-name>`. However, `.lefthook/` is in `.gitignore`, so tracked repository scripts belong in `scripts/hooks/`.
- `CONTEXT.md` was created in French ("Vocabulaire des skills Acrazie", "Famille Jenkins", etc.) whereas all repository architecture docs, guides, and metadata files must be in English.

## Architecture / Proposed Approach
1. Create a dedicated directory `/Users/acrazie/Documents/ProjectPerso/skills/scripts/hooks/` containing three standalone executable bash scripts (`check-forbidden-files.sh`, `validate-skills.sh`, and `check-skill-structure.sh`).
2. Simplify `/Users/acrazie/Documents/ProjectPerso/skills/lefthook.yml` so each hook command delegates directly to its corresponding script with `{staged_files}` passed when applicable.
3. Rewrite `/Users/acrazie/Documents/ProjectPerso/skills/CONTEXT.md` in English following standard domain terminology (matching Matt Pocock's ubiquitous language pattern).
4. Verify each script standalone with both positive (pass) and negative (fail) conditions, and verify `lefthook.yml` syntax.

---

## Step-by-Step Tasks

### Task 1: Create `scripts/hooks/check-forbidden-files.sh`
- **Path**: `/Users/acrazie/Documents/ProjectPerso/skills/scripts/hooks/check-forbidden-files.sh`
- **Action**: Create executable script that scans staged files against forbidden regex patterns.
- **Content**:
```bash
#!/usr/bin/env bash
set -euo pipefail

# Scans staged files for forbidden internal, cache, or temporary patterns.
forbidden=$(git diff --cached --name-only | grep -E '(\.skill-refiner/|\.skill-improver/|\.DS_Store|assets/.*-(preview|variants)\.html|skills/[^/]+/docs/)' || true)

if [ -n "$forbidden" ]; then
  echo "Error: Attempting to commit forbidden or internal files:" >&2
  echo "$forbidden" >&2
  exit 1
fi
```
- **Verification Command**:
```bash
chmod +x scripts/hooks/check-forbidden-files.sh
./scripts/hooks/check-forbidden-files.sh
```
- **Expected Output**: Exit code 0 (no output if no forbidden files are currently staged).

---

### Task 2: Create `scripts/hooks/validate-skills.sh`
- **Path**: `/Users/acrazie/Documents/ProjectPerso/skills/scripts/hooks/validate-skills.sh`
- **Action**: Create executable script that accepts staged file paths as arguments and checks frontmatter integrity.
- **Content**:
```bash
#!/usr/bin/env bash
set -euo pipefail

# Validates that given SKILL.md files contain valid YAML frontmatter, name, and description.
if [ "$#" -eq 0 ]; then
  exit 0
fi

for file in "$@"; do
  if [ -f "$file" ]; then
    if ! head -n 1 "$file" | grep -q '^---'; then
      echo "Error: $file missing YAML frontmatter" >&2
      exit 1
    fi
    if ! grep -q '^name:' "$file"; then
      echo "Error: $file missing 'name' in frontmatter" >&2
      exit 1
    fi
    if ! grep -q '^description:' "$file"; then
      echo "Error: $file missing 'description' in frontmatter" >&2
      exit 1
    fi
  fi
done
```
- **Verification Command**:
```bash
chmod +x scripts/hooks/validate-skills.sh
./scripts/hooks/validate-skills.sh skills/svg-icon-designer-acrazie/SKILL.md
```
- **Expected Output**: Exit code 0 (silent pass).

---

### Task 3: Create `scripts/hooks/check-skill-structure.sh`
- **Path**: `/Users/acrazie/Documents/ProjectPerso/skills/scripts/hooks/check-skill-structure.sh`
- **Action**: Create executable script that verifies every folder under `skills/*/` has `SKILL.md` and `agents/openai.yaml`.
- **Content**:
```bash
#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"

for dir in "$REPO_ROOT"/skills/*/; do
  if [ -d "$dir" ]; then
    skill_name="$(basename "$dir")"
    if [ ! -f "${dir}SKILL.md" ]; then
      echo "Error: Missing SKILL.md in skills/$skill_name" >&2
      exit 1
    fi
    if [ ! -f "${dir}agents/openai.yaml" ]; then
      echo "Error: Missing agents/openai.yaml in skills/$skill_name" >&2
      exit 1
    fi
  fi
done

echo "All skills match required directory structure."
```
- **Verification Command**:
```bash
chmod +x scripts/hooks/check-skill-structure.sh
./scripts/hooks/check-skill-structure.sh
```
- **Expected Output**:
`All skills match required directory structure.` (Exit code 0).

---

### Task 4: Refactor `lefthook.yml` to Invoke Extracted Scripts
- **Path**: `/Users/acrazie/Documents/ProjectPerso/skills/lefthook.yml`
- **Action**: Replace inline scripts with calls to `scripts/hooks/*.sh`.
- **Content**:
```yaml
pre-commit:
  parallel: true
  commands:
    check-forbidden-files:
      run: ./scripts/hooks/check-forbidden-files.sh
    validate-skills:
      glob: "skills/*/SKILL.md"
      run: ./scripts/hooks/validate-skills.sh {staged_files}

pre-push:
  commands:
    check-skill-structure:
      run: ./scripts/hooks/check-skill-structure.sh
```
- **Verification Command**:
```bash
python3 -c "import yaml; yaml.safe_load(open('lefthook.yml'))"
```
- **Expected Output**: Exit code 0 (valid YAML).

---

### Task 5: Rewrite `CONTEXT.md` in English
- **Path**: `/Users/acrazie/Documents/ProjectPerso/skills/CONTEXT.md`
- **Action**: Translate and format all domain definitions into concise English.
- **Content**:
```markdown
# Acrazie Skills Context & Domain Glossary

This document defines the ubiquitous language and domain vocabulary across the skills repository.

## Jenkins Family

**Jenkins Parent**:
The `jenkins-devops-acrazie` skill, responsible for approving, orchestrating, and validating pipeline modifications and production deployments across application repositories.

**Symfony Specialist**:
The `jenkins-symfony-php-acrazie` specialist skill, dedicated to interpreting Symfony application architecture, CI requirements, and runtime dependencies for the Jenkins Parent. It provides CI constraints without directly executing deployment stages.
*Avoid*: Generic PHP specialist, Symfony deployer.

**Python Specialist**:
The `jenkins-python-acrazie` specialist skill, dedicated to Python packaging, testing (pytest/tox), and runtime containerization for Jenkins pipelines.

## Skill Lifecycle & Refinement

**Skill Refiner**:
The interactive feedback workflow (`skill-refiner-acrazie`) that observes real skill usage, records append-only journals under `.skill-refiner/`, and updates living Architectural Decision Records (ADRs).
*Avoid*: Skill Improver (deprecated legacy name).

**Audit Record**:
A formal, read-only technical evaluation artifact created under `docs/audits/` via `audit-repository-acrazie`.
```
- **Verification Command**:
```bash
grep -iE "(vocabulaire|propre aux|responsable de|dédié|consacré)" CONTEXT.md || echo "No French text found"
```
- **Expected Output**: `No French text found` (Exit code 0).

---

## Tests & Validation Plan
1. **Script Executable Permissions**:
   Verify with `test -x scripts/hooks/check-forbidden-files.sh && test -x scripts/hooks/validate-skills.sh && test -x scripts/hooks/check-skill-structure.sh`.
2. **Negative Test for `check-forbidden-files.sh`**:
   Verify that simulating a forbidden staged file triggers exit code 1.
3. **Negative Test for `validate-skills.sh`**:
   Run against a dummy invalid file and verify error output and exit code 1.
4. **Negative Test for `check-skill-structure.sh`**:
   Verify behavior when a required file is missing.
5. **Git Status Check**:
   Run `git status --short` to ensure only the planned files are created/modified (`scripts/hooks/*`, `lefthook.yml`, `CONTEXT.md`) and no unwanted files are tracked.

---

## Risks, Tradeoffs, and Open Questions
- **Tradeoff (Inline vs Extracted)**:
  - *Extracted (Proposed)*: Much cleaner `lefthook.yml`, allows running scripts manually in terminal and CI without installing Lefthook, easier to debug and lint with ShellCheck.
  - *Inline*: Kept everything in a single file, but hard to read, multiline YAML escaping issues, and unportable outside Lefthook.
  - *Verdict*: Extraction to `scripts/hooks/` is the standard best practice.
- **Lefthook execution environment**:
  - Scripts assume bash (`#!/usr/bin/env bash`) which is standard across macOS, Linux, and WSL2.
