---
title: "Flask routes - URL mapping - views"
timestamp: 2019-02-09T23:30:01
tags:
  - Flask
published: true
books:
  - flask
author: szabgab
archive: true
---


<a href=/flask">Flask</a> allows you to have a very flexible mapping of URL pathes to function calls. Let's see what can
you do.


A few notes for placeholders:

* Simple &lt;varname&gt; captures anything except slashes.
* &lt;<b>string</b>:varname&gt; is the default prefix so we don't really need to include it. It captures everything except a slash <b>/</b>
* &lt;<b>int</b>:varname&gt; accepts various [unicode digits](https://www.fileformat.info/info/unicode/category/Nd/list.htm) as well
* &lt;<b>float</b>:varname&gt; accpets a floating point numnber like 123.4, but it does not accept 1. or .1  or a simple integer like 42 without any dot.
* &lt;<b>path</b>:varname&gt; accepts any character, including slashes <b>/</b>.

This a sample Flask file with several possible path mappings.

Including one where we created our own rule to match routes that contain a valid IPv4 address.

{% include file="examples/flask/routes/app.py" %}

{% include file="examples/flask/routes/converters.py" %}

You can start the application by running

```
FLASK_APP=app FLASK_DEBUG=1 flask run
```

And then you can access it using some of the following URLs:

```
http://localhost:5000/
http://localhost:5000/some/path
http://localhost:5000/user/foobar
http://localhost:5000/user/          Not Found!
```

Feel free to try anything you like. Below you'll find the test cases that will help you see which
route matches which URLs.

You can use more than one placeholders in a route definition and you can even have fixed elements between the
placeholders, though I am not sure when would you want to have that.


## Testing the routes

I've also included sample code that will test each one of the given routes.

{% include file="examples/flask/routes/test_app.py" %}

As they are writtent these two files need to be in the same directory. You can cd in that directory on your terminal and
run:

```
pytest
```

If you run it with the `-s` flag then you'll also see the output from the `print` statements in the test
file.

```
pytest -s
```



[See also](http://exploreflask.com/en/latest/views.html)

## Comments

can I write on the one of html page which is in templates folder from any function in which is written in main flask file?
