---
title: "Time left in process (progress bar) in Python"
timestamp: 2018-08-22T07:30:01
tags:
  - datetime
published: true
books:
  - python
author: szabgab
archive: true
---


In a project some Python code was used to monitor the progress of another process.
Besides reporting the progress basd on the number of units processed so far, I wanted
to be able to show how much time is left in the process.


We knew how many items (units) are there to process, every once in a while we could check how many have been alread processed (by looking up in a database).

The same can be used even if the processing is done in the same program where we have the monitoring.We just need to calculate how much time - on average - took to process one unit (dividing the elapsed time by the number of units done) and then multiplying it by the number of units remaining.

It won't be exact, but can give you a better feeling to see how much more you have to wait.

{% include file="examples/python/time_left.py" %}

