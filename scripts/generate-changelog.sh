#!/usr/bin/env bash
set -euo pipefail

# Check if git-cliff is installed
if ! command -v git-cliff >/dev/null 2>&1; then
  echo "Error: git-cliff is not installed." >&2
  echo "Install it via: brew install git-cliff (macOS) or cargo install git-cliff" >&2
  exit 1
fi

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

MODE="${1:---preview}"

case "$MODE" in
  --preview|-p)
    echo "=== Previewing unreleased changelog ==="
    git-cliff --unreleased
    ;;
  --all|-a)
    echo "=== Previewing full changelog ==="
    git-cliff
    ;;
  --latest|-l)
    echo "=== Previewing latest release notes ==="
    git-cliff --latest --strip header
    ;;
  --write|-w)
    echo "=== Writing full changelog to CHANGELOG.md ==="
    git-cliff --output CHANGELOG.md
    echo "CHANGELOG.md updated successfully."
    ;;
  *)
    echo "Usage: $0 [--preview|--all|--latest|--write]"
    exit 1
    ;;
esac
