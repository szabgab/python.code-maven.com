---
title: "Upload multiple files with HTML and Flask"
timestamp: 2021-10-10T12:30:01
tags:
  - Flask
  - HTML
published: true
books:
  - flask
author: szabgab
archive: true
show_related: true
---


Code to upload multiple files with HTML and Flask.


Directory structure:

```
dir/
├── app.py
├── files
└── templates
    └── upload.html
```

{% include file="examples/flask/upload/app.py" %}

{% include file="examples/flask/upload/templates/upload.html" %}

Run as:

```
FLASK_DEBUG=1 flask run
```
