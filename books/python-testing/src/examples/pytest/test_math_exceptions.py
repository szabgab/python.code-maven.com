import math
import pytest

def test_math():
    with pytest.raises(Exception) as exinfo:
        math.factorial(-1)
    assert exinfo.type == ValueError
    assert str(exinfo.value) == 'factorial() not defined for negative values'

    with pytest.raises(Exception) as exinfo:
        math.factorial(1.2)
    assert exinfo.type == TypeError
    assert str(exinfo.value) == "'float' object cannot be interpreted as an integer"

    # Actually, if I am not mistaken this used to be a ValueError with this message:
    # 'factorial() only accepts integral values'

