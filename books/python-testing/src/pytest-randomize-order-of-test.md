# PyTest: Randomize Order of tests

The [pytest-random-order](https://pypi.python.org/pypi/pytest-random-order) provides a new command-line flag `--random-order` that will randomize the test-function.

```
pip install pytest-random-order
```

You might need to run the tests several times till you see exactly this random order.

```
$ pytest -v --random-order test_order.py

test_order.py::test_two PASSED
test_order.py::test_three PASSED
test_order.py::test_one PASSED
```


