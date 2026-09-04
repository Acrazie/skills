#!/usr/bin/env sh
set -eu
: "${TARGET_ENV:?TARGET_ENV required}"
: "${IMAGE_REF:?known-good IMAGE_REF required}"
printf 'rollback %s to %s\n' "$TARGET_ENV" "$IMAGE_REF"
