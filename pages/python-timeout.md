---
title: "Python timeout on a function call or any code-snippet."
timestamp: 2019-09-17T15:30:01
tags:
  - signal
  - Exception
published: true
books:
  - python
author: szabgab
archive: true
---


There are cases when you'd like to let some code run, but if it takes too much time you'd like to stop it.
Usually libraries of network operatons (eg. http requests) have a built-in mechanisem to set the timeout,
but sometimes you'd like to create your own timeout in Python.


This basically works exactly as your alarm-clock works. You set some time in advance, then you can do whatever you want
without thinking about the time and when you reach the preset time, the clock buzzes with an annoying sound.

You then stop whatever you did and attend to do whatever you planned to do when you set the clock.

For example you'd like to go to sleep but need to get up at 3 am to go to the airport.
You would set your alarm clock to 3 am and go to slow.
Moreover you know yourself and thus you know that when you wake up at 3 am you will be so sleepy that you won't be able
to remember what are the things you need to do before you leave the house. So next to the alarm clock you put a piece of
paper with instructions on it.

An one more thing: If you happen to wake up earlier, you will probably want to turn of the alarm clock yourself as you
won't want to hear its annoying sound.

The next example basically works the same.

{% include file="examples/python/timeout.py" %}

The Operating system has a mechanism of sending signals to processes. One of these signals is called the <b>Alarm signal</b> or <b>ALRM</b>.

The command `signal.alarm(8)` tells the operating system to send an ALRM signal to your process 8 seconds later.

The call `signal.signal(signal.SIGALRM, alarm_handler)` tells Python to stop whatever it is currently doing and
execude the `alarm_handle` function that we implemented earlier. If the alarm_handle does not raise any exception
then Python will resume its original execution. In order to break out that potentially infinite loop we raise an
exception.
This can be any exception, but for cleaner code I've crated our own `TimeOutException`.
In order to handle this exception properly we wrap our function (or code-snippet that needs the time-limiting) in a
try-except block.

After we leave this block we have to remember to turn of our alarm clock by setting it to 0:
`signal.alarm(0)`. It is important to turn of your real-world alarm clock, but here it is even more important.
If you don't do it and if the original loop ends before the time was up then later, when the total time has passed,
we will receive an ALRM signal and because we are not in the try-except block any more our application will die.

Feel free to play around with the values and observe what happens.

## Windows

`alarm` only works on Unix systems (Linux, OSX). It does NOT work on Windows.

For more details you can check the documenation of [signal](https://docs.python.org/library/signal.html).

