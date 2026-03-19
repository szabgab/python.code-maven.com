# Pytest: Hard-coded path - `monkeypatch` attribute - `tmpdir`

An even better approach might be to use the [tmpdir](https://docs.pytest.org/en/stable/reference/reference.html#tmpdir) fixture to create a temporary folder, create the necessary file(s) there and use the [monkeypatch](https://docs.pytest.org/en/stable/reference/reference.html#monkeypatch) fixture to point there.

{% embed include file="src/examples/pytest/hard-coded-path/test_app_monkeypatch_tempdir.py" %}


{% embed include file="src/examples/pytest/hard-coded-path/test_app_monkeypatch_tempdir.out" %}


