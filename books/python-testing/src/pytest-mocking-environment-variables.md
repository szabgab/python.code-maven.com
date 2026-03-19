# Pytest: Mocking environment variables

Just some simple application that uses environment variables.

{% embed include file="src/examples/pytest/setenv/app.py" %}

Use the module on the command line:

```
$ INPUT_A=23 INPUT_B=19 python use_app.py
42
```

{% embed include file="src/examples/pytest/setenv/use_app.py" %}

Test the module setting the envrionment variable.

{% embed include file="src/examples/pytest/setenv/test_app.py" %}


