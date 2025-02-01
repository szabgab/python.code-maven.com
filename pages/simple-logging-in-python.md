---
title: "Simple logging in Python"
timestamp: 2018-06-12T08:30:01
tags:
  - logging
  - time
  - strftime
published: true
books:
  - python
author: szabgab
archive: true
---


Python provides a built-in library called [logging](https://docs.python.org/3/library/logging.html) to make it easy to add logging to any module or application in a unified way. Let's see how can we use it.


## Simple logging

The most simple way to get started with logging is to import the `logging` module and then call
the various logging methods on it. There are 5 primary [levels of logging](https://docs.python.org/3/library/logging.html#levels). Each one has a corresponding numeric value and a method to log on that level.

In addition we can call the `log` method passing to it the level as provided by the appropriate name in upper case (`logging.WARNING` in our example) or we can even pass the numerical value by ourself, though that makes of a much less readable code.

{% include file="examples/python/simple_logging.py" %}

If we run the above script we get the following output:

```
WARNING:root:warning
ERROR:root:error
CRITICAL:root:critical
WARNING:root:another warning
ERROR:root:another error
```

* By default the `logging` module only displays the levels WARNING and up.
* By default it prints then to the Standard Error channel (STDERR).
* The format is LEVEL followed by the name of the default logger (root), followed by the message

## Basic Configuration: Set the log level for logging in Python

We can easily adjust the level of logging to be INFO and above by calling the `basicConfig` method:

{% include file="examples/python/simple_logging_set_level.py" %}

The output will be:

```
INFO:root:info
WARNING:root:warning
ERROR:root:error
CRITICAL:root:critical
```

## Send log to a file

We can also configure the logging module to save the log messages in a file, <b>instead</b> of the STDERR
by adding the `filename` parameter to the `basicConfig` method call:

```
logging.basicConfig(level = logging.INFO, filename = "my.log")
```

This will create the log file if it does not exists and append the content of the file, if it already existed.


This means the file can grow in size quite fast so a better idea might be to use some kind of a log-file rotation tool
or to create log files for limited time periods. E.g. One file per day. For this we can use the [time.strftime](http://strftime.org/) method:

{% include file="examples/python/simple_logging_to_file.py" %}

This will use files in the following format: `my-2018-06-12.log`. Please don't use British or American date formats here.
Those are really confusing and break the sorting order.

Alternatively you could change it by adding `filemode = 'w'` that will change the mode of operation from "append" to "write"
and will overwrite the file every time we run our application. This usually is not very useful as this mean we lose all the old logs.

## Formatting the log message, including date

We can replace the default log message format using the `format` parameter and some keywords representing the various fields
supplied by the logging module:

{% include file="examples/python/simple_logging_format.py" %}

The output will look like this:

```
2018-06-12 08:46:22,942  WARNING    MainProcess  root warning
2018-06-12 08:46:22,942  ERROR      MainProcess  root error
2018-06-12 08:46:22,942  CRITICAL   MainProcess  root critical
```


## Change the date format in the log

Though I don't really recommend to change the date format, you can do that by passing the `datefmt` parameter
with a string using the [strftime](http://strftime.org/) tags.

{% include file="examples/python/simple_logging_format_date.py" %}

The output will then change to:

```
2018-06-12-08-51-30  WARNING    MainProcess  root warning
2018-06-12-08-51-30  ERROR      MainProcess  root error
2018-06-12-08-51-30  CRITICAL   MainProcess  root critical
```

## Comments

```
logging.basicConfig(level = logging.INFO, filename = "my.log")
```

This statement won't create the log file automatically for you.

<hr>


Have you tried https://simplelogging.readthedocs.io/en/latest/readme.html ?
You don't have to remember the boilerplate anylonger.

<hr>

Log to file doesnt work with this code


