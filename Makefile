.PHONY: install
install:
	poetry install

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall; poetry run pre-commit install

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

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

.PHONY: update
update: install migrate install-pre-commit ;
