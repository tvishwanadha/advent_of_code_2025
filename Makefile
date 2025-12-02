# Usage: make <target> [DAY=day_01]  - for single day
#        make <target>-all           - for entire workspace
DAY ?= day_01

.PHONY: lint format typecheck test run ci
.PHONY: lint-all format-all typecheck-all test-all ci-all

# Single day targets
lint:
	uv run ruff check packages/$(DAY)

format:
	uv run ruff format packages/$(DAY)

typecheck:
	uv run pyright packages/$(DAY)

test:
	uv run pytest packages/$(DAY)

run:
	uv run python -m $(DAY)

ci: format lint typecheck test

# Workspace-wide targets
lint-all:
	uv run ruff check packages/

format-all:
	uv run ruff format packages/

typecheck-all:
	uv run pyright packages/

test-all:
	uv run pytest packages/

ci-all: format-all lint-all typecheck-all test-all
