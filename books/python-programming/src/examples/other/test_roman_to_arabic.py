import pytest
from roman_to_arabic import roman_to_arabic

@pytest.mark.parametrize("roman, arabic", [
    ("I", 1),
    ("V", 5),
    ("X", 10),
    ("L", 50),
    ("C", 100),
    ("D", 500),
    ("M", 1000),
    ("II", 2),
    ("III", 3),
    ("IV", 4),
    ("MMMCLXXVIII", 3178),
    ("MMMCMXCIX", 3999),
])
def test_roman_to_arabic(roman, arabic):
    assert roman_to_arabic(roman) == arabic

def test_bad_1():
    with pytest.raises(ValueError) as err:
        roman_to_arabic("Z")
    assert str(err.value) == "Invalid character 'Z'"

def test_bad_2():
    with pytest.raises(ValueError) as err:
        roman_to_arabic("IVZ")
    assert str(err.value) == "Invalid character 'Z'"

#def test_bad_2():
#    with pytest.raises(ValueError) as err:
#        roman_to_arabic("IIII")
#    assert str(err.value) == "Invalid roman number 'IIII'"


