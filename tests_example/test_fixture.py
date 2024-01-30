# import pytest
#
#
# @pytest.fixture
# def input_value():
#     a = 39
#     return a
#
#
# def test_check_input_1(input_value):
#     assert input_value % 3 == 0
#
#
# def test_check_input_2(input_value):
#     assert input_value % 2 == 0

import pytest


@pytest.fixture
def setup_database():
    print("Setting up the database")
    yield
    print("Tearing down the database")


@pytest.mark.usefixtures("setup_database")
def test_example():
    print("Running the test")
