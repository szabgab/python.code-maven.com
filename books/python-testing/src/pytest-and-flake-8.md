# Pytest and flake8

[flake8](https://flake8.pycqa.org/) - Style Guide Enforcement

{% embed include file="src/examples/pytest/flake/mymod.py" %}
{% embed include file="src/examples/pytest/flake/test_mymod.py" %}
{% embed include file="src/examples/pytest/flake/.flake8" %}

```
pip install flake8
pip install pytest-flake8
pip install flake8-builtins

flake8
rm -rf .pytest_cache/
pytest --flake8
```

