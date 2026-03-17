# Pytest fixture - `tmpdir`

* Probably the simples fixture that PyTest provides is the `tmpdir`.
* Pytest will prepare a temporary directory and call the test function passing the path to the `tmpdir`.
* PyTest will also clean up the temporary folder, though it will keep the 3 most recent ones. (this is configurable)
* [tmp_path](https://docs.pytest.org/en/stable/how-to/tmp_path.html) is [pathlib.Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path).

{% embed include file="src/examples/pytest/test_tmpdir.py" %}

```
pytest -sq test_tmpdir.py
```

