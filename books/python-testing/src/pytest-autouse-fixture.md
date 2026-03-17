# Pytest Fixture - autouse fixtures (using `yield`)

Using the `@pytest.fixture` decorator we can designate some function to be called automatically before and/or after each test.

If we set the `scope` to `module` then the fixtures will be similar to the `setup_module`, `teardown_module` functions of the xUnit style.

If we set the`scope` to `function` then the fixtures will be similar to the `setup_function`, `teardown_function` functions of the xUnit style.

{% embed include file="src/examples/pytest/test_autouse_fixtures.py" %}

**Output:**

{% embed include file="src/examples/pytest/test_autouse_fixtures.out" %}

