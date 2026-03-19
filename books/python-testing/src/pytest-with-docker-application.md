# Pytest with Docker - application

This is the Flask-based web application.

The main page returns some text.

The '/api/calc` URL accepts 2 parameters: `a` and `b` with two numbers.
It returns a JSON with these values and their sum.

{% embed include file="src/examples/pytest/docker/app.py" %}

