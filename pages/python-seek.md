---
title: "Python: seek - move around in a file and tell the current location"
timestamp: 2018-11-17T14:30:01
tags:
  - seek
  - tell
  - readline
  - read
published: true
books:
  - python
author: szabgab
archive: true
---


When we open a file for reading with Python (thought this is true for any programming lanuage),
we get a filehandle that points to the beginning of the file. As we read from the file
the pointer always points to the place where we ended the reading and the next read will
start from there.

That is, unless we tell the filehandle to move around.

The `tell` method of the filehandle will return the current location of this pointer.

The `seek` method will move the pointer.


In this example first we create a file and then open it and fool around with `tell` and `seek`
for no particular reason just to show how they work.

{% include file="examples/python/seek.py" %}

`seek` gets two parameters. The first says how many bytes to move (+ or -)
the second parameter tells it where to start from. In some cases the former is called `offset`
and the latter is called `whence`.

The `whence` can be any of the following values:

* os.SEEK_SET - beginning of the file
* os.SEEK_CUR - current position
* os.SEEK_END - end of file

A positive offset will move the pointer forward, a negative offset would move backward.


## Special cases

There are two special cases:

```
fh.seek(0, os.SEEK_SET)  - go to the beginning of the file.
```

```
fh.seek(0, os.SEEK_END)  - go to the end of the file.
```
