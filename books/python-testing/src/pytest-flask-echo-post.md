# Pytest: Flask echo POST

This is very similar to the previous "application" except here the form sends a "POST" request
and the server handles that.

{% embed include file="src/examples/pytest/flask/echo_post.py" %}

Run the application

```
flask --app echo_post --debug run
```

Visit http://localhost:5000/


