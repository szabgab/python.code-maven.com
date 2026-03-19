# Pytest: Hard-coded path - `monkeypatch` attribute

We can also use the `setattr` method of the [monkeypatch](https://docs.pytest.org/en/stable/reference/reference.html#monkeypatch) fixture.

The path is still rather fixed, but now it is fixed in the test.
So we could prepare a few config file and use them in the tests.

{% embed include file="src/examples/pytest/hard-coded-path/test_app_monkeypatch.py" %}


---

When running all the tests the first one will have the mocked filename the second one will have the hard-coded one.

```
$ pytest -s -q test_app_monkeypatch.py
```

{% embed include file="src/examples/pytest/hard-coded-path/test_app_monkeypatch_all.out" %}

---

When running the tests separately each one of them will have the same filename as they had when we ran them together.

```
$ pytest -s -q test_app_monkeypatch.py::test_app_1
```

{% embed include file="src/examples/pytest/hard-coded-path/test_app_monkeypatch_1.out" %}

```
$ pytest -s -q test_app_monkeypatch.py::test_app_2
```

{% embed include file="src/examples/pytest/hard-coded-path/test_app_monkeypatch_2.out" %}



