#!/usr/bin/env bash
set -euo pipefail

# Links all skills in this monorepo into the local skill directories used by
# agent harnesses:
#   - ~/.hermes/skills : Hermes Agent
#   - ~/.agents/skills : Codex and other Agent Skills-compatible harnesses
#   - ~/.claude/skills : Claude Code (if directory exists)

REPO="$(cd "$(dirname "$0")/.." && pwd)"

DESTS=(
  "$HOME/.hermes/skills"
  "$HOME/.agents/skills"
)

if [ -d "$HOME/.claude/skills" ]; then
  DESTS+=("$HOME/.claude/skills")
fi

echo "Repository: $REPO"

for dest in "${DESTS[@]}"; do
  # Avoid circular linking if destination is inside repository
  if [ -L "$dest" ]; then
    resolved="$(readlink -f "$dest" || true)"
    case "$resolved" in
      "$REPO"|"$REPO"/*)
        echo "Skipping $dest: resolves into repo ($resolved)"
        continue
        ;;
    esac
  fi

  mkdir -p "$dest"
  echo "Linking skills to $dest..."

  for skill_dir in "$REPO"/skills/*/; do
    if [ -f "${skill_dir}SKILL.md" ]; then
      skill_name="$(basename "$skill_dir")"
      target="$dest/$skill_name"

      if [ -e "$target" ] && [ ! -L "$target" ]; then
        echo "  [warning] $target already exists and is not a symlink. Skipping."
        continue
      fi

      ln -sfn "$skill_dir" "$target"
      echo "  [linked] $skill_name -> $target"
    fi
  done
done

echo "Done."
