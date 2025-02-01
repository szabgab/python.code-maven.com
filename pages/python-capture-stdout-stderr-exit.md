---
title: "Python: Capture standard output, standard error, and the exit code of a subprocess"
timestamp: 2018-11-17T14:40:01
tags:
  - subprocess
  - stderr
  - stdout
  - exit
  - returncode
  - PYTHONUNBUFFERED
  - tee
published: true
books:
  - python
author: szabgab
archive: true
---


I might be missing the obvious, but I don't think the `subprocess` module has a method
that will capture the standard output, standard error, and the exit code of a subprocess in a single
call. It is not complex to write one and can be useful.


## The code that captures theresults

{% include file="examples/python/capture.py" %}


## A sample external program

{% include file="examples/python/run.py" %}

## Running the external program directly

```
$ python examples/python/run.py

STDOUT: Hello World!
STDERR: Welcome to the dark side!
STDOUT: Second line
STDERR: Warning
```

```
echo $?
42
```

## The results

```
out: 'STDOUT: Hello World!
STDOUT: Second line
'
err: 'STDERR: Welcome to the dark side!
STDERR: Warning
'
exit: 42
```

As you can see in this case the standard output and standard error are separated. You can't tell the exact order.

## Capture STDOUT and STDERR together

Sometimes it is better to be able to capture the two together:

{% include file="examples/python/capture_together.py" %}

Here we had `stderr = subprocess.STDOUT` instead of
`stderr = subprocess.PIPE`.

```
out: 'STDOUT: Hello World!
STDERR: Welcome to the dark side!
STDOUT: Second line
STDERR: Warning
'
err: 'None'
exit: 42
```

In order for this to work properly on a Python script we'll need to turn off output buffering
for the child process.
This can be done by setting the `PYTHONUNBUFFERED` environment variable.

## Tee: Capture and also print

Finally in this example we both collect the out and at the same time keep printing to the screen.
Just to show off we captur STDOUT and STDERR both individually and mixed together.

You'll probably use some subset of these features.

{% include file="examples/python/capture_tee.py" %}

```
python examples/python/capture_tee.py 
```

```
STDOUT: Hello World!
STDERR: Welcome to the dark side!
STDOUT: Second line
STDERR: Warning
out: '['STDOUT: Hello World!\n', 'STDOUT: Second line\n']'
err: '['STDERR: Welcome to the dark side!\n', 'STDERR: Warning\n']'
err: '['STDOUT: Hello World!\n', 'STDERR: Welcome to the dark side!\n', 'STDOUT: Second line\n', 'STDERR: Warning\n']'
exit: 42
```

