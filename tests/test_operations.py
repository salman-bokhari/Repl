import pytest
from calculator import operations

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (-1, -1, -2),
    (2.5, 2.5, 5.0)
])
def test_add(a, b, expected):
    assert operations.add(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (5, 2, 3),
    (2, 5, -3),
    (0, 0, 0)
])
def test_subtract(a, b, expected):
    assert operations.subtract(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 6),
    (-1, 5, -5),
    (0, 99, 0)
])
def test_multiply(a, b, expected):
    assert operations.multiply(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (10, 2, 5),
    (-9, -3, 3),
    (2.5, 0.5, 5)
])
def test_divide(a, b, expected):
    assert operations.divide(a, b) == expected

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        operations.divide(1, 0)
