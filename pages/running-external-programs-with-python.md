---
title: "Running external programs with Python (system and subprocess)"
timestamp: 2022-12-08T12:30:01
tags:
  - GitHub
published: true
books:
  - github
author: szabgab
archive: true
show_related: true
---


One of the things we often have to do is glue together various programs written by other people.
If these other programs are GUI based then we will have a very hard time doing so, but if they are command line based then
there are some nice ways to do that in Python. We'll see two different ways to accomplish this.


## Our external program

In order to demonstrate this we need an "external tool" that we will handle as a "black box". As you are using Python I can
assume you already have Python on your computer so we'll use a script written in Python as the "external tool".

You can see it here:

{% include file="examples/python/process/process.py" %}

The idea is to have a program that can demonstrate a process with

* Output on Standard Output (STDOUT)
* Output on Standard Error (STDERR)
* A process that takes time
* Various exit codes (ERRORLEVELs)

So we can see how to deal with either of those.

The user of the <b>process.py</b> can tell it how many iterations to do. On every iteration it will print to both STDOUT and STDERR and wait for 1 second.
The user can also tell the process how to set its exit code.

This can be a nice tool to fake the behavior of some external tool.

If we run the process as follows:

```
$ python process.py 3 4
```

We get the following output:

```
OUT 0
ERR 0
OUT 1
ERR 1
OUT 2
ERR 2
```

We can also observe the exit code on Linux/macOS:

```
$ echo $?
4
```

and on Windows:

```
> echo %ERRORLEVEL%
4
```

## Using os.system

The simplest way to run an external program is to use <b>os.system</b>.

{% include file="examples/python/process/os_system.py" %}

It accepts a string - exactly what you would type in on the command line and executes the external program.

Your program connects its own STDOUT and STDERR channels to the external process so while the external program is running
whatever it prints to STDOUT and STDERR will be handled exactly as if they came directly from your program.

It waits till the external program ends and at the end it returns the exit-code of the external program.
Well it actually returns two bytes and the real exit code is the higher byte so we need to do an integer division
<b>exit_code // 256</b> in order to get to the real value. (It is the same as <b>int(exit_code / 256)</b>.)

```
$ python os_system.py
```

```
OUT 0
ERR 0
OUT 1
ERR 1
OUT 2
ERR 2
OUT 3
ERR 3
OUT 4
ERR 4
exit code: 2
```

This can be very useful, but this way the output of the external program "gets lost" to our program. Often this is not what we want.

Often we would want to capture the output of the external program, parse it and do something based on the understanding from it.

We might also want to do something else while the external program does its thing.

Let's see how the <b>subprocess</b> module can help us. We will see a few examples.


## subprocess waiting for external process to finish

In the first example we will imitate the <b>os.system</b> just to lay the ground-work.

We have created a function called <b>run_process</b>. Instead of a string, the command we would want to type in,
it is expected to receive a list. The pieces of the command divided up. That is probably not be a problem to write.

I sprinkled the whole program with <b>print</b> statements to make it easier to see what is the order of things happening.

The first thing is to call <b>proc = subprocess.Popen(command)</b>. This will start the external program and return immediately
passing us an object that represents this external process. (<b>Popen</b> stands for <b>process open</b>)

At this point the external program will run regardless of what our program does. So we can wait for 1.5 seconds and see the output (and error)
of the external program. We could also do some other work while the external program runs. We'll see that later.

At one point, however, we will likely want to wait for the external program to end. This is what the <b>proc.communicate()</b> does.
(It's name is strange, I know. The next example will shed some light on why it is called that way.)
It stops our program and waits till the external program ends.

Then we can fetch the exit code (that Windows calls ERRORLEVEL) from the attribute <b>returncode</b> of the <b>proc</b> object.

(Are you already having fun by the fact that the same thing is called "exit code", ERRORLEVEL, and "returncode" by three different systems?)

Anyway, here is the code:

{% include file="examples/python/process/run_command.py" %}

Here is how you'd run it:

```
$ python run_command.py
```

Here is the output. As you can see the external program already managed to print out 4 lines while we were sleeping, before we called "communicate".

In this case we still let through STDOUT and STDERR to the respective channels of our script.

```
Before run_process
Before Popen
After Popen
OUT 0
ERR 0
OUT 1
ERR 1
Before communicate
OUT 2
ERR 2
OUT 3
ERR 3
OUT 4
ERR 4
After communicate
After run_process
exit code: 0
```


## subprocess capture both STDOUT and STDERR separately

In the next example we passed <b>stdout = subprocess.PIPE</b> and
<b>stderr = subprocess.PIPE</b> to the <b>subprocess.Popen()</b> call.

These will connect the STDOUT and STDERR channels of the external program
to two separate pipes in our program. Anything the external program prints
will go into these pipelines instead to the screen.

In this example too, we call the <b>communicate</b> method to wait for the external
program to end. Once the external program terminates the <b>communicate</b> method
returns and it returns all the content it collected from the external program as
two separate byte-streams.

Our own <b>run_process</b> function then returns the exit code along with these two.

We can then use these two variables directly or we can convert them to UTF-8 strings by
calling <b>decode('utf8')</b> on each one of them.

{% include file="examples/python/process/run_command_collect_output.py" %}

```
$ python run_command_collect_output.py
```

In the output you can see that we only print the output of the external program
after <b>run_process</b> ended. Of course instead of printing them to the screen
you could parse them using a regular expression or some other tool.

```
Before run_process
Before Popen
After Popen
Before communicate
After communicate
After run_process

exit code: 0

out:
OUT 0
OUT 1
OUT 2
OUT 3
OUT 4

err:
ERR 0
ERR 1
ERR 2
ERR 3
ERR 4
```

## Run external process and capture STDOUT and STDERR merged together

In the next example we combine the STDERR and STDOUT channels.

In the <b>Popen</b> call we pass <b>stdout = subprocess.PIPE</b> as previously, but now
we pass <b>stderr = subprocess.STDOUT</b>. This will tell <b>subprocess</b> to
merge STDERR into STDOUT.

The rest of the code is the same.

{% include file="examples/python/process/run_command_combine_stderr_and_stdout.py" %}

In the output you can see that the two channels are now mixed again as they were in the first case.
However there is no promise that this will be the exact same order as we had earlier. It seems to be now,
but our output was very regular. If they come at some fancy schedule then the the Standard Output
and Standard Error channels might be mixed in a different way.

```
$ python run_command_combine_stderr_and_stdout.py
```

```
Before run_process
Before Popen
After Popen
Before communicate
After communicate
After run_process

exit code: 0

out:
OUT 0
ERR 0
OUT 1
ERR 1
OUT 2
ERR 2
OUT 3
ERR 3
OUT 4
ERR 4

err:
None
```


## Doing things while subprocess is running in the background

There are some more examples showing how to do something else while our external program is running in the background,
but for now I think it is enough.





