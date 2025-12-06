import pytest

from day_02.solution import solve_part1, solve_part2


@pytest.fixture
def example_input():
    return """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""


def test_part1_example(example_input):
    assert solve_part1(example_input) == 1227775554


def test_part2_example(example_input):
    assert solve_part2(example_input) == 4174379265
