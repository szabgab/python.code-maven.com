import mymath
import pytest

cases = [
    (1, 1, 2),
    (2, 3, 5),
    (-1, 1, 0),
    (-1, -1, -2),
]

@pytest.mark.parametrize("a,b,expected", cases)
def test_add(a, b, expected):
    assert mymath.add(a, b)  == expected

