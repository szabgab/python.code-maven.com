from fibonacci import fib


def test_fib_1():
    assert fib(1)  == 0

def test_fib_7():
    assert fib(7)  == 8

def test_fib_10():
    assert fib(10) == 34

def test_fib_42():
    assert fib(42) == 165580141

