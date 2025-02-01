---
title: "Python Flask: execute code once before first request"
timestamp: 2020-06-22T23:30:01
tags:
  - Flask
  - before_first_request
published: true
books:
  - flask
author: szabgab
archive: true
show_related: true
---


Sometimes you would like to have code that will be executed once, before ant user arrives to your site, before the first
request arrives. You could put some code in the body of your Flask application file, that code will execute
when the application launches. Alternatively, and in many case in a cleaner way you could use the <b>before_first_request</b> hook.


{% include file="examples/flask/before_first_request/app.py" %}

Run as:

```
FLASK_APP=app FLASK_DEBUG=1 flask run
```


Output on the console:

```
[2020-06-22 23:24:56,675] INFO in app: before_first_request
[2020-06-22 23:24:56,675] INFO in app: main route
127.0.0.1 - - [22/Jun/2020 23:24:56] "GET / HTTP/1.1" 200 -
```
