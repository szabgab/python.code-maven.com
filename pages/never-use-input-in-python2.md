---
title: "Never use input() in Python 2"
timestamp: 2017-08-13T12:30:01
tags:
  - input
  - raw_input
published: true
books:
  - python
author: szabgab
archive: true
---

Never use `input()` in Python 2. It is a security hazard!


{% include file="examples/python/use_input.py" %}

Run the script.

Type in `os.system("ls -l")`

Can you feel the danger in that?

Not yet?

What if someone typed in `os.remove(__file__)`

That would remove the current python file.

What if instead of the `ls -l` in `os.system("ls -l")`
someone typed in `rm -rf /`.

All your files would be gone before you know it.

The problem is that [input(prompt)](https://docs.python.org/2/library/functions.html#input)
in Python 2 is the same as `eval(raw_input(prompt))` which means that after reading in the
content of the standard input, python will immediately try to evaluate it.

That's never a good idea. I don't know how Guido thought it would be a good idea to have this feature in the language.

Just remember:

## Python 2

`raw_input(prompt)` and never `input(prompt)`

## Python 3

`input(prompt)`

