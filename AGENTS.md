# Agent Instructions

This repository is an **AI experiment** testing Claude Opus 4.5 on Advent of Code 2025. The goal is to attempt zero-shot solutions and track results.

## Project Structure

- `packages/day_XX/` - Each day is a separate package
- `pyproject.toml` - Root workspace config with dev dependencies (ruff, pytest, pyright)
- `Makefile` - Build commands

### Package Structure

Each day package follows this structure:

```
packages/day_XX/
├── pyproject.toml
├── README.md           # Puzzle description (Part 1 & Part 2 sections)
├── src/
│   └── day_XX/
│       ├── __init__.py
│       ├── solution.py # Main solution (solve_part1, solve_part2)
│       └── input.txt   # Puzzle input (same for both parts)
└── tests/
    └── test_solution.py
```

## Slash Commands

### `/new-day XX` - Create a new day package

1. Prompts for Part 1 puzzle text
2. Runs `uv init --package packages/day_XX` to scaffold
3. Creates `tests/` directory and test file
4. Creates `solution.py` with part1/part2 template
5. Creates `README.md` with Part 1 description
6. Updates root `pyproject.toml` to include the new package
7. Runs `uv sync` and `make ci` to verify
8. Implements the Part 1 solution

### `/part2 XX` - Add Part 2 to an existing day

1. Prompts for Part 2 puzzle text
2. Updates README.md with Part 2 section
3. Implements `solve_part2()` in solution.py
4. Adds Part 2 test
5. Runs `make ci` to verify

## Solution Template

The `solution.py` file should follow this pattern:

```python
from pathlib import Path


def solve_part1(input_path: Path | str) -> int:
    # Parse input and solve Part 1
    ...
    return result


def solve_part2(input_path: Path | str) -> int:
    # Parse input and solve Part 2
    ...
    return result


if __name__ == "__main__":
    input_file = Path(__file__).parent / "input.txt"
    print(f"Part 1: {solve_part1(input_file)}")
    print(f"Part 2: {solve_part2(input_file)}")
```

## Testing

Tests should use the examples from the puzzle:

```python
from day_XX.solution import solve_part1, solve_part2


def test_part1_example():
    # Create temp file with example input
    # Assert solve_part1() returns expected result


def test_part2_example():
    # Create temp file with example input
    # Assert solve_part2() returns expected result
```

## CI Commands

Always run CI after making changes:

```bash
make ci DAY=day_XX      # Single day
make ci-all             # All days
```

## Code Style

- Line length: 100 characters
- Ruff rules: E, F, I, UP (errors, pyflakes, isort, pyupgrade)
- Type hints required (pyright standard mode)

## Experiment Tracking

Each day's README includes a **Notes** table to track AI performance:

| Part | Zero-shot | Attempts | Errors | Hints | Observations |
|------|-----------|----------|--------|-------|--------------|
| 1    | Yes/No    | N        | ...    | ...   | ...          |
| 2    | Yes/No    | N        | ...    | ...   | ...          |

**After solving each part, update the Notes table with:**
- **Zero-shot**: Yes if solved on first attempt without hints, No otherwise
- **Attempts**: Number of attempts needed to get correct answer
- **Errors**: Types of errors encountered (parsing, logic, edge cases, off-by-one, etc.)
- **Hints**: Any hints or guidance provided by the user
- **Observations**: Interesting notes (e.g., "tricky edge case", "needed to re-read problem")
