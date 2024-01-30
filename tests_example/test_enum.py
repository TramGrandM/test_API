from enum import Enum, unique

import pytest


@unique
class Day(Enum):
    Monday = 2
    Tuesday = 3
    Wednesday = 4
    Thursday = 5
    Friday = 6
    Saturday = 7
    Sunday = 8


@pytest.mark.xfail
def test_xfail():
    assert 1 + 1 == 3


def test_enum():
    print("\n", Day(7).name)
    print(Day.Sunday.name)


@pytest.mark.skip(reason="Test skip")
def test_skip():
    print("Test skip")
