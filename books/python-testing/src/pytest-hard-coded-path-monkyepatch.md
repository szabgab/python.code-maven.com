# Pytest: Hard-coded path - `monkeypatch` attribute

We can also use the `setattr` method of the [monkeypatch](https://docs.pytest.org/en/stable/reference/reference.html#monkeypatch) fixture.

The path is still rather fixed, but now it is fixed in the test.
So we could prepare a few config file and use them in the tests.

{% embed include file="src/examples/pytest/hard-coded-path/test_app_monkeypatch.py" %}


