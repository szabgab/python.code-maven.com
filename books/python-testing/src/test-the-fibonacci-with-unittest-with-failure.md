# Test the Fibonacci failure


{% embed include file="src/examples/testing/bad/test_fibonacci_with_unittest_failure.py" %}

```
$ python -m unittest test_fibonacci_with_unittest_failure.py
F
======================================================================
FAIL: test_fib (test_fibonacci_with_unittest_failure.TestFibo.test_fib)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "src/examples/testing/bad/test_fibonacci_with_unittest_failure.py", line 7, in test_fib
    self.assertEqual(fib(1), 0)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^
AssertionError: 1 != 0

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
```

```
$ echo $?
1
```

We can see that there is a problem, we can even see the error message, but we don't know what would be the result of the other 3 test-cases. Because the first test-case already raised an exception and stopped the processing, we don't know if the other would pass or if all the others would fail as well.

Maybe in our current situation it is not that important. After all we just added a test-case and we know the others passed before we added this. However if you have a bunch of tests. You make a change to your code and then you see such a failure then you'd want to know if the change impacted only one test-case, more than one case or all of them.


