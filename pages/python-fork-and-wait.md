---
title: "Python fork and wait or waitpid"
timestamp: 2021-04-29T08:30:01
tags:
  - fork
  - wait
  - waitpid
  - WNOHANG
published: true
books:
  - python
author: szabgab
archive: true
show_related: true
---


A low-level way to do things in parallel in Pythin is to use <b>fork</b>.


In this code we create 3 child-processes. Each process will generate a random number for the number of seconds it will wait
(to imitate processes that take some time). They will also generate a random number to be the exit code when they are done.

After creating the child processes and storing their PID in the processes list, the parent process will wait for each child process to terminate.

{% include file="examples/python/fork_and_wait.py" %}

In the first run we used the line <b>pid, exit_code = os.wait()</b>. This line will wait (and block the main process) till any of the child processes terminate.

```
$ python fork_and_wait.py

In child 96512 waiting for 3 and then exiting with 2
In child 96513 waiting for 5 and then exiting with 2
In child 96514 waiting for 5 and then exiting with 0
96512 2
96514 0
96513 2
```

In the second case we used the line <b>pid, exit_code = os.waitpid(-1, os.WNOHANG)</b>. This is a non-blocking wait. That it this command will return
immediately regardless of the the child processes. If there was a child process that already terminated then this will return the PID of that chile process.
If no child process has terminated yet then it will return 0. This will give us the opportunity to do something else in the main process.

```
$ python fork_and_wait.py

do something else or just wait 1 sec
In child 96517 waiting for 4 and then exiting with 0
In child 96518 waiting for 5 and then exiting with 0
In child 96519 waiting for 2 and then exiting with 1
do something else or just wait 1 sec
do something else or just wait 1 sec
96519 1
do something else or just wait 1 sec
do something else or just wait 1 sec
96517 0
do something else or just wait 1 sec
96518 0
```

## Exit code

The exit_code that was returned by either <b>wait</b> or <b>waitpid</b> is the same number that was passed to <b>exit()</b> in the child process, but it is in the "high-byte"
so we need to divide it by 256 in order to get the real number.

