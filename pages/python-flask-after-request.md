---
title: "Python Flask: execute code after every request"
timestamp: 2020-06-23T13:30:01
tags:
  - Flask
  - after_request
published: true
books:
  - flask
author: szabgab
archive: true
show_related: true
---


Sometime there is some code that you would like to run after the requests was served.  The <b>after_request</b> hook
can help you in this, thoigh beware, it won't run in the rare (well, hopefully rare) cases when there is an
uncaught exception in the route.


{% include file="examples/flask/after_request/app.py" %}

Run as:

```
FLASK_APP=app FLASK_DEBUG=1 flask run
```

Output on the console:

```
[2020-06-23 13:21:22,699] INFO in app: main route
[2020-06-23 13:21:22,699] INFO in app: after_request
127.0.0.1 - - [23/Jun/2020 13:21:22] "GET / HTTP/1.1" 200 -
```


Visiting the http://localhost:5000/crash URL shows a stack trace like this:

```
[2020-06-23 13:21:11,582] INFO in app: crash route
127.0.0.1 - - [23/Jun/2020 13:21:11] "GET /crash HTTP/1.1" 500 -
Traceback (most recent call last):
  ...
  File "/home/gabor/work/code-maven.com/examples/flask/after_request/app.py", line 20, in crash
    b = 3 / a
ZeroDivisionError: division by zero
```

