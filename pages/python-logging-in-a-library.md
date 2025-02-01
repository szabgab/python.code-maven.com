---
title: "Python: logging in a library even before enabling logging"
timestamp: 2019-07-09T20:44:01
tags:
  - logging
  - basicConfig
published: true
books:
  - python
author: szabgab
archive: true
---




You can add logging code to a library like in this excample:

{% include file="examples/python/loglib/lib.py" %}

and it will not bother the person who uses the library without enabling any logging like this code:

{% include file="examples/python/loglib/use_without.py" %}

The output will look like this:

```
$ python examples/python/loglib/use_without.py
before
after
```


If the user enabled logging, then that logging will be also included.

{% include file="examples/python/loglib/use_with.py" %}

```perl
$ python examples/python/loglib/use_with.py
before
DEBUG:root:hello
after
```




