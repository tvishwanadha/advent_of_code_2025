# Day 09: Movie Theater

## Part 1

You slide down the firepole in the corner of the playground and land in the North Pole base movie theater!

The movie theater has a big tile floor with an interesting pattern. Elves here are redecorating the theater by switching out some of the square tiles in the big grid they form. Some of the tiles are red; the Elves would like to find the largest rectangle that uses red tiles for two of its opposite corners. They even have a list of where the red tiles are located in the grid (your puzzle input).

For example:

```
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
```

Showing red tiles as `#` and other tiles as `.`, the above arrangement of red tiles would look like this:

```
..............
.......#...#..
..............
..#....#......
..............
..#......#....
..............
.........#.#..
..............
```

You can choose any two red tiles as the opposite corners of your rectangle; your goal is to find the largest rectangle possible.

For example, you could make a rectangle with an area of 24 between 2,5 and 9,7:

```
..............
.......#...#..
..............
..#....#......
..............
..OOOOOOOO....
..OOOOOOOO....
..OOOOOOOO.#..
..............
```

Or, you could make a rectangle with area 35 between 7,1 and 11,7:

```
..............
.......OOOOO..
.......OOOOO..
..#....OOOOO..
.......OOOOO..
..#....OOOOO..
.......OOOOO..
.......OOOOO..
..............
```

You could even make a thin rectangle with an area of only 6 between 7,3 and 2,3:

```
..............
.......#...#..
..............
..OOOOOO......
..............
..#......#....
..............
.........#.#..
..............
```

Ultimately, the largest rectangle you can make in this example has area 50. One way to do this is between 2,5 and 11,1:

```
..............
..OOOOOOOOOO..
..OOOOOOOOOO..
..OOOOOOOOOO..
..OOOOOOOOOO..
..OOOOOOOOOO..
..............
.........#.#..
..............
```

Using two red tiles as opposite corners, what is the largest area of any rectangle you can make?

### Example

Input: 8 red tiles at coordinates shown above
Output: 50

### Solution Approach

For each pair of red tiles, compute the area of the rectangle with those tiles as opposite corners. The area is `(|x2 - x1| + 1) * (|y2 - y1| + 1)` since both corner tiles are included. Return the maximum area found.

## Part 2

The Elves just remembered: they can only switch out tiles that are red or green. So, your rectangle can only include red or green tiles.

In your list, every red tile is connected to the red tile before and after it by a straight line of green tiles. The list wraps, so the first red tile is also connected to the last red tile. Tiles that are adjacent in your list will always be on either the same row or the same column.

The tiles on the edges between consecutive red tiles are green, and all tiles inside this loop of red and green tiles are also green. The remaining tiles are never red nor green.

The rectangle you choose still must have red tiles in opposite corners, but any other tiles it includes must now be red or green.

### Example

Using the same input, the largest rectangle using only red and green tiles has area 24 (between 9,5 and 2,3).

### Solution Approach

1. Build the polygon boundary from red tiles connected by green edges
2. Determine which tiles are inside the polygon (flood fill or ray casting)
3. For each pair of red tiles, check if the entire rectangle is within the red+green region
4. Return the maximum valid rectangle area

## Notes

| Part | Zero-shot | Attempts | Errors | Hints | Observations |
|------|-----------|----------|--------|-------|--------------|
| 1    | No        | 2        | Off-by-one: used `\|x2-x1\| * \|y2-y1\|` instead of `(\|x2-x1\|+1) * (\|y2-y1\|+1)` | None | Rectangle area must include both corner tiles |
| 2    | No        | 2        | Checking only 4 corners insufficient; polygon edges can cut through rectangle interior | None | Need to verify no polygon edge crosses through the rectangle |
