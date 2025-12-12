from collections import defaultdict
from functools import cache


def solve_part1(input_data: str) -> int:
    lines = input_data.strip().split("\n")

    # Build adjacency list (graph)
    graph: dict[str, list[str]] = defaultdict(list)
    for line in lines:
        parts = line.split(": ")
        source = parts[0]
        if len(parts) > 1:
            destinations = parts[1].split()
            graph[source].extend(destinations)

    # Count all paths from "you" to "out" using memoized DFS
    @cache
    def count_paths(node: str) -> int:
        if node == "out":
            return 1
        if node not in graph:
            return 0
        return sum(count_paths(neighbor) for neighbor in graph[node])

    return count_paths("you")


def solve_part2(input_data: str) -> int:
    lines = input_data.strip().split("\n")

    # Build adjacency list (graph)
    graph: dict[str, list[str]] = defaultdict(list)
    for line in lines:
        parts = line.split(": ")
        source = parts[0]
        if len(parts) > 1:
            destinations = parts[1].split()
            graph[source].extend(destinations)

    # Count paths from "svr" to "out" that visit both "dac" and "fft"
    # State: (current_node, visited_dac, visited_fft)
    @cache
    def count_paths(node: str, has_dac: bool, has_fft: bool) -> int:
        # Update state based on current node
        if node == "dac":
            has_dac = True
        if node == "fft":
            has_fft = True

        if node == "out":
            # Only count if we visited both required nodes
            return 1 if (has_dac and has_fft) else 0
        if node not in graph:
            return 0
        return sum(count_paths(neighbor, has_dac, has_fft) for neighbor in graph[node])

    return count_paths("svr", False, False)
