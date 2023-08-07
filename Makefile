SHELL := /bin/bash
CWD := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
ME := $(shell whoami)

nothing:
	@echo "do nothing"

up:
	docker-compose up --remove-orphans --build \
		poseidon__balancer \
		poseidon__broker__amqp \
		poseidon__api \
		poseidon__email_worker \
		poseidon__web \

check_env:
	@./srv/check_env.sh

cleanup:
	docker login gitlab.neroelectronics.by:5050 -u unic_lab_developers -p Vw3o4gBzgH_GGUzFs7NM

	@# git submodule foreach "git fetch && git merge origin/dev"
	git submodule init
	git submodule update --remote
	pipenv sync --dev

	ulpytool install

lint:
	pipenv run lint

tests:
	pipenv run test

drop:
	docker-compose down -v

fix_own:
	@echo "me: $(ME)"
	sudo chown $(ME):$(ME) -R .

######################## MANAGER POSEIDON DB START ########################

poseidon__db__dump:
	docker-compose run --rm manager__poseidon__db uldbutls dump '--db-uri=$$POSEIDON__DB_URI'

poseidon__db__migrate:
	docker-compose run --rm manager__poseidon__db uldbutls migrate --app-dir="./src/poseidon__db"

poseidon__db__revision:
	docker-compose run --rm manager__poseidon__db uldbutls revision --app-dir="./src/poseidon__db"

poseidon__db__init:
	docker-compose run --rm manager__poseidon__db uldbutls init --app-dir="./src/poseidon__db"

poseidon__db__upgrade:
	docker-compose run --rm manager__poseidon__db uldbutls upgrade --app-dir="./src/poseidon__db"

poseidon__db__downgrade:
	docker-compose run --rm manager__poseidon__db uldbutls downgrade --app-dir="./src/poseidon__db"

######################## MANAGER POSEIDON DB END ##########################
