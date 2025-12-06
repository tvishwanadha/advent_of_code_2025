def solve_part1(input_data: str) -> int:
    content = input_data.strip()

    # Split into ranges section and ingredients section
    sections = content.split("\n\n")
    ranges_section = sections[0]
    ingredients_section = sections[1]

    # Parse fresh ID ranges
    fresh_ranges: list[tuple[int, int]] = []
    for line in ranges_section.split("\n"):
        start, end = line.split("-")
        fresh_ranges.append((int(start), int(end)))

    # Parse available ingredient IDs
    ingredient_ids = [int(line) for line in ingredients_section.split("\n")]

    # Count fresh ingredients
    fresh_count = 0
    for ingredient_id in ingredient_ids:
        for start, end in fresh_ranges:
            if start <= ingredient_id <= end:
                fresh_count += 1
                break

    return fresh_count


def solve_part2(input_data: str) -> int:
    content = input_data.strip()

    # Split into ranges section (ignore ingredients section for Part 2)
    sections = content.split("\n\n")
    ranges_section = sections[0]

    # Parse fresh ID ranges
    fresh_ranges: list[tuple[int, int]] = []
    for line in ranges_section.split("\n"):
        start, end = line.split("-")
        fresh_ranges.append((int(start), int(end)))

    # Sort ranges by start position
    fresh_ranges.sort()

    # Merge overlapping ranges
    merged: list[tuple[int, int]] = []
    for start, end in fresh_ranges:
        if merged and start <= merged[-1][1] + 1:
            # Overlapping or adjacent - extend the previous range
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            # New non-overlapping range
            merged.append((start, end))

    # Count total fresh IDs
    total = 0
    for start, end in merged:
        total += end - start + 1

    return total
