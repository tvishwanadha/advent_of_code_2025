# Day 06: Trash Compactor

## Part 1

After helping the Elves in the kitchen, you were taking a break and helping them re-enact a movie scene when you over-enthusiastically jumped into the garbage chute!

A brief fall later, you find yourself in a garbage smasher. Unfortunately, the door's been magnetically sealed.

As you try to find a way out, you are approached by a family of cephalopods! They're pretty sure they can get the door open, but it will take some time. While you wait, they're curious if you can help the youngest cephalopod with her math homework.

Cephalopod math doesn't look that different from normal math. The math worksheet (your puzzle input) consists of a list of problems; each problem has a group of numbers that need to be either added (+) or multiplied (*) together.

However, the problems are arranged a little strangely; they seem to be presented next to each other in a very long horizontal list.

### Example

```
123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +
```

Each problem's numbers are arranged vertically; at the bottom of the problem is the symbol for the operation that needs to be performed. Problems are separated by a full column of only spaces.

So, this worksheet contains four problems:

- 123 * 45 * 6 = 33210
- 328 + 64 + 98 = 490
- 51 * 387 * 215 = 4243455
- 64 + 23 + 314 = 401

Grand total: 33210 + 490 + 4243455 + 401 = 4277556

### Solution Approach

Parse the input as a grid, identify problem columns by finding operations in the last row, extract numbers from each column, apply the operation, and sum all results.

## Part 2

Cephalopod math is written right-to-left in columns. Each number is given in its own column, with the most significant digit at the top and the least significant digit at the bottom. (Problems are still separated with a column consisting only of spaces, and the symbol at the bottom of the problem is still the operator to use.)

### Example

```
123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +
```

Reading the problems right-to-left one column at a time:

- The rightmost problem is 4 + 431 + 623 = 1058
- The second problem from the right is 175 * 581 * 32 = 3253600
- The third problem from the right is 8 + 248 + 369 = 625
- Finally, the leftmost problem is 356 * 24 * 1 = 8544

Grand total: 1058 + 3253600 + 625 + 8544 = 3263827

### Solution Approach

Parse the grid into problems (same as Part 1), but for each problem read digits column-by-column from right to left (top-to-bottom within each column) to form numbers, then apply the operation.

## Notes

| Part | Zero-shot | Attempts | Errors | Hints | Observations |
|------|-----------|----------|--------|-------|--------------|
| 1    | No        | 1        | Parsing logic error | None | Initial implementation incorrectly treated single spaces as separators instead of requiring "full column of only spaces". Test caught the bug before submitting. |
| 2    | Yes       | 1        | None | None | Clean implementation - read columns right-to-left, digits top-to-bottom to form numbers. |
