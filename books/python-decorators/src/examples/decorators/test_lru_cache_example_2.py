from lru_cache_example_1 import compute

def test_compute(check_out):
    compute.cache_clear()

    compute(1, 2)
    check_out("Called with 1 and 2\n")
    compute(1, 2)
    check_out("")
    compute(1, 2)
    check_out("")

    compute(1, 3)
    check_out("Called with 1 and 3\n")
    compute(1, 3)
    check_out("")

    compute(1, 4)
    check_out("Called with 1 and 4\n")
    compute(1, 4)
    check_out("")

    compute(1, 2)
    check_out("")

    compute(1, 5)
    check_out("Called with 1 and 5\n")

    # This is now in the cache
    compute(1, 2)
    check_out("")

    # This is called again as the last addition pushed this out from the cache
    compute(1, 3)
    check_out("Called with 1 and 3\n")

    assert compute.cache_info().hits == 6
    assert compute.cache_info().misses == 5
    assert compute.cache_info().maxsize == 3
    assert compute.cache_info().currsize == 3

