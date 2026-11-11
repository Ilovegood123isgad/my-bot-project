# Convenience targets for this repository.
#
# Run `make` (or `make help`) to list the available targets.

.DEFAULT_GOAL := help

PYTHON ?= python3

# Test modules are named test_*.py (see docs/conventions.md). Skip hidden
# directories such as .git and caches so only repository tests are run.
TEST_FILES := $(shell find . -path '*/.*' -prune -o -name '__pycache__' -prune -o -type f -name 'test_*.py' -print | sort)

.PHONY: help test

help:
	@echo "Available targets:"
	@echo "  make test   Run every unittest test file (test_*.py)"
	@echo "  make help   Show this message"

test:
	@status=0; \
	for file in $(TEST_FILES); do \
		echo "Running $$file"; \
		PYTHONPATH=. $(PYTHON) "$$file" || status=1; \
	done; \
	exit $$status
