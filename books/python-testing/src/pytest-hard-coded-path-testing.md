# Pytest: Hard-coded path - testing

The problem with this is that when trying to test the application, the test will also
use the same hard-coded path. Thus we cannot test with values that are different from
what the corporation has. This might include the credentials of the production database.

Not good.

{% embed include file="src/examples/pytest/hard-coded-path/test_app.py" %}

```
pytest -s test_app.py
```

{% embed include file="src/examples/pytest/hard-coded-path/test_app.out" %}
