#!/usr/bin/env bash
set -euo pipefail

# Scans staged added/modified/copied files for forbidden internal, cache, or temporary patterns.
# Note: Deletions (--diff-filter=d) are allowed so deleted legacy forbidden files can be committed.
forbidden=$(git diff --cached --name-only --diff-filter=d | grep -E '(\.skill-refiner/|\.skill-improver/|\.DS_Store|assets/.*-(preview|variants)\.html|skills/[^/]+/docs/)' || true)

if [ -n "$forbidden" ]; then
  echo "Error: Attempting to commit forbidden or internal files:" >&2
  echo "$forbidden" >&2
  exit 1
fi
