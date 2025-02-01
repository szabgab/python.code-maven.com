---
title: "Python Flask: execute code before every request"
timestamp: 2020-06-23T07:30:01
tags:
  - Flask
  - before_request
published: true
books:
  - flask
author: szabgab
archive: true
show_related: true
---


Sometime there is some code that you would like to run at the beginning of every request. Insead of insert the same code everywhere or
event just inserting a function call in every route handler, Flask has an easy way to accomplish this using the <b>before_request</b> hook.


{% include file="examples/flask/before_request/app.py" %}

Run as:

```
FLASK_APP=app FLASK_DEBUG=1 flask run
```


Output on the console:

```
[2020-06-22 23:24:56,675] INFO in app: before_request
[2020-06-22 23:24:56,675] INFO in app: main route
127.0.0.1 - - [22/Jun/2020 23:24:56] "GET / HTTP/1.1" 200 -
```
