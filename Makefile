DC = docker compose
EXEC = docker compose exec -it
LOGS = docker logs
ENV = --env-file docker-compose/.env
APP_FILE = docker-compose/app.yaml
STORAGES_FILE = docker-compose/storages.yaml
TEST_COMPOSE = tests/integrate/docker-compose-test.yaml
APP_CONTAINER = app

.PHONY: freeze
freeze:
	poetry export -o requirements.txt --without-hashes

.PHONY: lint
lint:
	ruff check video_api
	mypy video_api

.PHONY: lint
env:
	cp sample.env docker-compose/.env

.PHONY: app
app:
	${DC} -f ${APP_FILE} ${ENV} up --build -d

.PHONY: storages
storages:
	${DC} -f ${STORAGES_FILE} ${ENV} up --build -d

.PHONY: all
all:
	${MAKE} storages
	${MAKE} app

.PHONY: down-app
down-app:
	${DC} -f ${APP_FILE} down

.PHONY: down-storages
down-storages:
	${DC} -f ${STORAGES_FILE} down

.PHONY: down-all
down-all:
	${MAKE} down-storages
	${MAKE} down-app

.PHONY: tests
tests:
	pytest tests/unit
	${DC} -f ${TEST_COMPOSE} up --build --abort-on-container-exit --exit-code-from tests --attach tests

.PHONY: down-tests
down-tests:
	${DC} -f ${TEST_COMPOSE} down -v