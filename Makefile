SHELL := /usr/bin/env bash
PY := python3
VENV := .venv
BIN := $(VENV)/bin
PIP := $(BIN)/pip
UVICORN := $(BIN)/uvicorn

.DEFAULT_GOAL := help
.PHONY: help install env dev run

help:
	@echo "Targets:"
	@echo "  make install   - Create venv and install deps"
	@echo "  make env       - Copy backend/.env.example to backend/.env if missing"
	@echo "  make dev       - Run API with reload on :8000"
	@echo "  make run       - Run API without reload"

$(VENV):
	$(PY) -m venv $(VENV)

install: $(VENV)
	$(PIP) install -U pip
	$(PIP) install -r backend/requirements.txt

env:
	@test -f backend/.env || cp backend/.env.example backend/.env

dev: install env
	$(UVICORN) backend.main:app --reload --host 0.0.0.0 --port 8000

run: install env
	$(UVICORN) backend.main:app --host 0.0.0.0 --port 8000
