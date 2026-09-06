#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"

for dir in "$REPO_ROOT"/skills/*/; do
  if [ -d "$dir" ]; then
    skill_name="$(basename "$dir")"
    # Skip temporary test workspaces or non-skill directories ending with -workspace
    if [[ "$skill_name" == *-workspace ]]; then
      continue
    fi
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
