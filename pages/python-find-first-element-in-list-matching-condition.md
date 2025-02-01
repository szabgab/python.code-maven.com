---
title: "Find the first element in Python list that matches some condition"
timestamp: 2020-11-30T15:40:01
tags:
  - filter
  - next
  - for
  - else
  - lambda
description: "Filtering elements of a list based on some condition and then picking the first of them."
published: true
books:
  - python
author: szabgab
archive: true
show_related: true
---


Sometimes you'll have a list in python and you'd like to find the first element in that list that matches some arbitrary condition. We'll see now how to do that.

For our example the condition is very simple, the length of a string being longer than 5 characters.

Oh and if you are interested, I also wrote a solution to [find the first matching element using Perl](https://perlmaven.com/first)
where there is a function called <b>first</b>.


## Find first element using a for loop

The first solution that might come to mind is using a <b>for</b> loop. Grammatically I find it strange, but Python has a nice programming technique.
You can add an <b>else</b> part to a <b>for-loop</b> and this <b>else</b> part will be executed if the loop finished  "normally", without calling <b>break</b>.

{% include file="examples/python/first_loop.py" %}

## Find first element using filter and next

Another way that is more compact and some people might find nicer is to use the <b>filter</b> function of Python.
Usually we use it to create a  shorter list of elements meeting some condition. In this case however we don't need to store the result
of the <b>filter</b> call in a variable. Instead we can call the <b>next</b> function. This will return the next element returned by the
filter object. Which, in our case, will be the first element in the list.

The only issue is that if there were no matching values, this call would raise an exception. Adding a second parameter to the <b>next()</b>
call, Python will return that value. <b>None</b>, in our case.

I've added a second copy to the solution in which I've separated the steps: First assigning the result of <b>filter</b> to a variable and then calling
<b>next</b> on it. It is there only to make it easier to understand the construct.

{% include file="examples/python/first_filter.py" %}

The output will look like this:

```
etruscan shrew
-------
<filter object at 0x7f1519456a00>
etruscan shrew
```

## Show the operations

In Python 2 <b>filter</b> would have returned a list already checking all the values of the original list. That would be a waste of time and CPU.
The <b>filter</b> function in Python 3 returns a filter object and only executes the filtering condition when the user actually wants to find the next element
in the filtered list. You believe me (and the documentation)? Do you want to see it with your own eyes? Fair enough, let's try it.

In this example, instead of a <b>lambda-function</b> I used a function defined using <b>def</b> and in this function I've added a <b>print</b>-statement as
well so we can see when it is executed and with what values?

{% include file="examples/python/first_filter_log.py" %}

This is the output:

```
len(snake)
len(camel)
len(etruscan shrew)
etruscan shrew
```

As you can see it stopped calling the <b>condition</b> function once it encountered the first matching string.

## Etruscan shrew

In case you were wondering the [Etruscan shrew](https://en.wikipedia.org/wiki/Etruscan_shrew)
is the smallest mammal by mass.

<img src="/img/220px-Suncus_etruscus.jpg" alt="Etruscan shrew">

There is a shorter mammal, but this looks better.

