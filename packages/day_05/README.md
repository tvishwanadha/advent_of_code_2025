# Day 05: Cafeteria

## Part 1

The Elves in the kitchen are trying to determine which of the available ingredient IDs are fresh.

The database operates on ingredient IDs. It consists of a list of fresh ingredient ID ranges, a blank line, and a list of available ingredient IDs.

The fresh ID ranges are inclusive: the range 3-5 means that ingredient IDs 3, 4, and 5 are all fresh. The ranges can also overlap; an ingredient ID is fresh if it is in any range.

### Example

```
3-5
10-14
16-20
12-18

1
5
8
11
17
32
```

- Ingredient ID 1 is spoiled because it does not fall into any range.
- Ingredient ID 5 is fresh because it falls into range 3-5.
- Ingredient ID 8 is spoiled.
- Ingredient ID 11 is fresh because it falls into range 10-14.
- Ingredient ID 17 is fresh because it falls into range 16-20 as well as range 12-18.
- Ingredient ID 32 is spoiled.

So, in this example, 3 of the available ingredient IDs are fresh.

### Solution Approach

Parse the ranges and ingredient IDs, then for each ingredient, check if it falls within any of the fresh ranges.

## Part 2

The Elves would like to know all of the IDs that the fresh ingredient ID ranges consider to be fresh. The second section of the database (the available ingredient IDs) is now irrelevant.

### Example

Using the same ranges from Part 1:
```
3-5
10-14
16-20
12-18
```

The ingredient IDs that these ranges consider to be fresh are 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, and 20. So, the fresh ingredient ID ranges consider a total of **14** ingredient IDs to be fresh.

### Solution Approach

Merge overlapping ranges, then sum the count of IDs in each merged range.

## Notes

| Part | Zero-shot | Attempts | Errors | Hints | Observations |
|------|-----------|----------|--------|-------|--------------|
| 1    | Yes       | 1        | None   | None  | Straightforward range membership check |
| 2    | Yes       | 1        | None   | None  | Classic interval merging problem |
