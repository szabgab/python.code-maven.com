# PyTest: Multiple Failures output

The normal output will indicate that 3 of the 5 tests passed and 2 failed:

```
test_failures.py .F.F.
```

We can use the verbose flag (`-v`) to get a more detailed report:

```
$ pytest -v test_failures.py

test_failures.py::test_one PASSED
test_failures.py::test_two FAILED
test_failures.py::test_three PASSED
test_failures.py::test_four FAILED
test_failures.py::test_five PASSED
```

We can alos use the `-s` flag to let pytest show what we printed on the screen during the test run.
This will show the text in the cases of the where the assertion was successful we can see the print statements both before and after the assertion. In the cases when the assertion failed we only see the print statements before the assertion.

```
$ pytest -s test_failures.py

one before
one after
two before
three before
three after
four before
five before
five after
```


