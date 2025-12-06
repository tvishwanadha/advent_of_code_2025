def solve_part1(input_data: str) -> int:
    lines = input_data.split("\n")

    # Remove empty trailing lines but keep the structure
    while lines and lines[-1] == "":
        lines.pop()

    # The last line contains the operations (* or +)
    # Numbers are arranged in columns above the operations
    # Problems are separated by a full column of only spaces

    if not lines:
        return 0

    # Find the width of the grid
    max_width = max(len(line) for line in lines)

    # Pad all lines to the same width
    lines = [line.ljust(max_width) for line in lines]

    # Find columns that are entirely spaces (separator columns)
    separator_cols: set[int] = set()
    for col in range(max_width):
        if all(line[col] == " " for line in lines):
            separator_cols.add(col)

    # Group consecutive non-separator columns into problems
    problems: list[tuple[list[int], str]] = []
    col = 0

    while col < max_width:
        # Skip separator columns
        while col < max_width and col in separator_cols:
            col += 1

        if col >= max_width:
            break

        # Found start of a problem - find the extent
        start_col = col

        while col < max_width and col not in separator_cols:
            col += 1
        end_col = col

        # Extract the operation from the last row
        ops_segment = lines[-1][start_col:end_col].strip()
        if not ops_segment:
            continue
        op = ops_segment[0]  # Should be * or +

        # Extract numbers from number rows
        numbers: list[int] = []
        for row in lines[:-1]:
            segment = row[start_col:end_col].strip()
            if segment:
                numbers.append(int(segment))

        if numbers:
            problems.append((numbers, op))

    # Solve each problem and sum the results
    total = 0
    for numbers, op in problems:
        if op == "+":
            result = sum(numbers)
        else:  # op == "*"
            result = 1
            for n in numbers:
                result *= n
        total += result

    return total


def solve_part2(input_data: str) -> int:
    lines = input_data.split("\n")

    # Remove empty trailing lines but keep the structure
    while lines and lines[-1] == "":
        lines.pop()

    if not lines:
        return 0

    # Find the width of the grid
    max_width = max(len(line) for line in lines)

    # Pad all lines to the same width
    lines = [line.ljust(max_width) for line in lines]

    # Find columns that are entirely spaces (separator columns)
    separator_cols: set[int] = set()
    for col in range(max_width):
        if all(line[col] == " " for line in lines):
            separator_cols.add(col)

    # Group consecutive non-separator columns into problems
    # For Part 2, we need to read columns right-to-left within each problem
    # Each column forms a number (digits top-to-bottom = most significant to least)
    problems: list[tuple[list[int], str]] = []
    col = 0

    while col < max_width:
        # Skip separator columns
        while col < max_width and col in separator_cols:
            col += 1

        if col >= max_width:
            break

        # Found start of a problem - find the extent
        start_col = col

        while col < max_width and col not in separator_cols:
            col += 1
        end_col = col

        # Extract the operation from the last row
        ops_segment = lines[-1][start_col:end_col].strip()
        if not ops_segment:
            continue
        op = ops_segment[0]  # Should be * or +

        # For Part 2: read columns right-to-left
        # Each column forms one number (digits read top-to-bottom)
        numbers: list[int] = []
        number_rows = lines[:-1]

        # Iterate columns from right to left within this problem
        for c in range(end_col - 1, start_col - 1, -1):
            # Build number from digits in this column (top to bottom)
            digit_str = ""
            for row in number_rows:
                char = row[c]
                if char.isdigit():
                    digit_str += char
            if digit_str:
                numbers.append(int(digit_str))

        if numbers:
            problems.append((numbers, op))

    # Solve each problem and sum the results
    total = 0
    for numbers, op in problems:
        if op == "+":
            result = sum(numbers)
        else:  # op == "*"
            result = 1
            for n in numbers:
                result *= n
        total += result

    return total
