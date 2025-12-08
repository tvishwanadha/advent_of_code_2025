from collections import Counter


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True


def solve_part1(input_data: str, num_connections: int = 1000) -> int:
    lines = input_data.strip().split("\n")

    # Parse coordinates
    points = []
    for line in lines:
        x, y, z = map(int, line.split(","))
        points.append((x, y, z))

    n = len(points)

    # Calculate all pairwise distances (squared to avoid sqrt)
    distances = []
    for i in range(n):
        for j in range(i + 1, n):
            dx = points[i][0] - points[j][0]
            dy = points[i][1] - points[j][1]
            dz = points[i][2] - points[j][2]
            dist_sq = dx * dx + dy * dy + dz * dz
            distances.append((dist_sq, i, j))

    # Sort by distance
    distances.sort()

    # Use Union-Find to track circuits
    uf = UnionFind(n)

    # Process the shortest connections
    for _dist_sq, i, j in distances[:num_connections]:
        uf.union(i, j)

    # Count circuit sizes
    roots = [uf.find(i) for i in range(n)]
    sizes = Counter(roots)

    # Get three largest circuit sizes
    largest = sorted(sizes.values(), reverse=True)[:3]

    # Multiply together
    result = 1
    for size in largest:
        result *= size

    return result


def solve_part2(input_data: str) -> int:
    lines = input_data.strip().split("\n")

    # Parse coordinates
    points = []
    for line in lines:
        x, y, z = map(int, line.split(","))
        points.append((x, y, z))

    n = len(points)

    # Calculate all pairwise distances (squared to avoid sqrt)
    distances = []
    for i in range(n):
        for j in range(i + 1, n):
            dx = points[i][0] - points[j][0]
            dy = points[i][1] - points[j][1]
            dz = points[i][2] - points[j][2]
            dist_sq = dx * dx + dy * dy + dz * dz
            distances.append((dist_sq, i, j))

    # Sort by distance
    distances.sort()

    # Use Union-Find to track circuits
    uf = UnionFind(n)

    # Track the number of distinct components
    num_components = n
    last_i, last_j = -1, -1

    # Process connections until all in one circuit
    for _dist_sq, i, j in distances:
        if uf.union(i, j):
            num_components -= 1
            last_i, last_j = i, j
            if num_components == 1:
                break

    # Return product of X coordinates of the last two connected junction boxes
    return points[last_i][0] * points[last_j][0]
