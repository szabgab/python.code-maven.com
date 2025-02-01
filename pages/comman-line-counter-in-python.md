---
title: "Command-line counter in Python"
timestamp: 2017-08-21T10:30:01
tags:
  - os.path.exists
  - open
  - with
  - read
  - write
published: true
books:
  - python
author: szabgab
archive: true
---


Part of the big [counter example](/counter) project, let's see the
simple command line counter for a single number implemented in Python.


{% include file="examples/python/counter.py" %}

The `os.path.exists` method checks if a file exists.

Normally in Python if we `open` a file it does <b>not</b>
get closed automatically. If we forget to call `close` all
kinds of bad things can happen.

In order to force the call of close it is recommended to wrap any file operation
in a `with` statement. The `with` statement arranges the `close`
method to be called on the filehandle when the execution leaves the code inside the `with`
statement.

`open` defaults to read-only.

The `read` method reads in the whole content of the file which in our case is just a number.

By default everything we read from a file is considered as a string. We can use the `int` function to convert the value to Integer.

In Python there is no `++` so we use the `+= 1` construct to increment the number by one.

In order to save the new counter in the file, first we need to open the file for writing using `open(filename, 'w')` and then we can use the `write` method to actually write out the data. It expects a string so we need to convert our Integer to String using the `str` function.

No need to explicitly close the file as leaving the `with` statement will automatically call the `close` method.

