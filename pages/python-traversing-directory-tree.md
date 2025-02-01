---
title: "Traversing directory tree using walk in Python - skipping .git directory"
timestamp: 2020-03-12T07:30:01
tags:
  - os
  - walk
published: true
books:
  - python
author: szabgab
archive: true
---


The [os](https://docs.python.org/library/os.html) module of Python provides a function called <b>walk</b>
that makes it easy to go over all the directories and files in a directory tree.

It is also quite easy to skip some of the subtrees.


Here you can see an example how to go over a directory tree.

Changing the content of <b>dir</b> variable allows us to skip some of the subdirectories.

In the first example we only skip the <b>.git</b> directory, in the next example that is currently committed
out, we have a more complex filter that will make it skip a number of different subdirectories.

{% include file="examples/python/tree.py" %}

