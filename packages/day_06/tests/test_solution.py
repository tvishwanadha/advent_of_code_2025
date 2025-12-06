import pytest

from day_06.solution import solve_part1, solve_part2


@pytest.fixture
def example_input():
    return """123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +  """


def test_part1_example(example_input):
    # 123 * 45 * 6 = 33210
    # 328 + 64 + 98 = 490
    # 51 * 387 * 215 = 4243455
    # 64 + 23 + 314 = 401
    # Total: 33210 + 490 + 4243455 + 401 = 4277556
    assert solve_part1(example_input) == 4277556


def test_part2_example(example_input):
    # Reading right-to-left, column by column:
    # Rightmost problem: 4 + 431 + 623 = 1058
    # Second from right: 175 * 581 * 32 = 3253600
    # Third from right: 8 + 248 + 369 = 625
    # Leftmost: 356 * 24 * 1 = 8544
    # Total: 1058 + 3253600 + 625 + 8544 = 3263827
    assert solve_part2(example_input) == 3263827
