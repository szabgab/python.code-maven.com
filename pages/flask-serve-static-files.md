---
title: "Python Flask: serve static files: (CSS, JavaScript, images, etc.)"
timestamp: 2019-09-06T07:30:01
tags:
  - flask
published: true
books:
  - flask
author: szabgab
archive: true
---


Unless it is only an API returning JSON files, in a web application you will have many static files.
Images, CSS files, JavaScript files, etc. Usually on your production server you will want these
to be served by a web server such as nginx or Apache as those are faster and more suitable for such job.

However during development you probably won't want to have a web server on your computer. For that time
you probbaly need Flask to serve the static files as well.

Flask can do it easily, out of the box.


## static

The key is that you put the static files in a directory called <b>static</b> next to the main application file
and in the HTML skeleton you refer to the files as <b>/static/...</b>.

I put the css file in a subdirectory called css and the image in a subdirectory called img. This is not a requirement,
but might be a good practice to arrange them this way.


See the example:

We have the following directory layout:

```
.
├── static
│   ├── css
│   │   └── style.css
│   └── img
│       └── code_maven_128.png
├── templates
│   └── main.html
└── web.py
```

The "application" is rather simple. It has only one page returning a rendered template:

{% include file="examples/flask/stat/web.py" %}

The template itself is also simple. It is based on the [HTML 5 skeleton](/html-skeleton)
and it refers to both a CSS file and an image using the path from the directory where
the application file is found.

{% include file="examples/flask/stat/templates/main.html" %}

The CSS itself is also very simple, its content is not relevant for our purposes.

{% include file="examples/flask/stat/static/css/style.css" %}

## How to run this

There are two simple ways to run this in developlent. For both you need to open your terminal (cmd window if you are on
Windows), change to the directory where the application file (web.py in our case) can be found.

```
python web.py
```

A better way, that provides more control over how to run this is to use:

```
FLASK_APP=web FLASK_DEBUG=1 flask run --port 3000 --host 127.0.0.1
```


