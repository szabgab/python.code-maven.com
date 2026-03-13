from fibonacci import fib


def test_fib():
    assert fib(1)  == 0
    assert fib(7)  == 8
    assert fib(10) == 34
    assert fib(42) == 165580141

