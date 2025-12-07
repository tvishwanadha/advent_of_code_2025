# Add Part 2 to an existing day

The user wants to add Part 2 for day $ARGUMENTS.

## Steps

1. **Ask for puzzle text**: Use the AskUserQuestion tool to ask the user to paste the Part 2 puzzle description.

2. **Update README.md**: Replace the `## Part 2` section in `packages/day_$ARGUMENTS/README.md`:

   ```markdown
   ## Part 2

   <puzzle text provided by user>

   ### Example

   <example from puzzle, if different from Part 1>

   ### Solution Approach

   <brief description>
   ```

3. **Implement solve_part2**: Update `packages/day_$ARGUMENTS/src/day_$ARGUMENTS/solution.py` to implement `solve_part2()`.

4. **Enable Part 2 output**: In `packages/day_$ARGUMENTS/src/day_$ARGUMENTS/__init__.py`:
   - Add `solve_part2` to the import: `from day_$ARGUMENTS.solution import solve_part1, solve_part2`
   - Uncomment the Part 2 print line: `print(f"Part 2: {solve_part2(input_data)}")`

5. **Add Part 2 test**: In `packages/day_$ARGUMENTS/tests/test_solution.py`:
   - Add `solve_part2` to the import: `from day_$ARGUMENTS.solution import solve_part1, solve_part2`
   - Add the test function:
   ```python
   def test_part2_example(example_input):
       assert solve_part2(example_input) == <expected>
   ```

6. **Run CI** to verify:
   ```bash
   make ci DAY=day_$ARGUMENTS
   ```

7. **Run solution and present answer**: Run the solution with `uv run day-$ARGUMENTS` and present the Part 2 answer to the user.

8. **Wait for user validation**: Ask the user to confirm whether the answer was correct on the Advent of Code server. Do NOT update the Notes table until the user confirms the result.

9. **Update Notes**: After the user confirms, update the Part 2 row in the Notes table in README.md with:
   - Zero-shot: Yes if solved on first attempt without hints, No otherwise
   - Attempts: Number of attempts needed
   - Errors: Types of errors encountered (parsing, logic, edge cases, etc.)
   - Hints: Any hints or guidance provided by the user
   - Observations: Interesting notes about the solution process
