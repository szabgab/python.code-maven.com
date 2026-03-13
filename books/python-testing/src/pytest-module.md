# Testing functions

As we start writing tests to be used by pytest we don't actually need to use pytest in the code.
We just need to create one or more files with a name starting with `test_`.

In those files one or more "test-functions", that is functions that start with `test_`.

Inside those function we can call the functions of the AUT and compare the returned values to the expected values passing
the result to the regular `assert` function of Python.

The `assert` function receives a boolean value. If it is `True` then `assert` does nothing. If it is `False` then `assert` raises an exception.

We **should not** call these test-functions ourselves! Pytest will do it for us.


{% embed include file="src/examples/testing/good/test_mymath_with_pytest.py" %}

Running the tests:

The place where we do need `pytest` is for running the tests.

```
pytest test_mymath_with_pytest.py
```

{% embed include file="src/examples/testing/good/test_mymath_with_pytest.out" %}


Pytest will read the content of the file(s), find the `test_...` functions and run each one of them.
If any of them raises an exception (because of the `assert` or otherwise`), pytest will collect this data
and create a report at the end.


In the above report you can see that pytest reported the name of the test-file. The single dot `.` following the filename indicates that there was one test function that passed.


After the test run we could also see the exit code of the program by typing in `echo $?` on Linux or Mac or `echo %ERRORLEVEL%` on Windows.

```
$ echo $?
0
```

```
> echo %ERRORLEVEL%
0
```


