# Pytest testing expected exception

Pytest provides a tool that allows us to "expect and exception".
We'll usually use it using a `with` context manager.

Here we can see two different ways to verify the exception.

{% embed include file="src/examples/pytest/fib2/test_fibonacci.py" %}

**Output:**

{% embed include file="src/examples/pytest/fib2/test_fibonacci.out" %}


Now that we are testing the exception let's see how will this test protect us?

* Someone changing the text of the exception.
* Someone removing the exception.
