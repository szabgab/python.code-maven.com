from incrementer import inc_5, inc_7

def test_inc_5():
    assert inc_5(1) == 6
    assert inc_5(-5) == 0

def test_inc_7():
    assert inc_7(1) == 8
    assert inc_7(-5) == 2

