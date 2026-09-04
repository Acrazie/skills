FROM php:8.3-cli-alpine
WORKDIR /app
COPY composer.json composer.lock ./
COPY . .
CMD ["php", "bin/console", "about"]
