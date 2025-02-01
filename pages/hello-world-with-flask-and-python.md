---
title: "Hello World with Flask and Python"
timestamp: 2015-02-03T10:30:01
tags:
  - Flask
published: true
books:
  - python
  - flask
author: szabgab
archive: true
---


[Flask](http://flask.pocoo.org/) is a microframework for Python based on
[Werkzeug](http://werkzeug.pocoo.org/), [Jinja 2](http://jinja.pocoo.org/) and good intentions.

In this article we look at the "Hello World" of Flask also shown on the main page of the framework.


{% include file="examples/flask/hello_world.py" %}

After installing Flask with `pip install Flask` I could run the above script on the command line using

```
$ python examples/flask/hello_world.py 
```

The response was

```
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Then I turned my browser to the given URL and it indeed showed "Hello World!" while on the console I saw:

```
127.0.0.1 - - [03/Feb/2015 09:43:14] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [03/Feb/2015 09:43:14] "GET /favicon.ico HTTP/1.1" 404 -
```

The first one was my reql reuqest, the second one was my browser trying to be nice and trying to fetch the favicon of the site.
The first entry ended with [HTTP status 200](http://en.wikipedia.org/wiki/List_of_HTTP_status_codes) indicating success,
the second request ended with HTTP status 404, indicating "Not found".


The code itself seems to be straight forward.

We declared a function with an arbitrary name (`hello`), and used the `@app.route("/")`
decorator to map the request to `/` to this function.

```python
@app.route("/")
def hello():
    return "Hello World!"
```

When Flask runs, it accepts HTTP request and them maps the requests to routes based on the path in the request.
So the above code means if a request comes in for `/` then run the `hello` function.

At the end of the script we see this:

```python
if __name__ == "__main__":
    app.run()
```

The `app.run()` launches the web server with the Flask-based web application.
The `if __name__ == "__main__":` part protects it so the server will be only launched
if the file was executed as a script.

This will allow us to reuse the code in this file as part of another Flask-based application.

(In Perl this kind of behavior is referred to as a [Modulino](http://www.masteringperl.org/category/chapters/modulinos/).)

## A better Hello World example

<includ file="examples/flask/hw/hello_world.py">

This version cannot be launched with plain "python" we will need to use the already installed `flak` command.

Change to the directory where you put the "hello_world.py" file and then run:

```
FLASK_APP=hello_world flask run
```

It will print you a warnng:

```
 * Serving Flask app "hello_world.py"
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

That's fine for development.

## Run Flask on a different port

If port 5000 is already in use you can tell flask to use a different port:

```
FLASK_APP=hello_world flask run --port 3000
```

## Autoreload Flask app

When you are developing you application you will make frequent edits to the code.
In order for Flask to use the new code you will need to stop and start again the
Flask application. That's boring and a waste of energy.

Instead of that you can turn on debug mode by setting the `FLASK_DEBUG`
environment variable:

```
FLASK_APP=hello_world FLASK_DEBUG=1 flask run
```

IF you visit the page http://127.0.0.1:5000/ you can see the current results.
Then you can edit the file in a separate window (e.g. change the text returned 
to "Hello Flask!". On the terminal you will see that Flask notices the change
and restarts the application.

Then you can reload the browser page and see the new content.


## Listen on all the IP addresses

By default Flask will only listen on 127.0.0.1, that means you can access the web application
only from your own computer. This is a good security measurement.
However if you are running your code in some virtual computer (e.g. VirtualBox, Docker, etc.)
and your browser runs in your own computer, you will not be able to access the web application
as it only listens to itself.

The specific virtual environment might allow you to map an internal port to an external port,
but Flask also provides a way.

you can supply the `--host` flag:

```
FLASK_APP=hello_world flask run --host 0.0.0.0
```


## Everything together

```
FLASK_APP=hello_world FLASK_DEBUG=1 flask run --host 0.0.0.0 --port 3000
```

## Comments

how to resolve this error? GET /favicon.ico 404 NOT
FOUND


