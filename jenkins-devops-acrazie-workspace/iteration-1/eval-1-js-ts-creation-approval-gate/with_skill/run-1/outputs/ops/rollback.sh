#!/usr/bin/env sh
set -eu
: "${TARGET_ENV:?TARGET_ENV is required}"
: "${IMAGE_REF:?IMAGE_REF must identify the known-good image}"
printf 'rollback %s to %s\n' "$TARGET_ENV" "$IMAGE_REF"
