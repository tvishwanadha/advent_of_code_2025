import pytest

from day_05.solution import solve_part1, solve_part2


@pytest.fixture
def example_input():
    return """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""


def test_part1_example(example_input):
    assert solve_part1(example_input) == 3


def test_part2_example(example_input):
    assert solve_part2(example_input) == 14
