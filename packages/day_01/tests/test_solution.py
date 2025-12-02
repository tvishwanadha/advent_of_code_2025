import tempfile
from pathlib import Path

from day_01.solution import solve_part1, solve_part2


def test_part1_example():
    example_input = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        f.write(example_input)
        f.flush()
        result = solve_part1(Path(f.name))

    assert result == 3


def test_part2_example():
    example_input = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        f.write(example_input)
        f.flush()
        result = solve_part2(Path(f.name))

    assert result == 6
