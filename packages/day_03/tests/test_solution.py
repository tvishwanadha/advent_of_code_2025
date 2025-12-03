import tempfile
from pathlib import Path

from day_03.solution import solve_part1, solve_part2


def test_part1_example():
    example_input = """987654321111111
811111111111119
234234234234278
818181911112111"""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        f.write(example_input)
        f.flush()
        result = solve_part1(Path(f.name))

    assert result == 357


def test_part2_example():
    example_input = """987654321111111
811111111111119
234234234234278
818181911112111"""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        f.write(example_input)
        f.flush()
        result = solve_part2(Path(f.name))

    assert result == 3121910778619
