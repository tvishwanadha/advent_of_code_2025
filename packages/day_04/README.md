# Day 04: Printing Department

## Part 1

The rolls of paper (`@`) are arranged on a large grid. The forklifts can only access a roll of paper if there are fewer than four rolls of paper in the eight adjacent positions.

### Example

```
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
```

There are 13 rolls of paper that can be accessed by a forklift:

```
..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.
```

### Solution Approach

For each roll of paper (`@`) in the grid, count the number of adjacent rolls in all 8 directions. If the count is less than 4, the roll is accessible.

## Part 2

Once a roll of paper can be accessed by a forklift, it can be removed. Once removed, the forklifts might be able to access more rolls, which they can also remove. Keep repeating this process until no more rolls are accessible.

### Example

Using the same grid, repeatedly remove accessible rolls until none remain accessible. The example shows 43 total rolls removed through multiple iterations (13 + 12 + 7 + 5 + 2 + 1 + 1 + 1 + 1 = 43).

### Solution Approach

Iteratively find and remove all accessible rolls (those with fewer than 4 adjacent rolls) until no more can be removed. Count the total removed.

## Notes

| Part | Zero-shot | Attempts | Errors | Hints | Observations |
|------|-----------|----------|--------|-------|--------------|
| 1    | Yes       | 1        | None   | None  | Straightforward grid neighbor counting |
| 2    | Yes       | 1        | None   | None  | Simple extension - iterate until fixed point |
