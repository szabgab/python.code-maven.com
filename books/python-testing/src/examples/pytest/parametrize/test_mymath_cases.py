import mymath

# We can create a dataset of the test-cases and loop over them.
def test_add_cases():
    cases = [
        (1, 1, 2),
        (2, 3, 5),
        (-1, 1, 0),
    ]
    for (a, b, expected) in cases:
        assert mymath.add(a, b) == expected

