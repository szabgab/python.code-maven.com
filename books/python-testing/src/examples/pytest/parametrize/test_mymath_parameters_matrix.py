import mymath
import pytest

@pytest.mark.parametrize("a", [1, 2, 3])
@pytest.mark.parametrize("b", [4, 5, 6])
def test_add(a, b):
    assert mymath.add(a, b) > 0

