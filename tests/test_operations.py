import pytest
from calculator import operations

@pytest.mark.parametrize("func,a,b,expected", [
    (operations.add, 2, 3, 5),
    (operations.subtract, 5, 2, 3),
    (operations.multiply, 3, 4, 12),
    (operations.divide, 8, 2, 4)
])
def test_operations(func, a, b, expected):
    assert func(a, b) == expected

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        operations.divide(5, 0)
