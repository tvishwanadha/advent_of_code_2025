from pathlib import Path


def solve_part1(input_path: Path | str) -> int:
    position = 50
    zero_count = 0

    with open(input_path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            direction = line[0]
            distance = int(line[1:])

            if direction == "L":
                position = (position - distance) % 100
            else:  # R
                position = (position + distance) % 100

            if position == 0:
                zero_count += 1

    return zero_count


def solve_part2(input_path: Path | str) -> int:
    position = 50
    zero_count = 0

    with open(input_path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            direction = line[0]
            distance = int(line[1:])

            # Count how many times we pass through 0 during this rotation
            # Each click moves us one position, and we make 'distance' clicks
            # We need to count how many of those clicks land on 0

            if direction == "L":
                # Moving left (toward lower numbers)
                # From position p, after k clicks we're at (p - k) % 100
                # We hit 0 when (p - k) % 100 == 0, i.e., k ≡ p (mod 100)
                # For k in 1..distance, count how many times k ≡ p (mod 100)
                # This happens at k = p, p+100, p+200, ... (for k >= 1)
                if position == 0:
                    # First hit at k=100, then k=200, etc.
                    zero_count += distance // 100
                else:
                    # First hit at k=position, then k=position+100, etc.
                    if distance >= position:
                        zero_count += 1 + (distance - position) // 100
                position = (position - distance) % 100
            else:  # R
                # Moving right (toward higher numbers)
                # From position p, after k clicks we're at (p + k) % 100
                # We hit 0 when (p + k) % 100 == 0, i.e., k ≡ -p ≡ (100-p) (mod 100)
                # For k in 1..distance, count how many times k ≡ (100-p) (mod 100)
                if position == 0:
                    # First hit at k=100, then k=200, etc.
                    zero_count += distance // 100
                else:
                    first_hit = 100 - position
                    if distance >= first_hit:
                        zero_count += 1 + (distance - first_hit) // 100
                position = (position + distance) % 100

    return zero_count


def main() -> None:
    input_file = Path(__file__).parent / "input.txt"
    print(f"Part 1: {solve_part1(input_file)}")
    print(f"Part 2: {solve_part2(input_file)}")


if __name__ == "__main__":
    main()
