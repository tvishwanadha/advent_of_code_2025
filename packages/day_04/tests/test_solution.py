import pytest

from day_04.solution import solve_part1, solve_part2


@pytest.fixture
def example_input():
    return """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""


def test_part1_example(example_input):
    assert solve_part1(example_input) == 13


def test_part2_example(example_input):
    assert solve_part2(example_input) == 43
