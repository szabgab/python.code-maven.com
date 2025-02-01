---
title: "Function vs Generator in Python"
timestamp: 2015-06-28T15:00:01
tags:
  - yield
published: true
books:
  - python
author: szabgab
archive: true
---


We saw how take a [simple function and using callbacks](/function-or-callback-in-python) make it more general.
We also saw how to [create an iterator](/callback-or-iterator-in-python) to make our code more straight-forward.
This time we are going to see how to convert the plain function into a generator that,
after understanding how generators work, will seem to be the most obvious solution.


## Plain function

As a reminder let's see the original plain Fibonacci function we started with,
that we had to change to hold our hard-coded condition, or in the more flexible
case that we had to make it execute a callback function.

{% include file="examples/python/fibonacci_function.py" %}

## Generator

{% include file="examples/python/fibonacci_generator.py" %}

The example with the generator is almost exactly the same as the plain function,
and the way we can use it is exactly the same as we use the
[iterator](/callback-or-iterator-in-python)

The only addition in the generator implementation of the `fibonacci`
function is that it calls `yield` every time it calculates one of
the values. This call pauses the execution of the `fibonacci` function
and returns the command to the calling entity together with the value passed
to the `yield` statement.

For the first iteration of the `for` loop the `fibonacci` function
will start running from its first statement assigning an empty list to `values`.

When it encounters the `yield` statement it will return the value in `values[-1]`
that will be assigned to `f` of the `for` loop and it will let the `for`
loop execute its code. There we can put any condition to break-out from the loop.

If we don't `break` on the first iteration then on the subsequent
iterations of the `for` loop the `fibonacci` function will continue
from the exact state where it was paused. Meaning the content of the `values`
will be exactly the same as it was left, and the first statement to be executed will be the one
immediately after the `yield` statement which, in this case, will be checking
if `True` is still true in the `while(True):` statement.

So from the outside the `fibonacci` function will behave just as the
[Fibonacci iterator](/callback-or-iterator-in-python) does which
makes our code simple.


## Comments

1. You shouldn't have to collect values in fibonacci function if you yield them
2. Instead of checking length of array just add start values into `values` array before `while` cycle

def fib_gen():
    a = 1
    b = 1
    yield b
    while True:
        yield b
        a,b = b,a+b

fibonacci = fib_gen()
for item in xrange(10000):
    fib_number = fibonacci.next()
    if fib_number  % 17 == 0:
         print fib_number 
         break


<hr>

instead of using xrange, or range in Python 3, alongside with __next__(), you could do the following in your for loop:

k,n=0,10000
for i fib_gen():
k+=1
if i % 17 == 0:
print(i)
break
if k==n:
break


