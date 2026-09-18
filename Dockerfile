FROM node:24-alpine@sha256:ebfe2f90462722a7a4de65e91990e97fe0d401c70e0e762c5b53302f905ec1c1 AS build

WORKDIR /app

COPY docs/package.json docs/package-lock.json ./docs/
RUN npm ci --prefix docs

COPY docs ./docs
COPY skills ./skills
COPY CHANGELOG.md ./CHANGELOG.md

RUN npm run build --prefix docs

FROM nginxinc/nginx-unprivileged:alpine@sha256:b54ac358b83fc6c965793fd271839b4ea4cdb6e99895bb19618cbc2ca152d972 AS runtime

COPY --chown=101:101 nginx.conf /etc/nginx/nginx.conf
COPY --from=build --chown=101:101 /app/docs/dist/ /usr/share/nginx/html/

USER 101:101
EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD wget --spider --quiet http://127.0.0.1:8080/healthz
