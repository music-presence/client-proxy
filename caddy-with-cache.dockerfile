FROM caddy:builder AS builder

RUN xcaddy build \
    --with github.com/caddyserver/cache-handler \
    --with github.com/darkweak/storages/redis/caddy

FROM caddy:latest

COPY --from=builder /usr/bin/caddy /usr/bin/caddy
