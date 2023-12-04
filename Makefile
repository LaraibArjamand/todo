.PHONY: install
install:
	poetry install

.PHONY: migrate
migrate:
	poetry run python -m todoapp.manage migrate

.PHONY: makemigrations
makemigrations:
	poetry run python -m todoapp.manage makemigrations

.PHONY: runserver
runserver:
	poetry run python -m todoapp.manage runserver

.PHONY: superuser
superuser:
	poetry run python -m todoapp.manage createsuperuser

.PHONY: migrations
migrations: migrate makemigrations;
