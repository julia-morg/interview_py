.PHONY: help up down shell chess test test-rotation test-pawn test-ai-client sql-cats sql-phones sql-messages

COMPOSE = docker compose
SERVICE = interview
VENV = /app/.venv
PIP = $(VENV)/bin/pip
PYTHON = $(VENV)/bin/python
PYTEST = $(VENV)/bin/pytest
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

chess: # Run chess, e.g. make chess MOVES="e2-e4 e7-e5"
	$(EXEC) $(PYTHON) chess.py $(MOVES)

test: # Run all tests
	$(EXEC) $(PYTEST)

test-rotation: # Run rotation tests (task 1)
	$(EXEC) $(PYTEST) -m rotation

test-pawn: # Run pawn tests (task 2)
	$(EXEC) $(PYTEST) -m pawn

test-ai-client: # Run interviewer checks for task 7
	$(EXEC) $(PYTHON) -m pytest hints/test_ai_client.py -q

sql-cats: # Run sql/cats.sql (task 3)
	$(EXEC) $(PYTHON) sql/run_query.py sql/cats.sql

sql-phones: # Run sql/phones.sql (task 4)
	$(EXEC) $(PYTHON) sql/run_query.py sql/phones.sql

sql-messages: # Run sql/messages.sql (task 5)
	$(EXEC) $(PYTHON) sql/run_query.py sql/messages.sql
