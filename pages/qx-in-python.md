---
title: "qx or backticks in python - capture the output of external programs"
timestamp: 2019-05-17T10:00:01
tags:
  - qx
  - qxx
  - subprocess
  - check_output
published: true
books:
  - python
author: szabgab
archive: true
---


In the Unix/Linux shell you can use backticks to capture the output of an external command.
[In Perl you can use both backticks and the qx operator](https://perlmaven.com/qx).

In Python it requires a bit more code, but it is easy to wrap it in a function.


Basically this is it:

{% include file="examples/python/qx.py" %}


## External code

In order to show how it works I've created a program (that happens to be in Python, but could be in any language)
that prints to both STDOUT and STDERR:

{% include file="examples/python/external.py" %}

If we run it we see the following on the screen:

{% include file="examples/python/external.txt" %}

## Capture using qx

{% include file="examples/python/capture_stdout.py" %}

This will capture everything printed to STDOUT by the external code and assign it to the "out" variable.

Whatever printed to STDERR will be let through to STDERR.

This is the output:

{% include file="examples/python/capture_stdout.txt" %}

This is a blocking operation so your Python code will wait till the external program finishes to run.


## qxx - capture both stdout and stderr

{% include file="examples/python/qxx.py" %}

## See also

{% include file="examples/python/capture.py" %}

[capture STDOUT, STDERR, and exit in python](/python-capture-stdout-stderr-exit).


