#!/usr/bin/env bash
set -euo pipefail

# Scans added/modified/copied files for forbidden internal, cache, or temporary patterns.
# Note: Deletions (--diff-filter=d) are allowed so deleted legacy forbidden files can be committed.
# If a revision range is provided as $1 (e.g. in CI PR diff), inspect that range; otherwise inspect staged files.
if [ -n "${1:-}" ]; then
  forbidden=$(git diff --name-only "$1" --diff-filter=d | grep -E '(\.worktrees/|\.hermes/|\.skill-refiner/|\.skill-improver/|\.DS_Store|assets/.*-(preview|variants)\.html|skills/[^/]+/docs/)' || true)
else
  forbidden=$(git diff --cached --name-only --diff-filter=d | grep -E '(\.worktrees/|\.hermes/|\.skill-refiner/|\.skill-improver/|\.DS_Store|assets/.*-(preview|variants)\.html|skills/[^/]+/docs/)' || true)
fi

if [ -n "$forbidden" ]; then
  echo "Error: Detected forbidden or internal files:" >&2
  echo "$forbidden" >&2
  exit 1
fi
