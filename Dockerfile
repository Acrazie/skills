FROM oven/bun:1-alpine AS build

WORKDIR /app

COPY site/package.json site/bun.lock ./site/
RUN cd site && bun install --frozen-lockfile

COPY site ./site
COPY skills ./skills
COPY CHANGELOG.md ./CHANGELOG.md

RUN cd site && bun run build

FROM ghcr.io/nginx/nginx-unprivileged:alpine@sha256:b9241c6e7b8e9a862f129d8d4199ab64b10390949a78bdd5603379b32c844083 AS runtime-base

COPY --chown=101:101 nginx.conf /etc/nginx/nginx.conf

USER 101:101
EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD wget --spider --quiet http://127.0.0.1:8080/healthz

# CI supplies the site output already built and tested in this job.
# A named context keeps generated dist files out of the normal source context.
FROM runtime-base AS runtime-prebuilt
COPY --from=site-dist --chown=101:101 / /usr/share/nginx/html/

# Keep standalone/default builds self-contained.
FROM runtime-base AS runtime
COPY --from=build --chown=101:101 /app/site/dist/ /usr/share/nginx/html/
