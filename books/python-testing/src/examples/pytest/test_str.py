import pytest


@pytest.mark.parametrize("val", ["a", "b", "א", "2"])
def test_isalnum(val):
    assert val.isalnum()

@pytest.mark.parametrize("val", ["_", " "])
def test_not_isalnum(val):
    assert not val.isalnum()
