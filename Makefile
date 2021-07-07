install:
	pip install

migrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

superuser:
	python3 manage.py createsuperuser

collectstatic:
	python3 manage.py collectstatic

shell:
	python3 manage.py shell

set_env_vars:
	@[ -f .env ] && source .env

serve:
	python3 manage.py runserver

.PHONY: set_env_vars