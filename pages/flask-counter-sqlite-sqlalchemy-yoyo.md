---
title: "Flask counter with SQLite, SQLAlchemy, pytest - database migration with yoyo"
timestamp: 2021-05-13T16:30:01
tags:
  - Flask
  - SQLite
  - SQLAlchemy
  - pytest
  - yoyo
published: true
books:
  - flask
author: szabgab
archive: true
show_related: true
---


This is another [counter example](/counter) using Flask, SQLite, SQLAlchemy, pytest, but this time we are also usiong [youo migration](https://ollycope.com/software/yoyo/latest/)
to maintain the database. An [earlier version](/flask-counter-sqlite-sqlalchemy) of this example did not use Yoyo and there we created the schema using SQLAlhemy.



## Directory layout

```
.
├── app.py
├── migrations
│   ├── 001.rollback.sql
│   └── 001.sql
├── model.py
├── templates
│   └── counter.html
└── test_app.py
```

## The application code

{% include file="examples/flask/sqlite-counter-yoyo/app.py" %}

The way we run queries changed. We now need to call <b>db.session.query</b> and pass it
the class representing the table.

## The SQL migration scripts

{% include file="examples/flask/sqlite-counter-yoyo/migrations/001.sql" %}
{% include file="examples/flask/sqlite-counter-yoyo/migrations/001.rollback.sql" %}

## The SQLAlchemy code

{% include file="examples/flask/sqlite-counter-yoyo/model.py" %}

There are two ways to use SQLAlchemy. Either we declare the details of the schema in Python statements as we did in the
[other version](/flask-counter-sqlite-sqlalchemy) or we use the [automap](https://docs.sqlalchemy.org/en/14/orm/extensions/automap.html) feature
of SQLAlchemy.

As we already have our SQL declarations in the migration files I thought it would be better to try to use the <b>automap_base</b>.

## The Jinja template

{% include file="examples/flask/sqlite-counter-yoyo/templates/counter.html" %}

## The tests

{% include file="examples/flask/sqlite-counter-yoyo/test_app.py" %}

