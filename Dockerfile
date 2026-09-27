FROM oven/bun:1-alpine AS build

WORKDIR /app

COPY site/package.json site/bun.lock ./site/
RUN cd site && bun install --frozen-lockfile

COPY site ./site
COPY skills ./skills
COPY CHANGELOG.md ./CHANGELOG.md

RUN cd site && bun run build

FROM nginxinc/nginx-unprivileged:alpine@sha256:b54ac358b83fc6c965793fd271839b4ea4cdb6e99895bb19618cbc2ca152d972 AS runtime

COPY --chown=101:101 nginx.conf /etc/nginx/nginx.conf
COPY --from=build --chown=101:101 /app/site/dist/ /usr/share/nginx/html/

USER 101:101
EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD wget --spider --quiet http://127.0.0.1:8080/healthz
