import mymath

# We can separate them to several test functions
def test_add_1_1():
    assert mymath.add(1, 1)  == 2

def test_add_2_3():
    assert mymath.add(2, 3)  == 5

def test_add_minus_1_1():
    assert mymath.add(-1, 1)  == 0

