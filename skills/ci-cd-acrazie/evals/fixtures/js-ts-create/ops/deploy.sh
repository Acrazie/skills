#!/usr/bin/env sh
set -eu
: "${TARGET_ENV:?TARGET_ENV is required}"
: "${IMAGE_REF:?IMAGE_REF must be an immutable image reference}"
printf 'deploy %s to %s\n' "$IMAGE_REF" "$TARGET_ENV"
