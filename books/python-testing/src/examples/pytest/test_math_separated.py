import math

def test_gcd_6_9():
    assert math.gcd(6, 9) == 3

def test_gcd_17_9():
    assert math.gcd(17, 9) == 1

def test_ceil_0():
    assert math.ceil(0) == 0

def test_ceil_0_1():
    assert math.ceil(0.1) == 1

def test_ceil__0_1():
    assert math.ceil(-0.1) == 0

def test_factorial_0():
    assert math.factorial(0) == 1

def test_factorial_1():
    assert math.factorial(1) == 1

def test_factorial_2():
    assert math.factorial(2) == 2

def test_factorial_3():
    assert math.factorial(3) == 6

