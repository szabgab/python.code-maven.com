---
title: "Flask counter with SQLite, SQLAlchemy, pytest"
timestamp: 2021-05-13T14:30:01
tags:
  - Flask
  - SQLite
  - SQLAlchemy
  - pytest
published: true
books:
  - flask
author: szabgab
archive: true
show_related: true
---


This is a [counter example](/counter) to show how to create a web application using [Python](/python)  [Flask](/flask)
with [SQLite database](https://www.sqlite.org/). Using [SQLAlchemy](https://www.sqlalchemy.org/) as the ORM and ensuring that we
can test the whole application using [pytest](https://pytest.org/). Making sure that each test-case has its own database.


## Directory layout

```
.
├── app.py
├── model.py
├── templates
│   └── counter.html
└── test_app.py
```

To run the application execute the following:

```
FLASK_APP=app FLASK_DEBUG=1 flask run
```

## The application

{% include file="examples/flask/sqlite-counter/app.py" %}

## The model - the SQLAlchemy configuration

{% include file="examples/flask/sqlite-counter/model.py" %}

## The HTML template using Jinja

{% include file="examples/flask/sqlite-counter/templates/counter.html" %}

## The tests

The second test function was added primarily to show that the test functions have their own separate databases.
and there is no interence between the test functions.

{% include file="examples/flask/sqlite-counter/test_app.py" %}

You can run the tests by

```
pytest
```

