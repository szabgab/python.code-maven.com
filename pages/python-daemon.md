---
title: "Python daemon (background service)"
timestamp: 2019-06-25T07:40:01
tags:
  - daemon
published: true
books:
  - python
author: szabgab
archive: true
---


Using the [python-damon](https://pypi.org/project/python-daemon/) module:

{% include file="examples/python/mydaemon.py" %}


## Install the module

```
pip install python-daemon
```

## Launch the damon in the background

```
python mydaemon.py
```

## Check that it is working

```
tail -f /tmp/echo.txt
```


## Find the process id

```
$ ps axuw | grep mydaemon
gabor     7686  1.7  0.0  32692 15860 ?        S    06:50   0:00 python examples/python/mydaemon.py
gabor     7692  0.0  0.0  14352   920 pts/1    S+   06:50   0:00 grep --color=auto mydaemon
```

## Stop the process

Use the process ID to stop the service:

```
kill 7686
```

