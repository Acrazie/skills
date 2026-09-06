# Plan: Complete Repository Release Management

## Goal
Establish a robust, automated, and observable release management pipeline for the `Acrazie/skills` monorepo using Conventional Commits, GitHub Actions, Release Please, and standalone packaging & validation scripts.

## Current Context / Assumptions
- **Git & Branching**: Default branch is `main`. The working tree currently contains unstaged configuration files (`.github/workflows/release-please.yml`, `release-please-config.json`, `.release-please-manifest.json`, `lefthook.yml`, `scripts/hooks/*`, `AGENTS.md`, `CONTEXT.md`).
- **Release Automation**: Release Please is already partially wired in `release-please-config.json` (strategy `simple`, target `CHANGELOG.md`) and `.release-please-manifest.json` (`"." : "1.0.0"`).
- **Distribution Scope**: The repository ships 11 skills to [skills.sh](https://skills.sh) via Git cloning. Optional standalone `.skill` zip packages are stored in gitignored `dist/` for offline or direct manual distribution.
- **Rules & Constraints**:
  - All documentation, scripts, workflows, and commit messages must be in English.
  - Commits must adhere strictly to Conventional Commits format (`feat:`, `fix:`, `chore:`, etc.) to allow Release Please to detect changes and generate semantic tags and changelogs.
  - No secrets in config files; safe for public GitHub repository.

## Architecture / Proposed Approach
1. **Packaging & Archive Script (`scripts/package-skills.sh`)**:
   - Provide a deterministic, standalone script that builds `.skill` zip packages for each skill in `skills/*/` into `dist/`.
   - Ensure `evals/`, `docs/`, `.skill-refiner/`, and temporary preview HTML files are excluded from the zip archives.
   - Verify archive integrity with `unzip -t`.
2. **Release Workflow Augmentation (`.github/workflows/release-please.yml`)**:
   - Keep `release-please` as the orchestrator on push to `main`.
   - Add a follow-up job `build-release-assets` that triggers only when a new release tag is created by Release Please.
   - Build all `.skill` packages in GitHub Actions runner and upload them as GitHub Release binary assets.
3. **Pre-release Verification Script (`scripts/verify-release.sh`)**:
   - A single local command to run all sanity checks before pushing: hook scripts (`check-forbidden-files.sh`, `validate-skills.sh`, `check-skill-structure.sh`), build all packages, test zip integrity, and ensure git cleanliness.
4. **Release Process Documentation (`docs/releases.md` & `AGENTS.md`)**:
   - Document the end-to-end lifecycle: how PRs get merged, how Release Please opens a Release PR with `CHANGELOG.md`, and how merging the Release PR cuts a GitHub tag, creates a GitHub Release, and publishes release assets.

---

## Step-by-Step Tasks

### Task 1: Create `scripts/package-skills.sh`
- **Path**: `/Users/acrazie/Documents/ProjectPerso/skills/scripts/package-skills.sh`
- **Action**: Create an executable bash script that packages each valid skill into `dist/<skill-name>.skill` (zip format) excluding internal/dev artifacts.
- **Content**:
```bash
#!/usr/bin/env bash
set -euo pipefail

# Packages all skills in skills/ into dist/<skill-name>.skill archives.
# Excludes development artifacts, evals, internal docs, and journals.

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DIST_DIR="$REPO_ROOT/dist"

mkdir -p "$DIST_DIR"
rm -f "$DIST_DIR"/*.skill

echo "Packaging skills from $REPO_ROOT/skills to $DIST_DIR..."

for skill_dir in "$REPO_ROOT"/skills/*/; do
  if [ -d "$skill_dir" ]; then
    skill_name="$(basename "$skill_dir")"

    # Skip temporary or non-skill workspace folders
    if [[ "$skill_name" == *-workspace ]]; then
      continue
    fi

    if [ ! -f "${skill_dir}SKILL.md" ]; then
      continue
    fi

    target_archive="$DIST_DIR/${skill_name}.skill"
    echo "  -> Building $skill_name.skill"

    # Package from inside the specific skill directory for clean relative roots
    (
      cd "$skill_dir"
      zip -q -r "$target_archive" . \
        -x "evals/*" \
        -x "docs/*" \
        -x ".skill-refiner/*" \
        -x ".skill-improver/*" \
        -x "assets/*-preview.html" \
        -x "assets/*-variants.html" \
        -x "*.DS_Store" \
        -x "__pycache__/*"
    )

    # Smoke check archive integrity
    unzip -t -q "$target_archive"
  fi
done

echo "Successfully packaged all skills:"
ls -lh "$DIST_DIR"/*.skill
```
- **Verification Command**:
```bash
chmod +x scripts/package-skills.sh
./scripts/package-skills.sh
```
- **Expected Output**:
`Successfully packaged all skills:` followed by a list of 11 `.skill` files in `dist/`.

---

### Task 2: Create `scripts/verify-release.sh`
- **Path**: `/Users/acrazie/Documents/ProjectPerso/skills/scripts/verify-release.sh`
- **Action**: Create a unified pre-release validation script that chains all checks before opening PRs or merging.
- **Content**:
```bash
#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo "=== 1. Checking skill directory structure ==="
"$REPO_ROOT/scripts/hooks/check-skill-structure.sh"

echo "=== 2. Validating SKILL.md frontmatters ==="
for skill_md in "$REPO_ROOT"/skills/*/SKILL.md; do
  "$REPO_ROOT/scripts/hooks/validate-skills.sh" "$skill_md"
done
echo "All SKILL.md frontmatters are valid."

echo "=== 3. Packaging and testing .skill archives ==="
"$REPO_ROOT/scripts/package-skills.sh"

echo "=== 4. Checking forbidden staged files ==="
"$REPO_ROOT/scripts/hooks/check-forbidden-files.sh"

echo "=== All release checks passed successfully! ==="
```
- **Verification Command**:
```bash
chmod +x scripts/verify-release.sh
./scripts/verify-release.sh
```
- **Expected Output**:
All 4 sections complete with exit code 0 and `All release checks passed successfully!`.

---

### Task 3: Enhance `.github/workflows/release-please.yml` to Attach Release Assets
- **Path**: `/Users/acrazie/Documents/ProjectPerso/skills/.github/workflows/release-please.yml`
- **Action**: Add an automated step that builds packages with `scripts/package-skills.sh` and uploads `.skill` bundles as GitHub Release assets whenever a release is published.
- **Content**:
```yaml
name: release-please

on:
  push:
    branches:
      - main

permissions:
  contents: write
  pull-requests: write

jobs:
  release-please:
    runs-on: ubuntu-latest
    outputs:
      release_created: ${{ steps.release.outputs.release_created }}
      tag_name: ${{ steps.release.outputs.tag_name }}
    steps:
      - id: release
        uses: googleapis/release-please-action@v4
        with:
          config-file: release-please-config.json
          manifest-file: .release-please-manifest.json

  upload-release-assets:
    needs: release-please
    if: ${{ needs.release-please.outputs.release_created == 'true' }}
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Build skill archives
        run: |
          chmod +x scripts/package-skills.sh
          ./scripts/package-skills.sh

      - name: Attach .skill assets to GitHub Release
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          tag="${{ needs.release-please.outputs.tag_name }}"
          gh release upload "$tag" dist/*.skill --clobber
```
- **Verification Command**:
```bash
head -n 25 .github/workflows/release-please.yml
```
- **Expected Output**: Inspect YAML structure and step ordering.

---

### Task 4: Document Release Process in `AGENTS.md` and `README.md`
- **Path**: `/Users/acrazie/Documents/ProjectPerso/skills/AGENTS.md`
- **Action**: Add a dedicated "Release Lifecycle" section to `AGENTS.md` specifying how versions, PRs, and tags are triggered.
- **Diff specification**:
  - Document that merging to `main` with Conventional Commits triggers Release Please.
  - Release Please automatically creates and updates a release PR with generated `CHANGELOG.md`.
  - Merging the release PR tags the release, creates a GitHub Release, and uploads `dist/*.skill` packages.
- **Verification Command**:
```bash
grep -n "Release Lifecycle" AGENTS.md
```
- **Expected Output**: Line match showing the newly documented section.

---

## Tests & Validation Plan
1. **Package Integrity Test**:
   - Run `./scripts/package-skills.sh`.
   - Verify every `.skill` file contains `SKILL.md` and `agents/openai.yaml` at root using `unzip -l dist/svg-icon-designer-acrazie.skill`.
   - Verify internal directories like `.skill-refiner/` or `evals/` are excluded.
2. **End-to-End Local Verification**:
   - Run `./scripts/verify-release.sh`.
   - Ensure all validation steps pass cleanly without errors.
3. **Git Status & Boundary Check**:
   - Run `git status --short`.
   - Ensure `dist/` remains completely ignored by Git.

---

## Risks, Tradeoffs, and Open Questions
- **Single vs Multi-Package Versioning**:
  - *Current configuration*: Monorepo root release (`"." : "1.0.0"` in `.release-please-manifest.json`). This cuts a unified repository release (e.g., `v1.1.0`), which matches how `skills.sh` consumes the repo as a whole (`Acrazie/skills`).
  - *Tradeoff*: Individual skills do not get independent git tags. If independent skill versioning is ever desired in the future, Release Please supports multi-package monorepos, but unified release is much simpler and directly aligns with the current repository structure.
- **Token Permissions**:
  - `secrets.GITHUB_TOKEN` needs write access for contents and pull-requests, which is explicitly declared in `permissions:`.
