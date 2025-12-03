from pathlib import Path


def max_joltage_bruteforce(bank: str) -> int:
    """Find the maximum two-digit joltage from a bank of batteries (O(n²) brute-force)."""
    best = 0
    n = len(bank)
    for i in range(n):
        for j in range(i + 1, n):
            joltage = int(bank[i]) * 10 + int(bank[j])
            best = max(best, joltage)
    return best


def solve_part1(input_path: Path | str) -> int:
    with open(input_path) as f:
        lines = f.read().strip().split("\n")

    return sum(max_joltage_k(bank, 2) for bank in lines)


def max_joltage_k(bank: str, k: int) -> int:
    """Find the maximum k-digit joltage from a bank of batteries using greedy selection."""
    n = len(bank)
    result = []
    start = 0

    for i in range(k):
        # Need to pick (k - i) more digits, so we can search up to index n - (k - i)
        remaining_to_pick = k - i
        end = n - remaining_to_pick + 1

        # Find the maximum digit in the valid range
        best_digit = -1
        best_idx = start
        for j in range(start, end):
            digit = int(bank[j])
            if digit > best_digit:
                best_digit = digit
                best_idx = j

        result.append(best_digit)
        start = best_idx + 1

    # Convert digit list to number
    return int("".join(str(d) for d in result))


def solve_part2(input_path: Path | str) -> int:
    with open(input_path) as f:
        lines = f.read().strip().split("\n")

    return sum(max_joltage_k(bank, 12) for bank in lines)


def main() -> None:
    input_file = Path(__file__).parent / "input.txt"
    print(f"Part 1: {solve_part1(input_file)}")
    print(f"Part 2: {solve_part2(input_file)}")


if __name__ == "__main__":
    main()
