# Makefile for Annemoia

PYTHON := python3
PIP     := $(PYTHON) -m pip

.PHONY: help ann deps full

help:
	@echo "Usage:"
	@echo "  make ann    # install only the 'ann' CLI (editable)"
	@echo "  make deps   # install Bandit & Brakeman"

ann:
	@echo "Installing Annemoia CLI in editable mode…"
	$(PIP) install --upgrade pip setuptools wheel
	$(PIP) install -e .

deps:
	@echo "Installing security tool dependencies…"
	$(PIP) install bandit
	@gem install brakeman
	@gem install erb
