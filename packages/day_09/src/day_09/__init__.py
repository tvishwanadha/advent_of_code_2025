from pathlib import Path

from day_09.solution import solve_part1, solve_part2


def main() -> None:
    input_file = Path(__file__).parent / "input.txt"
    input_data = input_file.read_text()
    print(f"Part 1: {solve_part1(input_data)}")
    print(f"Part 2: {solve_part2(input_data)}")


if __name__ == "__main__":
    main()
