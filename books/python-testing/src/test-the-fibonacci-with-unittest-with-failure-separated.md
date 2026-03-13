# Test the Fibonacci failure separated

Now if we add a 4th test function and run the test we can see it reports `F...`. `F` meaning the first test-case failed and the 3 dots indicating that the other 3 test-cases passed.


{% embed include file="src/examples/testing/bad/test_fibonacci_with_unittest_failure_separated.py" %}

```
$ python -m unittest test_fibonacci_with_unittest_failure_separated.py 
F...
======================================================================
FAIL: test_1 (test_fibonacci_with_unittest_failure_separated.TestFibo.test_1)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/gabor/github/code-maven.com/python.code-maven.com/books/python-testing/src/examples/testing/bad/test_fibonacci_with_unittest_failure_separated.py", line 7, in test_1
    self.assertEqual(fib(1), 0)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^
AssertionError: 1 != 0

----------------------------------------------------------------------
Ran 4 tests in 0.001s

FAILED (failures=1)
```
