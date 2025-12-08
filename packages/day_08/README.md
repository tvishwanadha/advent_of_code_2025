# Day 08: Playground

## Part 1

Equipped with a new understanding of teleporter maintenance, you confidently step onto the repaired teleporter pad.

You rematerialize on an unfamiliar teleporter pad and find yourself in a vast underground space which contains a giant playground!

Across the playground, a group of Elves are working on setting up an ambitious Christmas decoration project. Through careful rigging, they have suspended a large number of small electrical junction boxes.

Their plan is to connect the junction boxes with long strings of lights. Most of the junction boxes don't provide electricity; however, when two junction boxes are connected by a string of lights, electricity can pass between those two junction boxes.

The Elves are trying to figure out which junction boxes to connect so that electricity can reach every junction box. They even have a list of all of the junction boxes' positions in 3D space (your puzzle input).

To save on string lights, the Elves would like to focus on connecting pairs of junction boxes that are as close together as possible according to straight-line distance.

The process is:
1. Find the two junction boxes which are closest together
2. Connect them (they become part of the same circuit)
3. Find the next two closest junction boxes that aren't already directly connected
4. If they're already in the same circuit, nothing happens
5. Continue this process

After making the specified number of connections, multiply together the sizes of the three largest circuits.

### Example

After making the ten shortest connections with 20 junction boxes, there are 11 circuits: one circuit which contains 5 junction boxes, one circuit which contains 4 junction boxes, two circuits which contain 2 junction boxes each, and seven circuits which each contain a single junction box. Multiplying together the sizes of the three largest circuits (5, 4, and one of the circuits of size 2) produces 40.

### Solution Approach

1. Parse the 3D coordinates of all junction boxes
2. Compute all pairwise distances and sort them
3. Use Union-Find (Disjoint Set Union) to track circuits as connections are made
4. Process the 1000 shortest connections
5. Find the three largest circuit sizes and multiply them

## Part 2

The Elves were right; they definitely don't have enough extension cables. You'll need to keep connecting junction boxes together until they're all in one large circuit.

Continue connecting the closest unconnected pairs of junction boxes together until they're all in the same circuit. What do you get if you multiply together the X coordinates of the last two junction boxes you need to connect?

### Example

The first connection which causes all of the junction boxes to form a single circuit is between the junction boxes at 216,146,977 and 117,168,530. Multiplying the X coordinates of those two junction boxes (216 and 117) produces 25272.

### Solution Approach

1. Continue from Part 1's Union-Find approach
2. Process connections in order of distance until all nodes are in one circuit
3. Track the last connection that actually merged two different circuits
4. Return the product of the X coordinates of those two junction boxes

## Notes

| Part | Zero-shot | Attempts | Errors | Hints | Observations |
|------|-----------|----------|--------|-------|--------------|
| 1    | Yes       | 1        | None   | None  | Classic Union-Find problem with 3D Euclidean distances |
| 2    | Yes       | 1        | None   | None  | Natural extension - find last edge in MST (Kruskal's algorithm) |
