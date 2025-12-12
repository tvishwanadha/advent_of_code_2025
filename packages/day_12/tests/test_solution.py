import pytest

from day_12.solution import solve_part1


@pytest.fixture
def example_input():
    return """0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2"""


def test_part1_example(example_input):
    assert solve_part1(example_input) == 2
