import pytest


def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y


def test_divide():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        result = divide(10, 0)
        print("Result", result)
