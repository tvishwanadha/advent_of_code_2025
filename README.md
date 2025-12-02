# Advent of Code 2025

Solutions for [Advent of Code 2025](https://adventofcode.com/2025) in Python.

## AI Experiment

This repository is an experiment to test how well AI handles Advent of Code 2025 puzzles. The goal is to:

1. **Zero-shot attempts**: For each day, attempt to solve both parts without hints or guidance
2. **Track results**: Document success/failure, number of attempts, error types, and observations
3. **Model**: Claude Opus 4.5 via [Claude Code](https://claude.ai/claude-code)

Each day's README includes a **Notes** section tracking:
- Whether zero-shot succeeded
- Number of attempts needed
- Types of errors encountered
- Any hints or guidance provided
- Interesting observations about the solution process

## Project Structure

```
aoc2025/
├── packages/
│   ├── day_01/
│   ├── day_02/
│   └── ...
├── pyproject.toml    # Workspace configuration
└── Makefile          # Build commands
```

Each day is a separate package with:
- `src/day_XX/solution.py` - Solution code
- `src/day_XX/input.txt` - Puzzle input
- `tests/test_solution.py` - Tests
- `README.md` - Puzzle description

## Usage

### Run a solution

```bash
make run              # Run day_01 (default)
make run DAY=day_05   # Run day_05
```

### Run tests

```bash
make test             # Test day_01
make test DAY=day_05  # Test day_05
make test-all         # Test all days
```

### Run full CI (format, lint, typecheck, test)

```bash
make ci               # CI for day_01
make ci DAY=day_05    # CI for day_05
make ci-all           # CI for all days
```

### Individual commands

```bash
make format           # Format code
make lint             # Run linter
make typecheck        # Run type checker
```

## Adding a New Day

Use the `/new-day` slash command in Claude Code:

```
/new-day 02
```

This will scaffold a new day package and prompt for the puzzle text.
