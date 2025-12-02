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

4. **Enable Part 2 output**: In `packages/day_$ARGUMENTS/src/day_$ARGUMENTS/solution.py`, uncomment the Part 2 print line in `main()`:
   ```python
   print(f"Part 2: {solve_part2(input_file)}")
   ```

5. **Add Part 2 test**: Add `test_part2_example()` to `packages/day_$ARGUMENTS/tests/test_solution.py`:

   ```python
   from day_$ARGUMENTS.solution import solve_part1, solve_part2


   def test_part2_example():
       example_input = """<example input>"""
       with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
           f.write(example_input)
           f.flush()
           result = solve_part2(Path(f.name))

       assert result == <expected>
   ```

6. **Run CI** to verify:
   ```bash
   make ci DAY=day_$ARGUMENTS
   ```
