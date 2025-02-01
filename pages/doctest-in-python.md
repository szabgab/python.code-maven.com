---
title: "Doctest in Python"
timestamp: 2017-10-04T17:30:01
tags:
  - doctest
  - __doc__
published: true
author: szabgab
archive: true
---


There are several testing libraries in Python. One of the simplest is called
[doctest](https://docs.python.org/3/library/doctest.html).
It is good for stand-alone libraries, not something where you need a lot of work to
set up the environment, but then it is a great way to also ensure that the documentation
is correct.


## A simple module

Let's create a simple module that has a function to check
if two given strings are [Anagram](https://en.wikipedia.org/wiki/Anagram)

{% include file="examples/python/dt/mymod_1.py" %}

It is not perfect, but it works in some of the cases.

For example this call will return `True`:

```python
is_anagram("silent", "listen")
```

This call too:

```python
is_anagram("abc", "acb")
```

On the other hand this call will return `False`

```python
is_anagram("one", "two")
```


## Documentation of functions

You probably know that you can add strings, even multi-line strings
to your code and if they are not assigned to any variable and not used in
any function, Python will just desregard them.

In addition if this string happens to be the first statement immediately after
the `def` line declaring a function then this string will be considered
to be "The documentation of the function".

Here it is:

{% include file="examples/python/dt/mymod_2.py" %}

We can then access this string using the `__doc__` attribute of the function object:

{% include file="examples/python/dt/use_mymod_2.py" %}

If we run this script we get:

```python
 $ python use_mymod_2.py

    Any Text
    Can be documentation

```

## Interactive Shell

You probably also know the Interactive Shell of python.
If you type in `python` on the command line without
any additional paramters you'll find yourself in the interactive
shell where you can type in commands to Python directly:
The 3 &gt; signs are the prompt:

```python
$ python
>>> 2 + 3
5
```

We could also import a module and use its functions

```python
>>> from mymod_2 import is_anagram
>>> is_anagram("silent", "listen")
True
>>> is_anagram("abc", "acb")
True
>>>> is_anagram("one", "two")
False
```


## Doctests

The [doctest](https://docs.python.org/3/library/doctest.html) module
will read the documentation of the functions in your code, assuming it looks
like a session from the Interactive Shell. It will execute the commands it finds
and compares the results with the expected result found in the documentation.

{% include file="examples/python/dt/mymod_3.py" %}

We need two things for this:

We added some documentation to ou function that looks like a session from the interactive shell.
(No need to import the function.)

We also have some code at the end of the file that will import the `doctes` module
and run the `testmod` function that will look for functions and the documentation
of the functions in the same file. It is protected by an `if` statement to make sure
the doctest related code only executes when we run our file directly and not when we load it
as a module.

If we run the file directly it will have no output. It is a bit strange, but that's how doctest
indicates that everything is fine.

```
python mymod_3.py
```

We could also add the `-v` verbos flag and we would get a lot of details on the execution:

```
$ python mymod_3.py -v

Trying:
    is_anagram("abc", "acb")
Expecting:
    True
ok
Trying:
    is_anagram("silent", "listen")
Expecting:
    True
ok
Trying:
    is_anagram("one", "two")
Expecting:
    False
ok
1 items had no tests:
    __main__
1 items passed all tests:
   3 tests in __main__.is_anagram
3 tests in 2 items.
3 passed and 0 failed.
Test passed.
```


## Failing tesst

In the above case all the calls returned the expected result.
What if someonf ask us if `"nag a ram"` is an anagram of the word `"anagram"`
which should be.

We can add another test case:


```python
>>> is_anagram("anagram", "nag a ram")
True
```

{% include file="examples/python/dt/mymod_4.py" %}

If we run our module now, we will get an error message:

```
$ python mymod_4.py
**********************************************************************
File "mymod_4.py", line 10, in __main__.is_anagram
Failed example:
    is_anagram("anagram", "nag a ram")
Expected:
    True
Got:
    False
**********************************************************************
1 items had failures:
   1 of   4 in __main__.is_anagram
***Test Failed*** 1 failures.
```

The test has failed as our `is_anagram` function assumes that there are the exact
same amount of whitespaces in both strings.

At this point, you the programmer can decide what should be the behaviour of the `is_anagram`
function change the function and update the tests if necessary.

## Conclusion

Having doctests in the code will provide the reader with well tested examples the reader can copy
and paste.

It makes sure the examples in the documentation and the code don't diverger.

It will help reduce the risk for when someone makes changes to the code (a re factoring, a bug fix, a new feature) 
making it much less likely that the behaviour would change, that there will be some regression
of the code.


