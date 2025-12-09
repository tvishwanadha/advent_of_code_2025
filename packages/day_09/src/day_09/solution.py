def solve_part1(input_data: str) -> int:
    lines = input_data.strip().split("\n")

    # Parse coordinates
    tiles = []
    for line in lines:
        x, y = map(int, line.split(","))
        tiles.append((x, y))

    # Find largest rectangle area using any two tiles as opposite corners
    max_area = 0
    n = len(tiles)
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = tiles[i]
            x2, y2 = tiles[j]
            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            max_area = max(max_area, area)

    return max_area


def solve_part2(input_data: str) -> int:
    lines = input_data.strip().split("\n")

    # Parse coordinates (red tiles form polygon vertices in order)
    red_tiles = []
    for line in lines:
        x, y = map(int, line.split(","))
        red_tiles.append((x, y))

    n = len(red_tiles)

    # Build polygon edges - each consecutive pair of red tiles is connected
    # The polygon wraps around (last connects to first)
    polygon = red_tiles  # vertices in order

    def point_in_polygon(px: int, py: int) -> bool:
        """Check if point (px, py) is inside or on the polygon using ray casting."""
        # First check if point is on an edge
        for i in range(n):
            x1, y1 = polygon[i]
            x2, y2 = polygon[(i + 1) % n]

            # Check if point is on this edge (edges are horizontal or vertical)
            if x1 == x2 == px and min(y1, y2) <= py <= max(y1, y2):
                return True
            if y1 == y2 == py and min(x1, x2) <= px <= max(x1, x2):
                return True

        # Ray casting for interior points
        # Cast ray from (px, py) to the right and count intersections
        inside = False
        for i in range(n):
            x1, y1 = polygon[i]
            x2, y2 = polygon[(i + 1) % n]

            # Only consider edges that could intersect a horizontal ray to the right
            if y1 == y2:
                # Horizontal edge - doesn't cross our horizontal ray
                continue

            # Vertical edge from (x1, y1) to (x2, y2) where x1 == x2
            # Check if ray at height py intersects this edge to the right of point
            # Use standard crossing rule: count if py is strictly between y1 and y2
            if x1 > px and (y1 > py) != (y2 > py):
                inside = not inside

        return inside

    def rectangle_in_polygon(x1: int, y1: int, x2: int, y2: int) -> bool:
        """Check if entire rectangle is inside or on the polygon."""
        min_x, max_x = min(x1, x2), max(x1, x2)
        min_y, max_y = min(y1, y2), max(y1, y2)

        # Check all 4 corners
        corners = [
            (min_x, min_y),
            (min_x, max_y),
            (max_x, min_y),
            (max_x, max_y),
        ]

        if not all(point_in_polygon(cx, cy) for cx, cy in corners):
            return False

        # Check that no polygon edge passes through the interior of the rectangle
        # An edge passes through interior if it's strictly inside the rectangle bounds
        for i in range(n):
            ex1, ey1 = polygon[i]
            ex2, ey2 = polygon[(i + 1) % n]

            if ex1 == ex2:  # Vertical edge
                edge_x = ex1
                edge_min_y, edge_max_y = min(ey1, ey2), max(ey1, ey2)
                # Edge passes through interior if x is strictly inside and y ranges overlap
                if min_x < edge_x < max_x and edge_min_y < max_y and edge_max_y > min_y:
                    return False
            else:  # Horizontal edge (ey1 == ey2)
                edge_y = ey1
                edge_min_x, edge_max_x = min(ex1, ex2), max(ex1, ex2)
                # Edge passes through interior if y is strictly inside and x ranges overlap
                if min_y < edge_y < max_y and edge_min_x < max_x and edge_max_x > min_x:
                    return False

        return True

    # Find largest rectangle with red tiles as opposite corners
    # where all tiles in rectangle are red or green
    max_area = 0

    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = red_tiles[i]
            x2, y2 = red_tiles[j]

            # Both corners are red tiles (on boundary), check if rectangle is valid
            if rectangle_in_polygon(x1, y1, x2, y2):
                area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
                max_area = max(max_area, area)

    return max_area
