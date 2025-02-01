---
title: "Parallel processing in Python using fork"
timestamp: 2017-08-09T08:30:01
tags:
  - fork
  - waitpid
published: true
books:
  - python
author: szabgab
archive: true
---


There are several ways to allow a Python application to do a number of things in parallel.
Probably the easiest is by creating child processes using `fork`.


[fork](https://docs.python.org/2/library/os.html#os.fork) 
(and [fork](https://docs.python.org/3/library/os.html#os.fork))
is part of the <b>os</b> standard Python library.  

{% include file="examples/python/one_fork.py" %}

When we call `os.fork` the operating system creates an exact clone of our process,
everything, including all the values we have assigned to variables get duplicated.
If the `fork` is successful then from that point there will be two process that are almost exactly the same.

The difference is in what `os.fork` returns in each one of them and how the operating system sees the two processes.
In Linux each process has a unique process ID. When we fork we get two processes.
One, that keeps the original process ID, is called the "parent process", the other one that gets a brand new process ID is referred to as the "child process".

In both processes the call to `os.fork()` returns, but in the "parent process" it returns the process ID of the newly created "child process",
while in the "child process" it returns 0.

That's why in our code we check `if pid == 0` that will be `True` if `pid` is 0  which means we are in the "child process".
This is how we can tell the "child process" and the "parent process" apart and this is how we can tell them to do different things.

Inside the `if`-statement we have the code of the "child process". It ends with a call to `exit` which is a rather important aspect of this code example.
If we did not have that call to `exit` then after finishing its own job the "child process" would proceed to execute the
code that is relevant to the parent only. This almost always leads to confusion and to hours of debugging.

Better to remember to always call `exit()` at the end of the `if` block or to have two distinct code path, one for the child part
and one for the parent part.

In the unlikely event that fork is not successful (e.g. because the operating system is so overloaded that it cannot create another process),
then Python will raise an [OSError](https://docs.python.org/2/library/exceptions.html#exceptions.OSError) exception.
That's what we `try` to catch in our code.

If we run the above example we git output that looks like this:

```
$ python one_fork.py

Process id before forking: 55862
In the child process that has the PID 55863
In the parent process after forking the child 55863
(55863, 0)
```

The number printed will differ in every run as your operating system creates new processes.
The order of the 2nd and 3rd line might be swapped as those parts run in parallel. (See below.)

The call to `os.waitpid(0, 0)` in the parent process will wait till the child process ends and then
it will return a tuple containing the process ID (PID) of the child process and the exit code, the value
we passed to `exit()` in the child process which defaults to 0.

## What does parallel mean here?

When we `fork` we create a second, almost identical process to the one already running.
The Operating system is free to schedule the two process as it wishes.

If you have a single CPU with a single core, something that was very common in the ancient times of the early 2000s,
then the operating system will swap between the two processes frequently and in a rather unpredictable
(to the regular programmer) way. That means they might seem to run in parallel even though they don't.
That also means the order of the 2nd and 3rd printed line in our examples can be in either way.

If you computer has multiple cores which is quite common in every computer, then the Operating System
might put these two processes on different cores and thus they can really work in parallel.
They still can only print one after the other, but now, if they had a lot of computation to do, they could
really do it in a shorter period of time.


## Many child processes

Forking once child process might be already useful, but in many cases we would want to fork many child processes
to work in parallel. In this example we see just that:

{% include file="examples/python/many_forks.py" %}

We created a variable called `forks` that has a default value of 3, but that you can change through
a command line parameter.

We have two `while` loops. In the first one we spawn the child-processes, in the second one
we wait for them to finish.

```
$ python many_forks.py

Process id before forking: 55992
In the parent process after forking the child 55993
In the parent process after forking the child 55994
In the parent process after forking the child 55995
In the parent process after forking 3 children
In the child process 1 that has the PID 55993
In the child process 2 that has the PID 55994
In the child process 3 that has the PID 55995
(55994, 0)
(55995, 0)
(55993, 0)
```


## Why to call waitpid?

You might ask why do we need to call `waitpid` and wait for the child-processes to finish.

We don't really have to, but it is a recommended good practice (or shall we say <b>best practice</b> ?)
to clean up after yourself. Otherwise you'd get parent-less dead child processes, which are also called
zombies. You usually prefer to avoid that.




## Comments

I don't want my parent process to wait for anything. I just want the child processes to die in a clean manner once they finish their task. How should I do this?

<hr>

How can i make a system call on that child process??

<hr>

i am using python 3.7 ,I cant able to use os.fork() function even i imported os module
its showing error 'module os has no attribute fork
---
Are you running this on Windows?

---
yes, i am running this on windows.

---
fork is not supported on windows. Try multiprocess: https://slides.code-maven.com/python/multiprocess-pool

---
can you help me which function help me to create a new child process in this multiprocessing module ,will it work same as fork function


