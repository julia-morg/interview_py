.PHONY: help up down shell test-ai-client sql-cats sql-messages

COMPOSE = docker compose
SERVICE = interview
VENV = /app/.venv
PIP = $(VENV)/bin/pip
PYTHON = $(VENV)/bin/python
EXEC = $(COMPOSE) exec $(SERVICE)

.DEFAULT_GOAL := help

help:
	@grep -E '^(Makefile:)?[a-zA-Z_-]+:.*?# .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":[^:]*?# "}; {sub(/^Makefile:/, "", $$1); if (length($$1) > 30) {printf "\033[36m%s\033[0m\n%31s%s\n", $$1, "", $$2} else {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}}'

up: # Start container and install dependencies
	$(COMPOSE) up -d
	$(EXEC) sh -c 'test -x $(PIP) || (python -m venv $(VENV) && $(PYTHON) -m pip install -q --upgrade pip)'
	$(EXEC) $(PIP) install -q -r requirements.txt

down: # Stop container
	$(COMPOSE) down

shell: # Open sh in container
	$(EXEC) env PATH="$(VENV)/bin:$$PATH" sh

sql-cats: # Run sql/cats.sql (task 2)
	$(EXEC) $(PYTHON) sql/run_query.py sql/cats.sql

sql-messages: # Run sql/messages.sql (task 3)
	$(EXEC) $(PYTHON) sql/run_query.py sql/messages.sql

test-ai-client: # Run interviewer checks for task 4
	$(EXEC) $(PYTHON) -m pytest tests/test_ai_client.py -vv
