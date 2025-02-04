---
title: "Python Flask Blueprint example with tests"
timestamp: 2021-05-12T16:30:01
tags:
  - Flask
  - Bluprint
  - pytest
published: false
books:
  - flask
author: szabgab
archive: true
show_related: true
---


<a href="https://flask.palletsprojects.com/en/2.0.x/blueprints/">Bluprints allow you to "hang" sub-applications at various URL prefixes.
This can make it easier to divide work into sub-projects.

This is simple example including the tests.


## Directory layout

Probably other layouts can work an might be even better, for better separation, but this is a working version.

```
.
├── app.py
├── echo
│   └── templates
│       └── echo
│           └── main.html
├── echo.py
├── templates
│   └── main.html
├── test_app.py
└── test_echo.py
```


## The blueprint

{% include file="examples/flask/blueprint/echo.py" %}

## The template of the blueprint

{% include file="examples/flask/blueprint/echo/templates/echo/main.html" %}

## The test of the blueprint

We create an application in it, hang the bluprint in the root of the application and test it there.

{% include file="examples/flask/blueprint/test_echo.py" %}


## The application

It has a single route of its own and uses the blueprint. It could add more bluprints, if there were more.

{% include file="examples/flask/blueprint/app.py" %}


## The template of the main application

{% include file="examples/flask/blueprint/templates/main.html" %}

## Test the application

In this test we also tested the routes of the blueprint. This is probably not necessary as we already tested them earlier,
but these tests can ensure that the routes work properly even when they are attached to a path different from the root.

{% include file="examples/flask/blueprint/test_app.py" %}


