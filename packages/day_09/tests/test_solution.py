import pytest

from day_09.solution import solve_part1, solve_part2


@pytest.fixture
def example_input():
    return """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""


def test_part1_example(example_input):
    assert solve_part1(example_input) == 50


def test_part2_example(example_input):
    assert solve_part2(example_input) == 24
