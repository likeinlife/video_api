.PHONY: freeze
freeze:
	poetry export -o requirements.txt --without-hashes

.PHONY: lint
lint:
	ruff check video_api
	mypy video_api

.PHONY: app
app:
	cd video_api;
