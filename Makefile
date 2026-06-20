# Run `make help` to see the available shortcuts.
PYTHON := python3
VENV := .venv
VENV_PYTHON := $(VENV)/bin/python

.PHONY: help venv install setup run clean

help:
	@echo "make setup    Create the virtual environment and install dependencies"
	@echo "make run      Set up the project and start the board"
	@echo "make clean    Remove the virtual environment and Python cache files"

$(VENV_PYTHON):
	$(PYTHON) -m venv $(VENV)

venv: $(VENV_PYTHON)

install: venv requirements.txt
	$(VENV_PYTHON) -m pip install -r requirements.txt

setup: install

run: setup
	$(VENV_PYTHON) src/main.py

clean:
	rm -rf $(VENV) src/__pycache__
