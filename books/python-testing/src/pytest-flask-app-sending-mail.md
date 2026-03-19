# Pytest: Flask app sending mail

This is a web application that allows the user to register by providing an email.
The system then generates a unique code and sends an email to the registered address
with a link back to the server.

The user is expected to click on the link in the email to verify that it is indeed his email address
and he wanted to subscribe.

{% embed include file="src/examples/pytest/mocking-flask/app.py" %}

