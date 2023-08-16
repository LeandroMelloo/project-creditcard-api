.PHONY: install
install:
	pip install --upgrade pip
	pip install -r requirements.txt

.PHONY: freeze
freeze:
	pip freeze > requirements.txt

.PHONY: migrations
migrations:
	python manage.py makemigrations

.PHONY: migrate
migrate:
	python manage.py migrate

.PHONY: runserver
runserver:
	python manage.py runserver

.PHONY: superuser
superuser:
	python manage.py createsuperuser

.PHONY: update
update: install migrate

.PHONY: build
build: 
	docker build .
	docker-compose build

.PHONY: run
run: 
	docker-compose up -d


