---
title: "Plain function or Callback - An example in Python"
timestamp: 2015-06-28T11:30:01
tags:
  - callback
published: true
books:
  - python
author: szabgab
archive: true
---


What if you need to process a series of values to answer a certain question,
that you cannot store in memory as a list?
For example when you read a huge file? Or if you can calculate the next value based on
some of the previous values and some external information that comes to light during
processing. Even a random series. Or if the series is infinite and you don't know up-front
how far you need to go to find your answer.

In this article we are going to see 2 solutions:

* A plain function.
* A function with a callback.

Then you can follow-up with a solution using [iterators](/callback-or-iterator-in-python)
and another solution using [generators](/function-vs-generator-in-python).


In order to avoid the need to explain a complex algorithm, we are going to use
the well-known Fibonacci series and the question we need to answer is
"What is the first number in the series that can be divided evenly by 17."

A much more complex use-case would be if you needed to go over DNA sequences
in a database, constantly refining your request for the next sequence before
locating one that fits your requirements.

In the case of the Fibonacci series we could compute the first few elements of
the list up-front, but that won't help in the general case. Even in the case of
the Fibonacci series no fixed sublist will be able to answer any arbitrary question,
and in the case of the DNA sequences, it is quite clear that we don't even have
enough memory to prepare the list up-front.

## Simple Fibonacci function

So let's see a simple implementation of the Fibonacci series and then tweak that
solution.

{% include file="examples/python/fibonacci_function.py" %}

There is nothing fancy in this implementation, but I don't recommend that you
run it, as
it does not have any output, and it does not have a stop condition. So if
you run it, it will appear to be "stuck".

You could include a

```python
print(values[-1])
```

in the loop to see what's going on and you could include something like this:

```python
if (values[-1] > 100):
    break;
```

to limit the series.

## Our "question" - divide by 17

Just to remind you that our task is to "research the Fibonacci series",
and the first question we need to answer is
"What is the first number in the Fibonacci series that can be evenly divided by 17?"

So we enhance the function to return the first value that can be divided by 17 with no remainder:

{% include file="examples/python/fibonacci_function_mod_17.py" %}

We just included the following statement, which checks if the current
value of the series can be wholly divided by 17:

```python
if values[-1] % 17 == 0:
    return(values[-1])
```

We have also changed the code to return the Fibonacci number that fulfills
our requirement. It is much better now that the program prints the result.

Running that script will stop at 34.

Later we might have other questions we need to answer. What if there is no answer at all?
In that case we'd better add some safety measures so the code will stop.

## Safety measures - limit the loop

By including a limitation like this, we can make sure our code will eventually
stop, even if we don't have an answer to our particular question.

```python
if values[-1] > 10000:
    return
```

Of course we could use a much bigger number for that or we could base our limitation
on the number of elements checked.

The full code is here:

{% include file="examples/python/fibonacci_function_with_safety.py" %}

## What was the problem?

We now have a simple function that can check a specific condition and return
the first value that matches the condition. If tomorrow I need to answer
"What is the first Fibonacci number that can be evenly divided by 19?",
or maybe
"What is the first Fibonacci number that is the square of another number?",

I can just copy-paste the function and change the condition.

That sounds simple, but that means we have lots of copies of the code implementing
the Fibonacci function. What if our algorithm is much larger? Do we still want to
have that code copied over and over again?

What if we find a bug in our algorithm (or just find a better way to calculate it)
after we have created 20 copies to answer various question?

That's clearly not a good path to go down.

Let's have a different approach. Let's change the Fibonacci function so
it will accept a function as a parameter and will call that function for
every element in the Fibonacci sequence.

## Callback function

The `fibonacci` function now looks like this:
it accepts a parameter called `cb` which is expected to be a function
and once we have calculated the new element in the series we call
the callback function passing the most recent element to it: `cb(values[-1])`.

The returned value is expected to be a list or a tuple in which the first element
will be `True` or `False` indicating if we have found the answer (True)
or not yet (False). If it is True, we return the second element of the result.

```python
def fibonacci(cb):
    values = []
    while(True):
        if len(values) < 2:
            values.append(1)
        else:
            values = [values[-1], values[-1] + values[-2]]

        r = cb(values[-1])
        if (r[0]):
            return(r[1])
```

Based on this the callback function must accept a single value and return
a tuple or a list in which the first element is True/False and the second element
is the value matching our condition.

The callback function looks like this:
It accepts a value `v`, the current value of the series.
It returns `True` and the value it found once it finds a value that can
be evenly divided by 17.

It returns `True` and `None` if it reaches the safety limit we set.
The True will indicate to the fibonacci function that the search has ended,
and the None will indicate to the end-user that no answer was found.

Lastly, we return a tuple with only one `False` value indicating to
the fibonacci function that this was not a good value and we are expecting to be called
with another value.

```python
def check_17(v):
    if v % 17 == 0:
        return (True, v)

    if v > 10000:
        return (True, None)

    return (False,)
```

The full implementation looks like this:

{% include file="examples/python/fibonacci_function_callback.py" %}

This solution is much better than the one we had earlier. Now we don't need to change
the fibonacci function based on the question we are asking. We could move
the fibonacci function to a module, import it and use it as an external resource.
If it needs fixing, it can be fixed in one place, and all the places it is
used will benefit.

Even better, the functions we create as callbacks can also be reused by calling
each other or by passing them to other sequence-generating functions.

## Iterators and Generators

There are two additional solutions to this problem.
One is by creating an [iterator](/callback-or-iterator-in-python),
and the other one is by creating a [generator](/function-vs-generator-in-python).


## Comments

Good explanation. However, I don't see whether or where the callback function "def cb(values[-1])" is actually declared. I see on line 12 where it is referenced, but where do you actually define it?

---

already read

----

Hey there.
cb is defined on line 16 as we see on line 27 that we are using check_17 as cb. cb is the just name for the paramater used in fibonacci().

line 27:
res = fibonacci(check_17)

so then at line 4 this is what the script will do:
def fibonacci(check_17):

so line 12 would rea
r = check_17(values[-1])

which we then go to line 16 and run through that function just replacing 'v' for 'values[-1]'.

Then we check the output of that function in the conditional at line 13

Lastly we have the conditional on line 28 that just makes sure that there is a value to print before printing.

I hope that helps it make sense for those that didn't quite get it.

<hr>

nice explanation

<hr>

How is this a "callback function"? By definition, a callback function should be executed after the first one has ended. This looks like one of those high order functions, which are completely legitimate in Python, since functions are "first class citizens" and are treated equally as any other objects.

<hr>

values [-1], isnt it out of index ? or am I too naive here.

---

I don't think that "naive" is the right word here. In Python you can use negative indexes values[-1] is the last element of the values list.

<hr>

Thanks Gabor,
You selected a good example to explain callbacks.

<hr>

Thanks that really helps with understanding callbacks, I can figure out how to implement this in a class , just assuming i need to use self. construct.


