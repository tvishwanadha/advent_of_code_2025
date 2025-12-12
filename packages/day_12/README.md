# Day 12: Christmas Tree Farm

## Part 1

You need to determine how many regions under Christmas trees can fit all of their listed presents.

The input contains:
1. A list of present shapes (polyominoes) identified by index
2. A list of regions with dimensions and required presents

Presents can be rotated and flipped to fit. Shapes can't overlap but can fit together (the `.` parts don't block other presents).

### Example

```
0:
###
##.
##.

1:
###
##.
.##

...

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2
```

In this example, 2 regions can fit all their presents.

### Solution Approach

This is a 2D bin packing problem with polyominoes. The solution uses:
1. Area constraint check - reject regions where total cells needed > grid area
2. Backtracking with MRV (Minimum Remaining Values) heuristic
3. Precomputed placements for each shape orientation
4. Grid-based collision detection

## Part 2

Part 2 is a narrative conclusion with no additional puzzle. Completing Part 1 awards both stars for Day 12.

## Notes

| Part | Zero-shot | Attempts | Errors | Hints | Observations |
|------|-----------|----------|--------|-------|--------------|
| 1    | Yes       | 1        | None   | None  | Took ~11 min to run; 540/1000 regions fail area constraint immediately |
| 2    | N/A       | N/A      | N/A    | N/A   | Narrative conclusion only - no puzzle |
