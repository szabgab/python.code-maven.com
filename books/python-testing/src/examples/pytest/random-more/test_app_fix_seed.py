import app
import random

def test_random_sum():
    random.seed(42)
    result = app.random_sum(3)
    assert result == 11


def test_random_8():
    random.seed(42)
    result = app.random_sum(8)
    assert result == 24

# Assginment: create a parametrized set of tests
