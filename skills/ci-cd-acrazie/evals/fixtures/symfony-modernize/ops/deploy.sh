#!/usr/bin/env sh
set -eu
: "${TARGET_ENV:?TARGET_ENV required}"
: "${IMAGE_REF:?IMAGE_REF required}"
printf 'deploy %s to %s\n' "$IMAGE_REF" "$TARGET_ENV"
