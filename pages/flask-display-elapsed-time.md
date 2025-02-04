---
title: "Flask: display elapsed time"
timestamp: 2019-07-17T20:30:01
tags:
  - Flask
  - before_request
  - g
published: true
books:
  - flask
author: szabgab
archive: true
---


In some applications it is a nice idea to show how long it took to load a page. Using the `g` global object and
attaching a function call to it, we can do this fairly close to the real value, without needing to add a lot of extra
code to every route just by using the `before_request` decorator.


{% include file="examples/flask/elapsed_time/app.py" %}

{% include file="examples/flask/elapsed_time/templates/main.html" %}

Start the application with this command:

```
FLASK_APP=app FLASK_DEBUG=1 flask run --host 0.0.0.0 --port 5000
```

See the [Flask API](https://flask.palletsprojects.com/en/1.0.x/api/) for more explanation.

