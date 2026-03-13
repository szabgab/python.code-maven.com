# Test the Fibonacci separated

Just as in the previous case, we can separate the test-cases into separate functions. Soon we'll see the real value of this separation.


{% embed include file="src/examples/testing/bad/test_fibonacci_with_unittest_separated.py" %}

```
$ python -m unittest test_fibonacci_with_unittest_separated.py 
...
-------------------------------------------------------------
Ran 3 tests in 0.000s

OK

```
