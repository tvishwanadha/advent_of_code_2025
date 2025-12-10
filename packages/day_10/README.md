# Day 10: Factory

## Part 1

Just across the hall, you find a large factory. Fortunately, the Elves here have plenty of time to decorate. Unfortunately, it's because the factory machines are all offline, and none of the Elves can figure out the initialization procedure.

The Elves do have the manual for the machines, but the section detailing the initialization procedure was eaten by a Shiba Inu. All that remains of the manual are some indicator light diagrams, button wiring schematics, and joltage requirements for each machine.

The manual describes one machine per line. Each line contains a single indicator light diagram in [square brackets], one or more button wiring schematics in (parentheses), and joltage requirements in {curly braces}.

To start a machine, its indicator lights must match those shown in the diagram, where `.` means off and `#` means on. The machine has the number of indicator lights shown, but its indicator lights are all initially off.

You can toggle the state of indicator lights by pushing any of the listed buttons. Each button lists which indicator lights it toggles, where 0 means the first light, 1 means the second light, and so on. When you push a button, each listed indicator light either turns on (if it was off) or turns off (if it was on). You have to push each button an integer number of times.

Because none of the machines are running, the joltage requirements are irrelevant and can be safely ignored.

You can push each button as many times as you like. However, to save on time, you will need to determine the fewest total presses required to correctly configure all indicator lights for all machines in your list.

### Example

```
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
```

- First machine: fewest presses is 2 (e.g., press (0,2) and (0,1) once each)
- Second machine: fewest presses is 3 (e.g., press (0,4), (0,1,2), and (1,2,3,4) once each)
- Third machine: fewest presses is 2 (e.g., press (0,3,4) and (0,1,2,4,5) once each)

Total: 2 + 3 + 2 = **7**

### Solution Approach

This is a linear algebra problem over GF(2) (the field with two elements, 0 and 1). Each button press toggles certain lights, and toggling twice cancels out. We need to find the minimum number of button presses to reach the target state.

Since pressing a button twice has no effect (toggles cancel), we only care about whether each button is pressed an odd or even number of times (0 or 1 presses in GF(2)). We model this as a system of linear equations over GF(2) and find the solution with minimum Hamming weight.

## Part 2

Now use the joltage requirements instead of indicator lights. Each machine has counters (initially 0) that need to reach specific values. Buttons now add 1 to their listed counters (instead of toggling). Find the minimum total button presses to configure all machines' joltage counters.

### Example

Same input as Part 1:
- First machine: minimum 10 presses to reach {3,5,4,7}
- Second machine: minimum 12 presses to reach {7,5,12,7,2}
- Third machine: minimum 11 presses to reach {10,11,11,5,10,5}

Total: 10 + 12 + 11 = **33**

### Solution Approach

This is an integer linear programming problem. We need to find non-negative integers for button press counts such that the sum of contributions equals the target joltage values, minimizing total presses. This can be solved using linear programming relaxation or direct ILP solvers.

## Notes

| Part | Zero-shot | Attempts | Errors | Hints | Observations |
|------|-----------|----------|--------|-------|--------------|
| 1    | Yes       | 1        | None   | None  | Classic GF(2) linear algebra problem; brute force for small cases |
| 2    | No        | 4        | Type errors, bounds calculation bugs | None  | ILP with Gaussian elimination; tricky bounds pruning for free variable search |
