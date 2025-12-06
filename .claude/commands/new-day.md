# Create a new Advent of Code day package

The user wants to create a new day package for day $ARGUMENTS.

## Steps

1. **Ask for puzzle text**: Use the AskUserQuestion tool to ask the user to paste the Part 1 puzzle description.

2. **Ask for puzzle input**: After receiving the puzzle text, ask the user to paste their puzzle input. Save it to `packages/day_$ARGUMENTS/src/day_$ARGUMENTS/input.txt`.

3. **Scaffold the package**: Run:
   ```bash
   uv init --package packages/day_$ARGUMENTS --no-readme
   ```

4. **Update pyproject.toml**: Update `packages/day_$ARGUMENTS/pyproject.toml` with the following changes:
   - Change `version = "0.1.0"` to `version = "2025.12"`
   - Change `description = "Add your description here"` to `description = "Advent of Code 2025 - Day $ARGUMENTS: <Title>"`
   - Keep the `name` as-is (uv init generates the correct hyphenated name like `day-05`)
   - Keep the `authors` block (already provided by uv init)
   - Change `requires-python = ">=3.14.0"` to `requires-python = ">=3.12"`
   - Keep the default scripts entry `day-$ARGUMENTS = "day_$ARGUMENTS:main"` (no changes needed)

5. **Sync to update uv.lock**: Run `uv sync` to ensure the version is recorded in the lock file.

6. **Replace __init__.py and create solution.py**:

   `packages/day_$ARGUMENTS/src/day_$ARGUMENTS/__init__.py`:
   ```python
   from pathlib import Path

   from day_$ARGUMENTS.solution import solve_part1, solve_part2


   def main() -> None:
       input_file = Path(__file__).parent / "input.txt"
       input_data = input_file.read_text()
       print(f"Part 1: {solve_part1(input_data)}")
       # print(f"Part 2: {solve_part2(input_data)}")


   if __name__ == "__main__":
       main()
   ```

   `packages/day_$ARGUMENTS/src/day_$ARGUMENTS/solution.py`:
   ```python
   def solve_part1(input_data: str) -> int:
       lines = input_data.strip().split("\n")

       # TODO: Implement solution
       return 0


   def solve_part2(input_data: str) -> int:
       # Part 2 not yet available
       msg = "Part 2 not yet implemented"
       raise NotImplementedError(msg)
   ```

7. **Create tests directory and test file**:

   `packages/day_$ARGUMENTS/tests/test_solution.py`:
   ```python
   import pytest

   from day_$ARGUMENTS.solution import solve_part1


   @pytest.fixture
   def example_input():
       return """TODO: Add example input"""


   def test_part1_example(example_input):
       assert solve_part1(example_input) == 0  # TODO: Add expected result
   ```

8. **Create README.md**: Create `packages/day_$ARGUMENTS/README.md` with the puzzle text:

   ```markdown
   # Day $ARGUMENTS: <Title>

   ## Part 1

   <puzzle text provided by user>

   ### Example

   <example from puzzle>

   ### Solution Approach

   <brief description>

   ## Part 2

   *Not yet available*

   ## Notes

   | Part | Zero-shot | Attempts | Errors | Hints | Observations |
   |------|-----------|----------|--------|-------|--------------|
   | 1    | ?         | ?        | ?      | ?     | ?            |
   | 2    | -         | -        | -      | -     | Not yet attempted |
   ```

9. **Update root pyproject.toml**: Add the new package to dependencies and sources:
   - Add `"day_$ARGUMENTS"` to `[project] dependencies`
   - Add `day_$ARGUMENTS = { workspace = true }` to `[tool.uv.sources]`

10. **Sync and verify**:
    ```bash
    uv sync
    make ci DAY=day_$ARGUMENTS
    ```

11. **Implement the solution**: Based on the puzzle description, implement `solve_part1()` in `solution.py` and update the test with the example from the puzzle.

12. **Run CI again** to verify the implementation passes all checks.

13. **Run solution and present answer**: Run the solution with `uv run day-$ARGUMENTS` and present the Part 1 answer to the user.

14. **Wait for user validation**: Ask the user to confirm whether the answer was correct on the Advent of Code server. Do NOT update the Notes table until the user confirms the result.

15. **Update Notes**: After the user confirms, update the Notes table in README.md with:
    - Zero-shot: Yes if solved on first attempt without hints, No otherwise
    - Attempts: Number of attempts needed
    - Errors: Types of errors encountered (parsing, logic, edge cases, etc.)
    - Hints: Any hints or guidance provided by the user
    - Observations: Interesting notes about the solution process
