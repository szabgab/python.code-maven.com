---
title: "Super-global variables in Python exploiting the builtins package"
timestamp: 2021-08-30T20:30:01
tags:
  - Python
  - builtins
published: true
books:
  - python
author: szabgab
archive: true
show_related: true
---


I just saw a lovely idea in Python to create super-global variables.

That is variable that will be available somehow globally in all the packages.


It was done by creating attributes on the [builtins](https://docs.python.org/library/builtins.html) module Like this:

{% include file="examples/python/super_global.py" %}

Then you can use them like this:

{% include file="examples/python/use_super_global.py" %}

This is a very bad idea. It makes the code very hard to maintain.

In many cases you might be better off using a module or caching for solving whatever issues you encounter.

