# Exercise: parametrize the tests of the math functions

In this example we have several test cases in each test function.
That means if one of the assertions fail the whole function fails and we
don't know what would be the result of the other test assertions.

{% embed include file="src/examples/pytest/test_math.py" %}

We could split up the test cases to several test functions along this example:

{% embed include file="src/examples/pytest/test_math_separated.py" %}

