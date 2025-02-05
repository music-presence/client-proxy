.PHONY: all update

all:

reload-proxy:
	docker compose exec -w /etc/caddy -it loon-proxy caddy reload

reload-clients:
	docker compose exec -w /etc/caddy -it loon-clients caddy reload

update:
	git submodule update --remote vendor/loon
	docker compose build --no-cache loon
