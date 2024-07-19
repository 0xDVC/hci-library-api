DOCKER_COMPOSE = docker-compose
ALEMBIC = alembic
PYTHON = python3

up:
	$(DOCKER_COMPOSE) up --build

down:
	$(DOCKER_COMPOSE) down
restart:
	$(DOCKER_COMPOSE) down && $(DOCKER_COMPOSE) up --build
migrate:
	$(ALEMBIC) upgrade head
makemigrations:
	$(ALEMBIC) revision --autogenerate -m "New migration"
install:
	$(PYTHON) -m venv venv && source venv/bin/activate && pip install -r requirements.txt
clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete