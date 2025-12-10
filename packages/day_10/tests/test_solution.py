import pytest

from day_10.solution import solve_part1, solve_part2


@pytest.fixture
def example_input():
    return """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""


def test_part1_example(example_input):
    assert solve_part1(example_input) == 7


def test_part2_example(example_input):
    assert solve_part2(example_input) == 33
