# Add extra command line parameters to Pytest - conftest - getoption

In the `conftest.py` file we can use the `pytest_addoption` function to defined new command line options.

* `--demo` expects a value.
* `--noisy` is a boolean flag. By default it is false.


In the tests we need to use the `request` fixture and the `getoption` method to get the value of each option

* See [Parser](https://docs.pytest.org/en/stable/reference.html#parser)
* See [argparse](https://docs.python.org/library/argparse.html)

{% embed include file="src/examples/pytest/py1/conftest.py" %}
{% embed include file="src/examples/pytest/py1/test_one.py" %}

```
pytest -s
None
False
```

```
pytest -s --demo Hello --noisy
Hello
True
```


