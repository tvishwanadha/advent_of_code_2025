from pathlib import Path


def is_invalid_id(n: int) -> bool:
    """Check if n is made of some sequence of digits repeated twice."""
    s = str(n)
    length = len(s)
    # Must have even number of digits
    if length % 2 != 0:
        return False
    half = length // 2
    return s[:half] == s[half:]


def solve_part1(input_path: Path | str) -> int:
    with open(input_path) as f:
        line = f.read().strip()

    total = 0
    ranges = line.split(",")
    for r in ranges:
        r = r.strip()
        if not r:
            continue
        start_str, end_str = r.split("-")
        start, end = int(start_str), int(end_str)
        for n in range(start, end + 1):
            if is_invalid_id(n):
                total += n
    return total


def is_invalid_id_v2(n: int) -> bool:
    """Check if n is made of some sequence of digits repeated at least twice."""
    s = str(n)
    length = len(s)
    # Try all possible pattern lengths from 1 to length//2
    for pattern_len in range(1, length // 2 + 1):
        if length % pattern_len == 0:
            pattern = s[:pattern_len]
            repetitions = length // pattern_len
            if repetitions >= 2 and pattern * repetitions == s:
                return True
    return False


def solve_part2(input_path: Path | str) -> int:
    with open(input_path) as f:
        line = f.read().strip()

    total = 0
    ranges = line.split(",")
    for r in ranges:
        r = r.strip()
        if not r:
            continue
        start_str, end_str = r.split("-")
        start, end = int(start_str), int(end_str)
        for n in range(start, end + 1):
            if is_invalid_id_v2(n):
                total += n
    return total


def main() -> None:
    input_file = Path(__file__).parent / "input.txt"
    print(f"Part 1: {solve_part1(input_file)}")
    print(f"Part 2: {solve_part2(input_file)}")


if __name__ == "__main__":
    main()
