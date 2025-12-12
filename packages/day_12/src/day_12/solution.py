type Shape = frozenset[tuple[int, int]]


def parse_input(
    input_data: str,
) -> tuple[list[Shape], list[tuple[int, int, list[int]]]]:
    """Parse input into shapes and regions."""
    lines = input_data.strip().split("\n")

    # Parse shapes first, then regions
    shapes: list[Shape] = []
    regions: list[tuple[int, int, list[int]]] = []
    shape_lines: list[str] = []
    parsing_shapes = True

    for line in lines:
        if not line.strip():
            # Empty line - finalize current shape if any
            if shape_lines:
                shapes.append(parse_shape(shape_lines))
                shape_lines = []
            continue

        # Check if this is a region line (WxH: counts)
        if "x" in line and ":" in line:
            before_colon = line.split(":")[0]
            if "x" in before_colon and all(
                c.isdigit() or c == "x" for c in before_colon
            ):
                parsing_shapes = False

        if parsing_shapes:
            # Check if this is a shape header (digit:)
            if ":" in line:
                before_colon = line.split(":")[0].strip()
                if before_colon.isdigit():
                    # Finalize previous shape if any
                    if shape_lines:
                        shapes.append(parse_shape(shape_lines))
                        shape_lines = []
                    continue  # Skip the header line
            shape_lines.append(line)
        else:
            # Region line
            dims, counts_str = line.split(":")
            width, height = map(int, dims.split("x"))
            counts = list(map(int, counts_str.strip().split()))
            regions.append((width, height, counts))

    # Finalize last shape if any
    if shape_lines:
        shapes.append(parse_shape(shape_lines))

    return shapes, regions


def parse_shape(lines: list[str]) -> Shape:
    """Parse shape lines into a set of (row, col) coordinates."""
    cells: set[tuple[int, int]] = set()
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char == "#":
                cells.add((row, col))
    return normalize_shape(cells)


def normalize_shape(cells: set[tuple[int, int]]) -> Shape:
    """Normalize shape so min row and col are 0."""
    if not cells:
        return frozenset()
    min_row = min(r for r, _ in cells)
    min_col = min(c for _, c in cells)
    return frozenset((r - min_row, c - min_col) for r, c in cells)


def get_all_orientations(shape: Shape) -> list[Shape]:
    """Get all unique orientations (rotations and flips) of a shape."""
    orientations: set[Shape] = set()

    def rotate_90(cells: Shape) -> Shape:
        """Rotate 90 degrees clockwise: (r, c) -> (c, -r)"""
        return normalize_shape({(c, -r) for r, c in cells})

    def flip_horizontal(cells: Shape) -> Shape:
        """Flip horizontally: (r, c) -> (r, -c)"""
        return normalize_shape({(r, -c) for r, c in cells})

    current = shape
    for _ in range(4):
        orientations.add(current)
        orientations.add(flip_horizontal(current))
        current = rotate_90(current)

    return list(orientations)


def can_place(
    grid: list[list[bool]],
    shape: Shape,
    start_row: int,
    start_col: int,
    height: int,
    width: int,
) -> bool:
    """Check if shape can be placed at (start_row, start_col)."""
    for dr, dc in shape:
        r, c = start_row + dr, start_col + dc
        if r < 0 or r >= height or c < 0 or c >= width:
            return False
        if grid[r][c]:
            return False
    return True


def place_shape(
    grid: list[list[bool]], shape: Shape, start_row: int, start_col: int, value: bool
) -> None:
    """Place or remove a shape on the grid."""
    for dr, dc in shape:
        grid[start_row + dr][start_col + dc] = value


def solve_region(
    width: int, height: int, shapes: list[Shape], counts: list[int]
) -> bool:
    """Try to fit all presents into the region using backtracking with MRV heuristic."""
    # Check area constraint first
    total_cells = sum(len(shapes[idx]) * counts[idx] for idx in range(len(counts)))
    if total_cells > width * height:
        return False

    # Build list of unique shape indices we need to place (with counts)
    shape_counts: dict[int, int] = {}
    for shape_idx, count in enumerate(counts):
        if count > 0:
            shape_counts[shape_idx] = count

    if not shape_counts:
        return True

    # Precompute all valid placements for each shape type
    shape_orientations: dict[int, list[Shape]] = {}
    for shape_idx in shape_counts:
        shape_orientations[shape_idx] = get_all_orientations(shapes[shape_idx])

    # Precompute all placements (with bounds check only)
    all_placements: dict[int, list[tuple[tuple[int, int], ...]]] = {}
    for shape_idx in shape_counts:
        placements: list[tuple[tuple[int, int], ...]] = []
        for orientation in shape_orientations[shape_idx]:
            for r in range(height):
                for c in range(width):
                    cells: list[tuple[int, int]] = []
                    valid = True
                    for dr, dc in orientation:
                        nr, nc = r + dr, c + dc
                        if nr < 0 or nr >= height or nc < 0 or nc >= width:
                            valid = False
                            break
                        cells.append((nr, nc))
                    if valid:
                        placements.append(tuple(cells))
        all_placements[shape_idx] = placements

    # Use a grid representation for faster collision checking
    grid = [[False] * width for _ in range(height)]

    def can_place(cells: tuple[tuple[int, int], ...]) -> bool:
        return all(not grid[r][c] for r, c in cells)

    def place(cells: tuple[tuple[int, int], ...]) -> None:
        for r, c in cells:
            grid[r][c] = True

    def unplace(cells: tuple[tuple[int, int], ...]) -> None:
        for r, c in cells:
            grid[r][c] = False

    def get_valid_count(
        shape_idx: int,
    ) -> tuple[int, list[tuple[tuple[int, int], ...]]]:
        """Get count and list of valid placements for a shape."""
        valid = [cells for cells in all_placements[shape_idx] if can_place(cells)]
        return len(valid), valid

    def backtrack(remaining: dict[int, int]) -> bool:
        if not remaining:
            return True

        # Find shape with fewest valid placements (MRV heuristic)
        best_shape = -1
        best_count = float("inf")
        best_placements: list[tuple[tuple[int, int], ...]] = []

        for shape_idx, count in remaining.items():
            if count == 0:
                continue
            valid_count, valid_placements = get_valid_count(shape_idx)
            if valid_count == 0:
                return False  # No valid placement - prune
            if valid_count < best_count:
                best_count = valid_count
                best_shape = shape_idx
                best_placements = valid_placements

        if best_shape == -1:
            return True

        # Try each placement
        for cells in best_placements:
            place(cells)
            remaining[best_shape] -= 1
            if remaining[best_shape] == 0:
                del remaining[best_shape]

            if backtrack(remaining):
                return True

            if best_shape not in remaining:
                remaining[best_shape] = 0
            remaining[best_shape] += 1
            unplace(cells)

        return False

    return backtrack(dict(shape_counts))


def solve_part1(input_data: str, verbose: bool = False) -> int:
    shapes, regions = parse_input(input_data)

    count = 0
    for i, (width, height, counts) in enumerate(regions):
        result = solve_region(width, height, shapes, counts)
        if verbose:
            print(f"Region {i + 1}/{len(regions)}: {width}x{height} -> {result}")
        if result:
            count += 1

    return count


def solve_part2(input_data: str) -> int:
    # Part 2 not yet available
    msg = "Part 2 not yet implemented"
    raise NotImplementedError(msg)
