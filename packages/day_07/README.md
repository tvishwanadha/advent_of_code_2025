# Day 07: Laboratories

## Part 1

You thank the cephalopods for the help and exit the trash compactor, finding yourself in the familiar halls of a North Pole research wing.

Based on the large sign that says "teleporter hub", they seem to be researching teleportation; you can't help but try it for yourself and step onto the large yellow teleporter pad.

Suddenly, you find yourself in an unfamiliar room! The room has no doors; the only way out is the teleporter. Unfortunately, the teleporter seems to be leaking magic smoke.

Since this is a teleporter lab, there are lots of spare parts, manuals, and diagnostic equipment lying around. After connecting one of the diagnostic tools, it helpfully displays error code 0H-N0, which apparently means that there's an issue with one of the tachyon manifolds.

You quickly locate a diagram of the tachyon manifold (your puzzle input). A tachyon beam enters the manifold at the location marked S; tachyon beams always move downward. Tachyon beams pass freely through empty space (.). However, if a tachyon beam encounters a splitter (^), the beam is stopped; instead, a new tachyon beam continues from the immediate left and from the immediate right of the splitter.

### Example

```
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
```

In this example, the incoming tachyon beam extends downward from S until it reaches the first splitter. At that point, the original beam stops, and two new beams are emitted from the splitter. Those beams continue downward until they reach more splitters.

When two beams merge into the same location (between adjacent splitters), they combine into a single beam. The process continues until all tachyon beams reach a splitter or exit the manifold.

In this example, a tachyon beam is split a total of **21** times.

### Solution Approach

Simulate tachyon beams moving downward through the grid. Track beam positions at each row. When a beam hits a splitter (^), count it as a split and spawn two new beams (left and right). Handle beam merging when multiple beams occupy the same column.

## Part 2

With a quantum tachyon manifold, only a single tachyon particle is sent through the manifold. A tachyon particle takes both the left and right path of each splitter encountered.

Since this is impossible, the manual recommends the many-worlds interpretation of quantum tachyon splitting: each time a particle reaches a splitter, it's actually time itself which splits. In one timeline, the particle went left, and in the other timeline, the particle went right.

To fix the manifold, what you really need to know is the number of timelines active after a single particle completes all of its possible journeys through the manifold.

### Example

In the example, there are many timelines - including the one where the particle always went left, the one where it alternated, etc. In total, the particle ends up on **40** different timelines.

### Solution Approach

Instead of tracking just positions, track (position, timeline_count) pairs. When a particle at position with N timelines hits a splitter, it creates N timelines going left and N timelines going right. When particles at the same position merge, their timeline counts add up.

## Notes

| Part | Zero-shot | Attempts | Errors | Hints | Observations |
|------|-----------|----------|--------|-------|--------------|
| 1    | Yes       | 1        | None   | None  | Straightforward beam simulation with set-based merging |
| 2    | Yes       | 1        | None   | None  | Changed from set to dict to track timeline counts per position |
