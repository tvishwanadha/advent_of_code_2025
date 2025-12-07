def solve_part1(input_data: str) -> int:
    lines = input_data.strip().split("\n")

    # Find starting position S
    start_col = -1
    start_row = 0
    for row_idx, line in enumerate(lines):
        if "S" in line:
            start_col = line.index("S")
            start_row = row_idx
            break

    # Track active beam positions (column indices) as a set
    # Beams at the same column merge into one
    beam_positions: set[int] = {start_col}

    split_count = 0
    width = len(lines[0])

    # Simulate beams moving downward from the starting row
    for row_idx in range(start_row + 1, len(lines)):
        line = lines[row_idx]
        new_positions: set[int] = set()

        for col in beam_positions:
            if col < 0 or col >= width:
                # Beam exits the manifold
                continue

            char = line[col]
            if char == "^":
                # Beam hits a splitter - count the split and spawn two beams
                split_count += 1
                # New beams go left and right
                new_positions.add(col - 1)
                new_positions.add(col + 1)
            else:
                # Beam continues downward through empty space
                new_positions.add(col)

        beam_positions = new_positions

        if not beam_positions:
            break

    return split_count


def solve_part2(input_data: str) -> int:
    lines = input_data.strip().split("\n")

    # Find starting position S
    start_col = -1
    start_row = 0
    for row_idx, line in enumerate(lines):
        if "S" in line:
            start_col = line.index("S")
            start_row = row_idx
            break

    # Track (column -> timeline_count) as a dict
    # When particles at the same position merge, their timeline counts add
    beam_timelines: dict[int, int] = {start_col: 1}

    width = len(lines[0])

    # Simulate particle moving downward from the starting row
    for row_idx in range(start_row + 1, len(lines)):
        line = lines[row_idx]
        new_timelines: dict[int, int] = {}

        for col, count in beam_timelines.items():
            if col < 0 or col >= width:
                # Particle exits the manifold - timelines still count
                new_timelines[col] = new_timelines.get(col, 0) + count
                continue

            char = line[col]
            if char == "^":
                # Particle hits a splitter - splits into left and right
                # Each timeline branches into two
                left_col = col - 1
                right_col = col + 1
                new_timelines[left_col] = new_timelines.get(left_col, 0) + count
                new_timelines[right_col] = new_timelines.get(right_col, 0) + count
            else:
                # Particle continues downward
                new_timelines[col] = new_timelines.get(col, 0) + count

        beam_timelines = new_timelines

        if not beam_timelines:
            break

    # Total number of timelines is sum of all timeline counts
    return sum(beam_timelines.values())
