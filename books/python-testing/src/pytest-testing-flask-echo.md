# Pytest: testing Flask echo GET

We have a fixture that will return the [Flask test_client](https://flask.palletsprojects.com/en/stable/testing/) that we can use in every test function to send a `get` request.

{% embed include file="src/examples/pytest/flask/test_echo_get.py" %}
