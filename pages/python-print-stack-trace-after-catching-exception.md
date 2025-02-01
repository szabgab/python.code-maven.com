---
title: "Python: print stack trace after catching exception"
timestamp: 2019-07-09T20:30:01
tags:
  - traceback
  - Exception
published: true
books:
  - python
author: szabgab
archive: true
---


{% include file="examples/python/stack_trace.py" %}


The upper stack-trace was printed by the `traceback` module. The lower one would
be if we did not catch it.

```
$ python examples/python/stack_trace.py
Traceback (most recent call last):
  File "examples/python/stack_trace.py", line 11, in <module>
    g()
  File "examples/python/stack_trace.py", line 4, in g
    f()
  File "examples/python/stack_trace.py", line 7, in f
    raise Exception("hi")
Exception: hi

---------------------
Traceback (most recent call last):
  File "examples/python/stack_trace.py", line 19, in <module>
    g()
  File "examples/python/stack_trace.py", line 4, in g
    f()
  File "examples/python/stack_trace.py", line 7, in f
    raise Exception("hi")
Exception: hi
```



