---
title: Elapsed time in human readable format in Python
timestamp: 2024-06-21T10:30:02
author: szabgab
published: true
description: datetime can help us handle time differences and thus also elapsed time
tags:
    - datetime
    - timedelta
---

It is rather easy to get the [elapsed time in seconds or miliseconds](/elapsed-time-in-seconds), but if the we are
trying to measure a very long running process we will probably want to see the elapsed time in a more human readable
format using minutes and even hours. We can convert seconds into such format using the `datetime.timedelta` function.

{% include file="examples/elapsed_time_in_human_readable_form.py" %}

```
0:00:01.429948
0:00:01
0:00:05
0:01:01
0:01:40
0:16:40
2:46:40
```


