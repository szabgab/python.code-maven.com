# Pytest capture STDOUT and STDERR with `capsys`

The `capsys` fixture captures everything that is printed to STDOUT and STDERR so we can compare that to the expected output and error.

* We need to include `capsys` as the parameter of the test function.
* The first call to `readouterr` will return whatever was printed to STDOUT and STDERR respectively from the start of the test function.
* The subsequent calls to `readouterr` will return the output that was generated since the previous call to `readouterr`.

{% embed include file="src/examples/pytest/test_greet.py" %}

```
pytest test_greet.py
```

Note, however, using `-s` won't print anything extra in this case as the ourput was captured by `capsys`.

```
pytest -s test_greet.py
```

