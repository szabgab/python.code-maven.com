# Manual fixtures (using dependency injection)

If we don't set the `autouse` to `True` then by default it is `False`. Meaning you will have to explicitly use them. However instead of calling these function we use their names as parameters of our test functions. Pytest will notice that your test function requires certain parameters, it will find the fixture with the given name, call it, and set the variable to the value "returned" by the fixture.

{% embed include file="src/examples/pytest/test_manual_fixtures.py" %}

**Output:**

{% embed include file="src/examples/pytest/test_manual_fixtures.out" %}

* We can't add fixtures to test_functions as decorators (as I was the case in NoseTest), we need to use dependency injection.


