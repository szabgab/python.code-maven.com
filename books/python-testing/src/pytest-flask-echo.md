# Pytest: Flask echo GET

A simple web application with a static page showing an HTML form with a text box and a button.
Pressing the button will send the text we enetered in the box to the server which will echo it back.

We need to install `flask` using `pip install flask` then we can run the application:

```
flask --app echo_get --debug run
```

Then visit http://localhost:5000/ and try the "application".

Stop the web server by clicking "Ctrl-C".

{% embed include file="src/examples/pytest/flask/echo_get.py" %}



