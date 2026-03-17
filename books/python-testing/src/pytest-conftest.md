# Share fixtures among test files: conftest.py

You can create a file called `conftest.py` and place it in the root of the test folder or the root of the project if you don't have a test-folder. Pytest will automaticall import its functions into every test.

{% embed include file="src/examples/pytest/autouse/conftest.py" %}
{% embed include file="src/examples/pytest/autouse/test_blue.py" %}
{% embed include file="src/examples/pytest/autouse/test_green.py" %}

```
pytest -qs
```

**Output:**

{% embed include file="src/examples/pytest/autouse/pytest.out" %}



