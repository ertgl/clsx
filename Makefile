.DEFAULT_GOAL := all


PROJECT_DIR := $(CURDIR)

HACK_DIR := $(PROJECT_DIR)/hack
HACK_SCRIPTS_DIR := $(HACK_DIR)/scripts

VENV_DIR ?= $(PROJECT_DIR)/.venv


GLOBAL_PYTHON ?= $(shell which python)
LOCAL_PYTHON := $(VENV_DIR)/bin/python
PYTHON ?= $(shell test -x $(LOCAL_PYTHON) && echo $(LOCAL_PYTHON) || echo $(GLOBAL_PYTHON))

GLOBAL_MYPY ?= $(shell which mypy)
LOCAL_MYPY := $(VENV_DIR)/bin/mypy
MYPY ?= $(shell test -x $(LOCAL_MYPY) && echo $(LOCAL_MYPY) || echo $(GLOBAL_MYPY))

GLOBAL_RUFF ?= $(shell which ruff)
LOCAL_RUFF := $(VENV_DIR)/bin/ruff
RUFF ?= $(shell test -x $(LOCAL_RUFF) && echo $(LOCAL_RUFF) || echo $(GLOBAL_RUFF))


.PHONY: lint
lint:
	$(RUFF) check .
	$(MYPY) .


.PHONY: lint.fix
lint.fix:
	$(RUFF) check . --fix
	$(PYTHON) $(HACK_SCRIPTS_DIR)/format_exported_py_symbols.py


.PHONY: format
format: lint.fix


.PHONY: test
test:
	$(PYTHON) -m unittest discover \
		-s $(PROJECT_DIR)/src/ \
		-p "*_test.py"


.PHONY: all
all: test
