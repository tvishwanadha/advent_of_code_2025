import pytest

from day_01.solution import solve_part1, solve_part2


@pytest.fixture
def example_input():
    return """L68
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


def test_part1_example(example_input):
    assert solve_part1(example_input) == 3


def test_part2_example(example_input):
    assert solve_part2(example_input) == 6
