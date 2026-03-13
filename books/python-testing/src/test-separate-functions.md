# Each test case in its own method

We can put each check in a separate function.

{% embed include file="src/examples/testing/good/test_mymath_with_unittest_separated.py" %}

In this case the reporting will show 4 tests.

```
$ python -m unittest test_mymath_with_unittest_separated.py 
....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```

The advantage of putting them in separate functions is that then the tests can run independently.


