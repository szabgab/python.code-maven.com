import pytest
from transpose_text import transpose_text

@pytest.mark.parametrize("text, width, out", [
    ("a", 1, "a"),
    ("a", 2, "a"),
    ("ab", 2, "ab"),
    ("abcdefg", 2, "acegbdf"),
    ("abcdef", 2, "acebdf"),
    ("abcdefg", 3, "adgbecf"),
    ("abcdef", 3, "adbecf"),
    ("abcde", 3, "adbec"),
])
def test_1(text, width, out):
    assert transpose_text(text, width) == out

