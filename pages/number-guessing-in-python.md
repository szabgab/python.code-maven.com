---
title: "Solution: Number guessing game in Python"
timestamp: 2015-10-18T12:00:01
tags:
  - exercises
  - random
  - randrange
  - int
  - if
  - else
  - elif
published: true
books:
  - python
author: szabgab
archive: true
---


In this [exercise](/exercises), you were asked to create the first version of the
[Number guessing game](/exercise-number-guessing-game). Here we are going
to see a solution in Python.


## Solution in Python 2

{% include file="examples/python/number_guessing.py" %}

The first thing is to load the [random](https://docs.python.org/2/library/random.html) module.
It has a method called `randrange` that can generate an integer number ina given range.
In our case we wanted to have a number that can be 1 .. 200 but because of the way the Python range works
we had to call the method with 201 as the ranges in Python never include the upper boundary.

the commneted out
```
# print hidden
```

is only there so if we remove the commenting, then we can see what was the hidden value and we can check
if the program works as expected.

Then we use the `raw_input` function to prompt and to read the value from the standard input.
Just as in Ruby, here too the value we receive is a string. We use the `int` function to convert it
to an integer number.

Once we have the `guess` we can compare it to the `hidden` number and provide feedback to
the user.

## Solution in Python 3

{% include file="examples/python3/number_guessing.py" %}

There are two differences compared to the Python 2 solution:

<ol>
  <li>`print()` is now a function. It requires parentheses around the parameters.</li>
  <li>Instead of `raw_input`, now we should use the plain `input` function to get values from standard input.</li>
</ol>

