# Pytest Change the text of the exception

What if someone changes the text of the exception?

{% embed include file="src/examples/pytest/fib3/fibonacci.py" %}

{% embed include file="src/examples/pytest/fib3/test_fibonacci.py" %}

**Output:**

{% embed include file="src/examples/pytest/fib3/test_fibonacci.out" %}

If the change was unintentional then the test helped us catch this.
If it was intentional then someone will have to ajust the test as well.

