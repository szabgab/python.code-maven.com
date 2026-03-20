# Flask Debugging

If you launch the Flask application using the `--debug` flag and your application enconteres and exception,
you can get the browser to open an interactive prompt where you can execute arbitrary Python code.

{% embed include file="src/examples/flask/debugging/app.py" %}


```
$ flask --app app --debug run
```

