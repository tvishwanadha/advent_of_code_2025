import tempfile
from pathlib import Path

from day_05.solution import solve_part1, solve_part2


def test_part1_example():
    example_input = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        f.write(example_input)
        f.flush()
        result = solve_part1(Path(f.name))

    assert result == 3


def test_part2_example():
    example_input = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        f.write(example_input)
        f.flush()
        result = solve_part2(Path(f.name))

    assert result == 14
