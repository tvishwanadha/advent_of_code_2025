# Create a new Advent of Code day package

The user wants to create a new day package for day $ARGUMENTS.

## Steps

1. **Ask for puzzle text**: Use the AskUserQuestion tool to ask the user to paste the Part 1 puzzle description.

2. **Scaffold the package**: Run:
   ```bash
   uv init --package packages/day_$ARGUMENTS --no-readme
   ```

3. **Update pyproject.toml**: Update `packages/day_$ARGUMENTS/pyproject.toml` to set the version and add the scripts entry point:
   ```toml
   version = "2025.12"
   ```
   And add:
   ```toml
   [project.scripts]
   day_$ARGUMENTS = "day_$ARGUMENTS.solution:main"
   ```

4. **Sync to update uv.lock**: Run `uv sync` to ensure the version is recorded in the lock file.

5. **Create solution.py**: Replace the generated `__init__.py` content and create `solution.py`:

   `packages/day_$ARGUMENTS/src/day_$ARGUMENTS/__init__.py` should be empty.

   `packages/day_$ARGUMENTS/src/day_$ARGUMENTS/solution.py`:
   ```python
   from pathlib import Path


   def solve_part1(input_path: Path | str) -> int:
       with open(input_path) as f:
           lines = f.read().strip().split("\n")

       # TODO: Implement solution
       return 0


   def solve_part2(input_path: Path | str) -> int:
       # Part 2 not yet available
       msg = "Part 2 not yet implemented"
       raise NotImplementedError(msg)


   def main() -> None:
       input_file = Path(__file__).parent / "input.txt"
       print(f"Part 1: {solve_part1(input_file)}")
       # print(f"Part 2: {solve_part2(input_file)}")


   if __name__ == "__main__":
       main()
   ```

6. **Create tests directory and test file**:

   `packages/day_$ARGUMENTS/tests/test_solution.py`:
   ```python
   import tempfile
   from pathlib import Path

   from day_$ARGUMENTS.solution import solve_part1


   def test_part1_example():
       example_input = """TODO: Add example input"""
       with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
           f.write(example_input)
           f.flush()
           result = solve_part1(Path(f.name))

       assert result == 0  # TODO: Add expected result
   ```

7. **Create README.md**: Create `packages/day_$ARGUMENTS/README.md` with the puzzle text:

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

8. **Update root pyproject.toml**: Add the new package to dependencies and sources:
   - Add `"day_$ARGUMENTS"` to `[project] dependencies`
   - Add `day_$ARGUMENTS = { workspace = true }` to `[tool.uv.sources]`

9. **Sync and verify**:
   ```bash
   uv sync
   make ci DAY=day_$ARGUMENTS
   ```

10. **Implement the solution**: Based on the puzzle description, implement `solve_part1()` in `solution.py` and update the test with the example from the puzzle.

11. **Run CI again** to verify the implementation passes all checks.

12. **Update Notes**: After implementation, update the Notes table in README.md with:
    - Zero-shot: Yes if solved on first attempt without hints, No otherwise
    - Attempts: Number of attempts needed
    - Errors: Types of errors encountered (parsing, logic, edge cases, etc.)
    - Hints: Any hints or guidance provided by the user
    - Observations: Interesting notes about the solution process
