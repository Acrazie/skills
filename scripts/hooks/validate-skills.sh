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
