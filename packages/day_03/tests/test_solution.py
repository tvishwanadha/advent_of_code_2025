import pytest

from day_03.solution import solve_part1, solve_part2


@pytest.fixture
def example_input():
    return """987654321111111
811111111111119
234234234234278
818181911112111"""


def test_part1_example(example_input):
    assert solve_part1(example_input) == 357


def test_part2_example(example_input):
    assert solve_part2(example_input) == 3121910778619
