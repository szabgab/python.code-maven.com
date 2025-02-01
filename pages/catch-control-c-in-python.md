---
title: "Signal handling: Catch Ctrl-C in Python"
timestamp: 2021-05-06T18:00:01
tags:
  - readchar
  - signal
  - Ctrl-C
description: "Catching the Ctrl-C signal in Python and changing the default behavior of the code."
types:
  - screencast
published: true
books:
  - python
author: szabgab
archive: true
show_related: true
---


Python allows us to set up signal -handlers so when a particular signal arrives to our program we can have a behavior different from the default.

For example when you run a program on the terminal and press Ctrl-C the default behavior is to quit the program.

In this example we override that behavior and instead we ask the user if s/he really want to quit or if we can continue running.


This can be useful in all kinds of situations. For example a long-running process that somehow knows how much more time is needed
can ask the user if s/he really wants to abandon the process at this point or return to processing.

This is how it works:

<img src="/img/counter-ctrl-c-python.gif" alt="Catching Ctrl-c" />


The first thing is to create a function that will be executed when the specific signal arrives.

Then we use the <b>signal.signal</b> call to connect a specific signal to a specific function.

From that point on this is going to be the behavior.

In this example we also use the "magic" of printing carriage return ("\r") only and not new line ("\n") so
we keep counting in the same row. We also tell the print function to <b>flush</b> the output to the screen immediately
and not wait for a newline. Finally we also employ <b>readchar</b> so the python code will be able to react to the pressing
of a single button on the keyboard without the need to press <b>ENTER</b>. (That would move us to another line.)

{% include file="examples/python/ctrl_c.py" %}


## Skeleton

A simplified version of the script, that does not include the fancy "keep it in one line" thing:

{% include file="examples/python/ctrl_c_skeleton.py" %}

This is how it looks like when the numbers are running out of the screen:

<img src="img/counter-ctrl-c-python-skeleton.gif" alt="Catching Ctrl-C" />

