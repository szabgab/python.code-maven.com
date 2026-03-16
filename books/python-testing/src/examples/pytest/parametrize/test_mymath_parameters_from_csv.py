import mymath
import pytest
import csv

filename = "cases.csv"

cases = []
with open(filename, "r") as fh:
    reader = csv.reader(fh)
    next(reader, None) # skip first row
    for line in reader:
        cases.append(tuple(map(int, line)))
        #cases.append(list(map(int, line)))
        #cases.append(list(map(float, line)))
print(cases)

@pytest.mark.parametrize("a,b,expected", cases)
def test_add(a, b, expected):
    assert mymath.add(a, b)  == expected

