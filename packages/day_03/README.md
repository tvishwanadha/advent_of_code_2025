# Day 03: Lobby

## Part 1

You descend a short staircase, enter the surprisingly vast lobby, and are quickly cleared by the security checkpoint. When you get to the main elevators, however, you discover that each one has a red light above it: they're all offline.

"Sorry about that," an Elf apologizes as she tinkers with a nearby control panel. "Some kind of electrical surge seems to have fried them. I'll try to get them online soon."

You explain your need to get further underground. "Well, you could at least take the escalator down to the printing department, not that you'd get much further than that without the elevators working. That is, you could if the escalator weren't also offline."

"But, don't worry! It's not fried; it just needs power. Maybe you can get it running while I keep working on the elevators."

There are batteries nearby that can supply emergency power to the escalator for just such an occasion. The batteries are each labeled with their joltage rating, a value from 1 to 9. You make a note of their joltage ratings (your puzzle input).

The batteries are arranged into banks; each line of digits in your input corresponds to a single bank of batteries. Within each bank, you need to turn on exactly two batteries; the joltage that the bank produces is equal to the number formed by the digits on the batteries you've turned on. For example, if you have a bank like 12345 and you turn on batteries 2 and 4, the bank would produce 24 jolts. (You cannot rearrange batteries.)

You'll need to find the largest possible joltage each bank can produce.

### Example

```
987654321111111
811111111111119
234234234234278
818181911112111
```

- In `987654321111111`, you can make the largest joltage possible, 98, by turning on the first two batteries.
- In `811111111111119`, you can make the largest joltage possible by turning on the batteries labeled 8 and 9, producing 89 jolts.
- In `234234234234278`, you can make 78 by turning on the last two batteries (marked 7 and 8).
- In `818181911112111`, the largest joltage you can produce is 92.

The total output joltage is the sum of the maximum joltage from each bank: 98 + 89 + 78 + 92 = **357**

### Solution Approach

For each bank, find the two batteries that form the largest two-digit number when selected in order (first digit * 10 + second digit).

## Part 2

Now you need to turn on exactly **twelve** batteries within each bank instead of two. The joltage output is still the number formed by the digits of the batteries turned on, but now there will be 12 digits.

### Example

Using the same input:
- `987654321111111` → `987654321111` (turn on everything except some 1s at the end)
- `811111111111119` → `811111111119` (turn on everything except some 1s)
- `234234234234278` → `434234234278` (skip a 2, 3, and another 2 near the start)
- `818181911112111` → `888911112111` (turn on everything except some 1s near the front)

Total: 987654321111 + 811111111119 + 434234234278 + 888911112111 = **3121910778619**

### Solution Approach

Use dynamic programming or greedy selection to find the 12 digits that form the largest number when selected in order.

## Notes

| Part | Zero-shot | Attempts | Errors | Hints | Observations |
|------|-----------|----------|--------|-------|--------------|
| 1    | Yes       | 1        | None   | None  | Initially O(n²) brute-force; refactored to use O(n) greedy for consistency with Part 2 |
| 2    | Yes       | 1        | None   | None  | Greedy selection - pick largest digit that leaves enough remaining |
