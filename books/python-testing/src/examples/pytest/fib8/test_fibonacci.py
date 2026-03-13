import pytest
from fibonacci import fib

def test_fib():
    assert fib(10) == 55

def test_fib_negative():
    with pytest.raises(Exception) as err:
        fib(-1)
    assert err.type == ValueError
    assert str(err.value) == 'Invalid parameter -1 is negative'

def test_fib_negative_again():
    with pytest.raises(ValueError) as err:
        fib(-1)
    assert str(err.value) == 'Invalid parameter -1 is negative'

def test_fib_floating_point():
    with pytest.raises(ValueError) as err:
        fib(3.5)
    assert str(err.value) == 'Invalid value type of "3.5" is "float"'

def test_fib_small_floating_point():
    with pytest.raises(ValueError) as err:
        fib(0.5)
    assert str(err.value) == 'Invalid value type of "0.5" is "float"'

def test_fib_big_floating_point():
    with pytest.raises(ValueError) as err:
        fib(3.0)
    assert str(err.value) == 'Invalid value type of "3.0" is "float"'
