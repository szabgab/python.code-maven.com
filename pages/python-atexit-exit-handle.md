---
title: "Python atexit exit handle - like the END block of Perl"
timestamp: 2019-07-19T14:30:01
tags:
  - atexit
  - END
published: true
books:
  - python
author: szabgab
archive: true
---


The word <b>Postmoretem</b> is used in several context. One is the when a (software development) project was finished.
Wikipedia describes it as [Postmortem documentation](https://en.wikipedia.org/wiki/Postmortem_documentation).

It is a very useful technique to lear from all the good and bad that happened during the project.

Python provides a way to do a sort of a "post mortem" of a Python program after it exits. Even if it exited in a very
exceptional way.

Perl programmers might be familiar with the concept using an [END](https://perlmaven.com/end) block.


Python provides a module called [atexit](https://docs.python.org/3/library/atexit.html)

That is, you can designate a function (or more functions) to be execute after your script called `exit()`, fall
out at the end of the file, or even raised an uncaught exception, just before python exits.

Here is an example how to use it:

<a href="examples/python/end.py">

You need to import `atexit` and then you need to register a function either with the `atexit.register`
method or using the `@atexit.register` decorator.

This script can end in 3 ways:

If we call it without any parameters it will end with the `exit` call:

```
$ python end.py
Usage: end.py A B
myexit
```

If we provide two number when the second one is not 0 it will print out the result of the division and fall off the end
of the file:

```
$ python end.py 4 2
2
myexit
```

If we call it with the second argument being 0 it will rais a ZeroDivisionError exception which is not caught and thus
the script will stop running.


```
$ python end.py 4 0
Traceback (most recent call last):
 File "end.py", line 13, in module
   print(int(sys.argv[1]) / int(sys.argv[2]))
ZeroDivisionError: integer division or modulo by zero
myexit
```

As you can see above, in every case the last line of output was "myexit" that was printed out by the `myexit`
function that was registered as an atexit function.


Instead of printing out some text we can use this technique to do some cleanup work in our environment evemn if our
application dies due to an unhandled exception.

Or as I like to put it in a slightly incomprehensible way: "execute some code after the script exited".

