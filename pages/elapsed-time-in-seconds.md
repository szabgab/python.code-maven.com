---
title: Elapsed time in seconds in Python
timestamp: 2024-06-21T10:30:01
author: szabgab
published: true
description:
tags:
    - time
---

If you'd like to measure and display the elapsed time during some operation in Python, probably the easiest way is to create a timestamp before
and after the operation using `time.time()` and compute the difference.

In the following code the `do_something` is just some arbitrary function that takes slightly more than 1 seconds to run on my computer.

{% include file="examples/elapsed_time_in_seconds.py" %}

The result looks like this:

```
1.429948091506958
1
```

## Handle big numbers

If the elapsed time is small then you'd be probably interested in a few digits after the decimal point, but if the elapsed time is long, lik 100 or 1000 seconds
then you'd probably want a more [Human readable format of the elapsed time](/elapsed-time-in-human-readable-form)

