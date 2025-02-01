---
title: "for-else in Python indicating "value not found""
timestamp: 2018-03-27T10:40:01
tags:
  - for
  - else
  - break
published: true
author: szabgab
archive: true
---


There are tons of cases when we are looking for a value in a list of elements and would like to
be able to indicate when we could not find that value.

In most of the languages it is a bit cumbersome.


## Find the first match

For example this very simple example in which we are looking for an even number:

{% include file="examples/python/for_else/find_even_number.py" %}

If we run this program it will set the name `even` to be 4 which is what we wanted.

The problem is that if there is no match (there is no even number) then the variable `even`
will never get a value and thus it will be undeclared.

{% include file="examples/python/for_else/no_even_number.py" %}

Running this program will result in the following exception:

```
$ python no_even_number.py

Traceback (most recent call last):
  File "no_even_number.py", line 8, in <module>
    print(even)
NameError: name 'even' is not defined
```

## Default value outside the loop

One solution to this problem employed in most programming languages is to
set a default value to the `even` variable before we enter the loop.
That way if we pass all the values without finding a match, the variable `even`
already has a value:

{% include file="examples/python/for_else/default_result.py" %}

```
$ python default_result.py

None
```


## for-else

A more elegant way that can be written in Python is the use of `else` after the `for`-loop.

{% include file="examples/python/for_else/for_else.py" %}

The code in the `else` part will be executed if the loop has finished normally, without calling `break`.

That mean if we find a match during our loop, assign it to `even` and leave the loop calling `break`
then the `else` part won't be executed.

Together with the name- or variable-scoping of Python this will result in the same effect, but in my humble opinion
a more elegant way.

