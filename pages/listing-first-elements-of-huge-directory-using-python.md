---
title: "Listing first elements of a huge directory using Python"
timestamp: 2023-01-17T11:40:01
tags:
  - walk
  - pathlib
  - iterdir
published: true
books:
  - python
author: szabgab
archive: true
show_related: true
---


At a client we have a huge directory of files. I wanted to list the first few files. <b>ls -l | head</b> took ages as it first lists all the files and only then cuts it down.
After my first attempts in Python failed I wrote a [Perl one-liner to list the first elements of a huge directory](https://perlmaven.com/oneliner-read-huge-directory). However I wanted to see if I can do it with Python in some other way.


## using iterdir of pathlib

The original attempt in Python was using the [iterdir](https://docs.python.org/3/library/pathlib.html#pathlib.Path.iterdir) method of [pathlib](https://docs.python.org/3/library/pathlib.html).

{% include file="examples/python/list_dir_using_iterdir.py" %}

On the real data it took 47 minutes to run.

## using walk of os

The second attempt was to use the [walk](https://docs.python.org/3/library/os.html#os.walk) method of [os](https://docs.python.org/3/library/os.html#os.walk).

{% include file="examples/python/list_dir_using_walk.py" %}

I don't know how long this would take. I stopped it after a minute.

## using scandir of os

Finally I found the [scandir](https://docs.python.org/3/library/os.html#os.scandir) method of [os](https://docs.python.org/3/library/os.html#os.walk). That did the trick:

{% include file="examples/python/list_dir_using_scandir.py" %}

## using scandir and a range

After getting an improvement suggestion for my solution in Perl I thought I can use the same idea here too. I assume that there are at least 3 element in this folder or I'll get a <b>StopIteration</b> exception calling <b>__next__</b>, but besides that this works.

{% include file="examples/python/list_dir_using_scandir_range.py" %}
