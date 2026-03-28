# Flask

## Other parameters

There are two

```
$ FLASK_APP=app FLASK_DEBUG=1  flask run --port 8080 --host 0.0.0.0
```

logging:
    what happens to logging in a production server where is it logging to?
    how can I change the logging format?
    how can I configure the logging using an external configuration file?
    See the log-other example

Link to [HTTP Status code](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status)

Exercises change the calculator to use a form and redirect

Implement a simple url shortener
    form: get url, generate unix short id, save both in some "database" (can be a file).
    path: get the short id and redirect to the original url (looked up in the "database").

Show how the one function for both GET and POST and the separate functions work in a more complete example.

Take the jinja examples from python.org.il and show them in the slides.
