.PHONY: all update

all:

update:
	git submodule update --remote vendor/loon
	docker compose build --no-cache loon
