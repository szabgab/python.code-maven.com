import mymath

# We can have all the cases in one test function
def test_add_all():
    assert mymath.add(1, 1)  == 2
    assert mymath.add(2, 3)  == 5
    assert mymath.add(-1, 1)  == 0

