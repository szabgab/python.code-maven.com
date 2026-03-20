# Sendmail from logger

As Flask is uses the standard [logging](https://docs.python.org/3/library/logging.html) library of Python,
we an also use the [logging.handlers.SMTPHandler](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.SMTPHandler) andconfigure the logger to send an email every time there is an ERROR-level log message.

{% embed include file="src/examples/flask/log/sendmail.py" %}
