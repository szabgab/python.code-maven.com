# Multiple Failures in separate test functions

Every test function is executed separately. Normally pytest will run all the test functions, collect the results
and display a summary. In this example we have 5 test functions. We don't really test anything in them but calling `assert False` will fail the given test.


{% embed include file="src/examples/pytest/test_failures.py" %}

We can run this as `pytest test_failures.py` and observe the results.
