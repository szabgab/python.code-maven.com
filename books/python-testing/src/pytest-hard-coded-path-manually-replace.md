# Pytest: Hard-coded path - manually replace attribute


{% embed include file="src/examples/pytest/hard-coded-path/test_app_manually.py" %}

---

We set the path in one of the test-functions, but it will be set in both.

```
pytest -v -s test_app_manually.py
```
{% embed include file="src/examples/pytest/hard-coded-path/test_app_manually_all.out" %}

---

Run test 1, we see the path we set:

```
pytest -v -s test_app_manually.py::test_app_1
```

{% embed include file="src/examples/pytest/hard-coded-path/test_app_manually_1.out" %}

---

Run test 2, we see a the original path:


```
pytest -v -s test_app_manually.py::test_app_2
```

{% embed include file="src/examples/pytest/hard-coded-path/test_app_manually_2.out" %}
