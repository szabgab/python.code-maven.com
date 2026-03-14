import math
import pytest

def test_gcd():
    assert math.gcd(6, 9) == 3
    assert math.gcd(17, 9) == 1

@pytest.mark.parametrize("val,expected", [
    (0, 0),
    (0.1, 1),
    (-0.1, 0),
    ])
def test_ceil(val, expected):
    assert math.ceil(val) == expected

@pytest.mark.parametrize("n,expected", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    ])
def test_factorial(n, expected):
    assert math.factorial(n) == expected

