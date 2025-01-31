.PHONY: all update

all:

update:
	git submodule update --remote loon_git
	docker compose build --no-cache loon
