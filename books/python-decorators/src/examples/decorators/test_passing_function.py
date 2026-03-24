from passing_function import call, double, square

def test_call():
    assert double(3) == 6
    assert call(double) == 84

    assert square(2) == 4
    assert call(square) == 1764
