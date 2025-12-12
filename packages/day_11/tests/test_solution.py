import pytest

from day_11.solution import solve_part1, solve_part2


@pytest.fixture
def example_input():
    return """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out"""


def test_part1_example(example_input):
    assert solve_part1(example_input) == 5


@pytest.fixture
def example_input_part2():
    return """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out"""


def test_part2_example(example_input_part2):
    assert solve_part2(example_input_part2) == 2
