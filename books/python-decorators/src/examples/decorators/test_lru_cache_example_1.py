from lru_cache_example_1 import compute

def test_compute(capsys):
    compute(1, 2)
    check(capsys, "Called with 1 and 2\n")
    compute(1, 2)
    check(capsys, "")
    compute(1, 2)
    check(capsys, "")

    compute(1, 3)
    check(capsys, "Called with 1 and 3\n")
    compute(1, 3)
    check(capsys, "")

    compute(1, 4) # Called with 1 and 4
    check(capsys, "Called with 1 and 4\n")
    compute(1, 4)
    check(capsys, "")

    compute(1, 5) # Called with 1 and 5
    check(capsys, "Called with 1 and 5\n")
    check(capsys, "")

    compute(1, 2)
    # This is called again as the previos 3 pushed this out from the cache
    check(capsys, "Called with 1 and 2\n")
    compute(1, 2)
    check(capsys, "")

def check(capsys, expected_out):
    out, err = capsys.readouterr()
    assert err == ''
    assert out == expected_out
