import pytest

@pytest.mark.parametrize("text", ["Foo", "Bar", "🐍🐪🦀"])
def test_cases_3(text):
    assert len(text) == 3

@pytest.mark.parametrize("text", ["apple", "banan"])
def test_cases_5(text):
    assert len(text) == 5

