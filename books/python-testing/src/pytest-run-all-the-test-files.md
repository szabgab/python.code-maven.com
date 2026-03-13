# Pytest run all the test files

In the `src/examples/testing/good` folder run `pytest`.

```
$ pytest
=========================================== test session starts ============================================
platform linux -- Python 3.13.7, pytest-9.0.2, pluggy-1.6.0
rootdir: /home/gabor/github/code-maven.com/python.code-maven.com
configfile: pyproject.toml
plugins: anyio-4.12.0, cov-7.0.0
collected 7 items

test_mymath_with_pytest.py .                                                                         [ 14%]
test_mymath_with_pytest_class.py .                                                                   [ 28%]
test_mymath_with_unittest.py .                                                                       [ 42%]
test_mymath_with_unittest_separated.py ....                                                          [100%]

============================================ 7 passed in 0.06s =============================================
```

It found all the `test_*` files and all the `test_*` functions. (and also the `Test*` class and the `test_` methods).
It ran them all and reported the results.

If you run the same in the `src/examples/testing/` folder then it will find a lot more test-cases, many of which will fail
as we had a number of examples showing failure.

