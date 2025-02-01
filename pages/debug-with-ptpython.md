---
title: "Debug and Explore Python with PT Python"
timestamp: 2021-06-21T17:30:01
tags:
  - ptpython
types:
  - screencast
published: true
books:
  - python
author: szabgab
archive: true
show_related: true
---


Python has several interactive shells (aka. REPLs) that you can use to explore Python directly and you can also
tell python that a certain point in your application it will enter the REPL and allow you to discover
things from that point.

[ptpython](https://github.com/prompt-toolkit/ptpython) is such a REPL.



```
pip install ptpython
```

Then I used the following code:

{% include file="examples/debug_with_ptpython.py" %}

<img src="/img/debug-with-ptpython.gif" alt="Debug with PTPython" />


