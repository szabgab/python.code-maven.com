---
title: "range vs. xrange in Python"
timestamp: 2015-06-25T16:30:01
tags:
  - range
  - xrange
  - sys.getsizeof
  - type
published: true
books:
  - python
author: szabgab
archive: true
---


[Python](/python) has a built-in function called `range` that can easily generate
a range of whole numbers. There is another built-in function called `xrange` that provides the
same result, but uses a lot less memory.


## range and xrange

In the following 3 examples we could replace `range` by `xrange` and receive the same result:

{% include file="examples/python/range_3_7.py" %}

From the first number (3) until one less than the second number (7):

<pre>
3
4
5
6
</pre>

{% include file="examples/python/range_5.py" %}

If there is only one number, that will be the end number and the default start number
will be 0. Thus `range(5)` is the same as `range(0, 5)`

<pre>
0
1
2
3
4
</pre>

{% include file="examples/python/range_step.py" %}

If there are three parameters, the third one is the "step" that defaults
to 1 if the third parameter is not present. The result will be the following:

<pre>
0
2
4
</pre>

## Variable holding a range

What if we would like to create a variable that will hold the range?
We can do that and it is quite simple with either `range`
or `xrange`

```python
r = range(1000)
```

Then we can go over the elements:

```python
for v in r:
    pass
```

or we can access them by index:

```python
print(r[4])
```

## Memory Size

The big difference is in the amount of memory they use:

{% include file="examples/python/range-memory.py" %}

The variable holding the range created by `range` uses 80072 bytes
while the variable created by `xrange` only uses 40 bytes.

The reason is that `range` creates a list holding all the values while
`xrange` creates an object that can iterate over the numbers on demand.

{% include file="examples/python/range-type.py" %}

## Speed - Benchmarking range and xrange

The "cost" of the memory savings is that looking up indexes in xrange
will take slightly longer. This benchmark code uses the `timeit`
module to show that the xrange version is 10% slower:

{% include file="examples/python/range-benchmark.py" %}

The resulting numbers are:

<pre>
2.16770005226
2.35304307938
</pre>
