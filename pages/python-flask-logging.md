---
title: "Python Flask: logging"
timestamp: 2020-06-26T15:30:01
tags:
  - Flask
  - logger
  - logging
  - before_first_request
published: true
books:
  - flask
author: szabgab
archive: true
show_related: true
---


Python Flask provides a built-in connection to the standard [logging](https://docs.python.org/library/logging.html) facility of Python.


## Quick solution

```
app.logger.setLevel(logging.INFO)
app.logger.info("some text")
```

## Example

{% include file="examples/flask/logging/app.py" %}

Run as:

```
FLASK_APP=app FLASK_DEBUG=1 flask run
```

Output on the console as <b>FLASK_DEBUG</b> was set to be true:

```
[2020-06-26 15:55:22,930] DEBUG in app: main debug
[2020-06-26 15:55:22,930] INFO in app: main info
[2020-06-26 15:55:22,930] WARNING in app: main warning
[2020-06-26 15:55:22,930] ERROR in app: main error
[2020-06-26 15:55:22,930] CRITICAL in app: main critical
```

If you run as

```
FLASK_APP=app FLASK_DEBUG=0 flask run
```

So we set <b>FLASK_DEBUG</b> was set to be false, which is actually also the default, we only get warning and higher level logging messages:

```
[2020-06-26 15:56:48,387] WARNING in app: main warning
[2020-06-26 15:56:48,388] ERROR in app: main error
[2020-06-26 15:56:48,388] CRITICAL in app: main critical
```

So if you would like to have detailed logging, you need to enable the FLASK_DEBUG mode, but that's not a good idea to do on your production
server because then Flask will spew a whol stack-trace on the screen of an unfortunate visitor who stumbles uppon an exception.

A much better way is to control the log-level by yourself.

## Setting the level of logging in Flask

You can easily do that by calling the `app.logger.setLevel(logging.INFO)` method.
The <a href="/python-flask-before-first-request"><b>before_first_request</b></a> hooks seems like a perfect place to do this.
You just need to make sure the <b>logging</b> module is loaded.

{% include file="examples/flask/logging-set-level/app.py" %}

If we run it like this (with the debugging turned off)

```
FLASK_APP=app flask run
```

The result on the console will be

```
[2020-06-26 16:00:36,292] INFO in app: main info
[2020-06-26 16:00:36,292] WARNING in app: main warning
[2020-06-26 16:00:36,293] ERROR in app: main error
[2020-06-26 16:00:36,293] CRITICAL in app: main critical
```

Of course you can set any log level this way and you can use any configuration option to set it.

## Logging to file

If you prefer to have the logs go to a specific file, you can do that too.

Here first we remove all the existing logging handlers. (You only do this if you don't want the console logging any more.)

Then we create a directory in called "logs" in the root of the project and finally we create a logging handler to log to a file.

{% include file="examples/flask/logging-to-file/app.py" %}

