---
title: "Creating an Iterator in Python"
timestamp: 2015-07-21T11:30:01
tags:
  - raise
  - StopIteration
  - for
  - __iter__
  - next
published: true
books:
  - python
author: szabgab
archive: true
---


An "iterable" object in Python is one that we can iterate on it using a `for` loop.
For example a list is "iterable" because we can iterate over its elements:

{% include file="examples/python/iterate_on_list.py" %}

to see:

<pre>
Foo
Bar
Zorg
</pre>


A string is also iterable because we can iterate over its characters:

{% include file="examples/python/iterate_on_string.py" %}

<pre>
F
o
o

B
a
r
</pre>

A much more interesting example might be the use of `xrange` that creates
an iterable object without taking up precious memory.

{% include file="examples/python/iterate_on_xrange.py" %}

See [range vs. xrange](/range-vs-xrange-in-python)
for a longer discussion on the topic.

## Why to create your own iterator?

Before showing how to create your own iterator, let's try to figure out why
and when would we want to do that?

In all the following case you could achieve the same result without
using a real iterator object, but creating an iterator object will allow us to
use a simple `for`-loop which will make our code look more similar to
other code written in Python.

One of the use-cases is when you would like to go over an infinite series of
values up to a point that is determined only later, probably by some external force.
For example take the well known case of the Fibonacci series.
You might want to look at each element of the series and stop at the first element
that can be divided by 17.

That case can already benefit from an iterator, but what if you work with a bunch
of people researching the Fibonacci series. Each one of them will want to go
over the Fibonacci series and stop at some condition. We just don't know what
condition will be.

So we can create an iterator object that will be able to iterate over the Fibonacci
numbers until the code of the researcher says it to stop or until power runs out of
the computer.

## Create an iterable

An iterable object can be created by any class. It only needs 3 things:
2 required and one optional.

The two required are:

<ol>
  <li>A method called `__iter__` that will return the instance object. A very simple piece of code.</li>
  <li>A method called `next` that will return the next value of the iterable.</li>
</ol>

These two will create an unbounded or unlimited iterator.

Optionally you might want your iterator to stop at a certain point by itself. You can achieve that
by having the `next` method `raise` a `StopIteration` exception.

## Finate Iterator

In this example the constructor of the Fibonacci class is expected to receive a number,
the number of elements we would like to iterate over. It does not calculate all the numbers
at once, instead it computes the next element every time the `next` method is called
which is done internally by the `for` loop.

When the iteration counter reaches the limit originally provided, itraises a StopIteration
exception which is caught by the `for` loop (again without us doing anything special)
and terminates the for-loop.

{% include file="examples/python/fibonacci_finate_iterator.py" %}

## Infinite Iterator

In the next solution we don't need to provide a limit, our iterator never raises
an exception, and therefor it never stops by itself. We assume that the user
who uses this iterafor will have some code in place that will stop the iteration
by calling `break` on some condition.
This condition can be related to the series itself, (e.g. we have iterated over 100
elements), or it can be totally unrelated. (e.g. some user input. Elapsed time.
Day of the week. Etc.)

{% include file="examples/python/fibonacci_iterator.py" %}


## Comments

Very nice. Thank you!

<hr>

%> python3 fibonacci_finate_iterator.py
TypeError: iter() returned non-iterator of type 'Fibonacci'

