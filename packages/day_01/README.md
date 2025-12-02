# Day 1: Safe Combination

## Part 1

You arrive at the secret entrance to the North Pole base ready to start decorating. Unfortunately, the password seems to have been changed, so you can't get in. A document taped to the wall helpfully explains:

"Due to new security protocols, the password is locked in the safe below. Please see the attached document for the new combination."

The safe has a dial with only an arrow on it; around the dial are the numbers 0 through 99 in order. As you turn the dial, it makes a small click noise as it reaches each number.

The attached document (your puzzle input) contains a sequence of rotations, one per line, which tell you how to open the safe. A rotation starts with an L or R which indicates whether the rotation should be to the left (toward lower numbers) or to the right (toward higher numbers). Then, the rotation has a distance value which indicates how many clicks the dial should be rotated in that direction.

So, if the dial were pointing at 11, a rotation of R8 would cause the dial to point at 19. After that, a rotation of L19 would cause it to point at 0.

Because the dial is a circle, turning the dial left from 0 one click makes it point at 99. Similarly, turning the dial right from 99 one click makes it point at 0.

So, if the dial were pointing at 5, a rotation of L10 would cause it to point at 95. After that, a rotation of R5 could cause it to point at 0.

The dial starts by pointing at 50.

You could follow the instructions, but your recent required official North Pole secret entrance security training seminar taught you that the safe is actually a decoy. The actual password is the number of times the dial is left pointing at 0 after any rotation in the sequence.

### Example

```
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
```

Following these rotations:
- Start at 50
- L68 → 82
- L30 → 52
- R48 → 0 (count: 1)
- L5 → 95
- R60 → 55
- L55 → 0 (count: 2)
- L1 → 99
- L99 → 0 (count: 3)
- R14 → 14
- L82 → 32

**Answer: 3**

### Solution Approach

1. Start at position 50
2. For each rotation, apply modulo 100 arithmetic:
   - L (left): `position = (position - distance) % 100`
   - R (right): `position = (position + distance) % 100`
3. Count how many times position equals 0 after a rotation

## Part 2

You're sure that's the right password, but the door won't open. You knock, but nobody answers. You build a snowman while you think.

As you're rolling the snowballs for your snowman, you find another security document that must have fallen into the snow:

"Due to newer security protocols, please use password method 0x434C49434B until further notice."

You remember from the training seminar that "method 0x434C49434B" means you're actually supposed to count the number of times any click causes the dial to point at 0, regardless of whether it happens during a rotation or at the end of one.

### Example

Using the same example rotations from Part 1:

- The dial starts by pointing at 50.
- L68 → 82; during this rotation, it points at 0 once.
- L30 → 52
- R48 → 0
- L5 → 95
- R60 → 55; during this rotation, it points at 0 once.
- L55 → 0
- L1 → 99
- L99 → 0
- R14 → 14
- L82 → 32; during this rotation, it points at 0 once.

The dial points at 0 three times at the end of a rotation, plus three more times during a rotation.

**Answer: 6**

Note: if the dial were pointing at 50, a single rotation like R1000 would cause the dial to point at 0 ten times before returning back to 50!

### Solution Approach

1. Start at position 50
2. For each rotation, count how many times we pass through or land on 0
3. Track each click individually, or calculate mathematically based on start/end positions and distance

## Notes

| Part | Zero-shot | Attempts | Errors | Hints | Observations |
|------|-----------|----------|--------|-------|--------------|
| 1    | Yes       | 1        | None   | None  | Straightforward modular arithmetic problem |
| 2    | Yes       | 1        | None   | None  | Extended Part 1 logic to count zero crossings during rotations |
