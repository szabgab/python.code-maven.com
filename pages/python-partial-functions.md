---
title: "Python create partial functions in runtime"
timestamp: 2021-09-29T08:30:01
tags:
  - partial
  - exec
  - locals
published: true
books:
  - python
author: szabgab
archive: true
show_related: true
---


The functools package in Python has a function called [partial](https://docs.python.org/library/functools.html#functools.partial) which is similar
to, but not the same as [Currying](https://en.wikipedia.org/wiki/Currying).

It helps us create a new function where some of the original arguments have fixed values.


It can be done manually:

{% include file="examples/python/generate_partials.py" %}

but sometimes you'd like to do that on-the fly with a number of different values of the same parameter.

It can be done using <b>exec</b>:

{% include file="examples/python/generate_partials_on_the_fly_with_exec.py" %}

but there is a better way to do it using <b>locals</b>.

manually:

{% include file="examples/python/generate_partials_using_locals.py" %}

on-the fly to many values:

{% include file="examples/python/generate_partials_on_the_fly_with_locals.py" %}


