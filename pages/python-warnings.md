---
title: "Python: capturing, hiding, and reporting warnings"
timestamp: 2020-06-27T09:40:01
tags:
  - CodeMaven
published: true
books:
  - python
author: szabgab
archive: true
show_related: true
---


I am sure you have already seen [warnings](https://docs.python.org/library/warnings.html) coming from some Python code.
I espcially encountered warnings about using deprecated features.

This always raises threww questions:

How can I hide the warnings?

How can I capture, collect, and report the warnings?

How can you create my own warnings?


## Generate warnings

{% include file="examples/python/warn.py" %}

```
before
warn.py:4: UserWarning: Some warning
  warnings.warn("Some warning")
after
```

## Capture and hide or print warnings

{% include file="examples/python/warn_capture.py" %}

```
before
-----
warn: Some warning
<class 'UserWarning'>
{message : UserWarning('Some warning'), category : 'UserWarning', filename : 'warn_capture.py', lineno : 4, line : None}
-----
warn: Other warning
<class 'UserWarning'>
{message : UserWarning('Other warning'), category : 'UserWarning', filename : 'warn_capture.py', lineno : 5, line : None}
-----
after
```

## Log the warnings

{% include file="examples/python/warn_to_logger.py" %}

```
2020-06-27 09:41:37,847 - INFO       - before
2020-06-27 09:41:37,848 - WARNING    - warn_to_logger.py:5: UserWarning: Some warning
  warnings.warn("Some warning")

2020-06-27 09:41:37,848 - INFO       - after
```

