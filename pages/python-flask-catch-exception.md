---
title: "Python Flask: catch and handle exceptions in routes using errorhandler"
timestamp: 2020-06-26T10:30:01
tags:
  - Flask
  - Exception
  - errorhandler
  - ZeroDivisionError
published: true
books:
  - flask
author: szabgab
archive: true
show_related: true
---


No matter how much your test your code, there might be an occassional exception raised during the execution of
one of the routes in your code. You cannot wrap all the code in a huge <b>try</b>-<b>except</b> block, but you
can use the built-in error-handling of Flask using the <b>errrohandler</b> hook that we have already
seen when we wanted to have a unified look for [404 page not found](/flask-return-404).


## Catching the Exception

```
@app.errorhandler(Exception)
def server_error(err):
    app.logger.exception(err)
    return "exception", 500
```

Alternativelly, using a template:

```
@app.errorhandler(Exception)
def server_error(err):
    return render_template('crash.html'), 500
```


## Sample application handling the Exception

{% include file="examples/flask/catch_exception/app.py" %}

Run as:

```
FLASK_APP=app FLASK_DEBUG=1 flask run
```

Output on the console for regular pages.

```
[2020-06-26 10:33:22,903] INFO in app: main route
127.0.0.1 - - [26/Jun/2020 10:33:22] "GET / HTTP/1.1" 200 -
```


## Oputput of the crash

Visiting the http://localhost:5000/crash URL shows a stack trace like this on the command line:

```
[2020-06-26 10:33:29,633] INFO in app: crash route
[2020-06-26 10:33:29,633] ERROR in app: division by zero
Traceback (most recent call last):
  File ".../flask/app.py", line 1950, in full_dispatch_request
    rv = self.dispatch_request()
  File ".../flask/app.py", line 1936, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File ".../flask/catch_exception/app.py", line 20, in crash
    b = 3 / a
ZeroDivisionError: division by zero
127.0.0.1 - - [26/Jun/2020 10:33:29] "GET /crash HTTP/1.1" 200 -
```

The user only sees the word "exception".

Of course insted of returning that word, we could have used <b>render_template</b> to
render any page. The status code returned by the page will be 500 as indicated by the
second value returned.


## Catching specific exceptions

In the above examples we use the catch-all <b>Exception</b> class, but you can be more specific
about the exceptions and you can return different pages based on the error type.
You could do this by checking the <b>type</b> of the <b>err</b> variable, but a probably cleaner way
is to set up separate exception handler hooks for each exception type you'd like to deal with:

{% include file="examples/flask/catch_specific_exception/app.py" %}

## Logging the Exception

In the above examples we keept using the `app.logger.exception(err)` expression to log
the exception and the stack trace. If you are not interested in the stack-trace you can use
the <b>error</b> logging method: `app.logger.error(err)`.
