---
title: "Callback or Iterator in Python"
timestamp: 2015-06-28T13:10:01
tags:
  - for
published: true
books:
  - python
author: szabgab
archive: true
---


Earlier we saw how [callbacks can be better than plain functions](/function-or-callback-in-python),
but we have other possible solutions. We can also create a possibly unbounded iterator that will go over the elements
of our series making our code look even more straight-forward than the solution with the callback.


## Solution with Callback

Just as a reminder, here is our solution with a callback. We have a function called
fibonacci that goes over the elements of the series and for each element it
calls the `check_17` function passed to it.

{% include file="examples/python/fibonacci_function_callback.py" %}

The fact that we had to be able to signal to the `fibonacci`
function when to stop made our code slightly more complex than we hoped for.
We had to return a tuple in which the first element was the True/False indicator.

## Create a Fibonacci iterator

Let's turn the whole thing around and let the end-user retain full control of
the looping. We create a `Fibonacci` class that becomes iterable by
the addition of the `__iter__` method which just returns the object,
and by having a `next` method (In Python 3 I think it should be `__next__`)
that will return the next element.

The object internally will keep the current state of the iteration, which in our case
means it needs to keep the last two elements of the series.

{% include file="examples/python/fibonacci_iterator.py" %}

Calling  `fib = Fibonacci()` will create an iterator object and as such,
we'll be able to use the `for in` construct on it to iterate over the
elements. Because the is an unbounded iteator, that is one that does not have
an end, we have to make sure there is some code inside the `for` loop
that will stop it no matter what.

This solution seem to be more simple to use than the one [with callbacks](/function-or-callback-in-python)
