def solve_part1(input_data: str) -> int:
    lines = input_data.strip().split("\n")

    grid = [list(line) for line in lines]
    rows = len(grid)
    cols = len(grid[0])

    # 8 directions: N, NE, E, SE, S, SW, W, NW
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    accessible_count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "@":
                # Count adjacent rolls of paper
                adjacent_rolls = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "@":
                        adjacent_rolls += 1

                # Accessible if fewer than 4 adjacent rolls
                if adjacent_rolls < 4:
                    accessible_count += 1

    return accessible_count


def solve_part2(input_data: str) -> int:
    lines = input_data.strip().split("\n")

    grid = [list(line) for line in lines]
    rows = len(grid)
    cols = len(grid[0])

    # 8 directions: N, NE, E, SE, S, SW, W, NW
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    def find_accessible() -> list[tuple[int, int]]:
        """Find all rolls that can be accessed (fewer than 4 adjacent rolls)."""
        accessible = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "@":
                    adjacent_rolls = 0
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "@":
                            adjacent_rolls += 1
                    if adjacent_rolls < 4:
                        accessible.append((r, c))
        return accessible

    total_removed = 0

    while True:
        accessible = find_accessible()
        if not accessible:
            break
        # Remove all accessible rolls
        for r, c in accessible:
            grid[r][c] = "."
        total_removed += len(accessible)

    return total_removed
