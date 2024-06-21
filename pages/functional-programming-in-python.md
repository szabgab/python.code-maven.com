---
title: Functional programming in Python
timestamp: 2024-06-21T08:30:01
author: szabgab
published: true
description: How functional-style programming can be used in Python.
tags:
    - map
    - filter
    - reduce
    - zip
    - list comprehension
    - generator expression
todo:
    - TODO
---

{% youtube id="QgehdVJoHUE" %}


* [Python slides](https://code-maven.com/slides/python/)
* [Source of the slides](https://github.com/szabgab/slides/)
* [list generator](https://code-maven.com/slides/python/list-generator)
* [YouTube channel](https://code-maven.com/youtube)
* [Python Maven Telegram group](https://t.me/+stsA0F0rzCAzYjlk)


## Notes

Iterables: list, string, range

What does `range` return?

Taking up less space `sys.getsizeof()`

`for` loop with some transformation - from a list of numbers create a new list with the doubles of each value, use a function to calculate them.

```
map(function,  iterable)
```

first iterate over the results

use `list` to flatten the `map` object.
Show the size.

Add a print statement to the to the double function to show how it is printed on every iteration.

Add a condition in the for loop to `break` out the loop when the number is negative

Instead using a named function, we could use a `lambda` function.


Two lists (with the same number ov values) use a `map with a lambda function on the two lists:

```
map(function, iterable_a, iterable_b)
```

what if one list is shorter? - stop iterating

`map` to fetch

`filter` - filter out big numbers


**list-comprehension**

**generator expression**

`reduce`

```
from functools import reduce
print(reduce(lambda x,y: x+y, numbers))
```

`reduce` with default

```
for f_name, l_name, b_date in zip(fname, lname, born):
    print(f"{f_name:7} {l_name:7} was born {b_date}")

```
