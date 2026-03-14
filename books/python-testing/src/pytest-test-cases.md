# Test cases of mymath

We could create a data structure holding all the cases and add a loop to the test function. e.g. to test the `add` function we could create list of tuples where in each tuple the first two values are the input values and the last one is the expected output.

{% embed include file="src/examples/pytest/parametrize/test_mymath_cases.py" %}

