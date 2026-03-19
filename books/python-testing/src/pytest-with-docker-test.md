# Pytest with Docker  - test

This test uses xUnit-style fixtures and because we need to pass around some values it uses some `global` variable. Not ideal.

The fixtures build the image and run the container that launches the web application.

Then the tests use `request` to access the site.

{% embed include file="src/examples/pytest/docker/test_with_docker.py" %}


```
pytest test_with_docker.py
```
