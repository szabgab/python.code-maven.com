---
title: "Caching results to speed up process in Python"
timestamp: 2019-04-16T17:30:01
tags:
  - levenshtein
published: true
books:
  - python
author: szabgab
archive: true
---


If you need to calculate the same thing multiple times it is often better to use in-memory caching to eliminate some of the processing.
Sometimes the processing part involves disk- or networkaccess that makes it slow. Sometime it is "just" using the CPU.

Memoization is usually the name of the process and one can write a generic Memoizer if that's needed. In this example
we'll do the caching manually. We'll look at two implementation calculating the [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance)
of strings.


## Pylev

In the first example we used the [pylev](https://pypi.python.org/pypi/pylev) module.
This is our script:

{% include file="examples/python/levenshtein_pylev.py" %}


The non-cached version is just a function wrapping the call to `pylev.levenshtein`

The cached version usses the dictionary representing the wrapper function `cached` to store the
cached results.

This snippet checks if we already have a key called 'data' in that dictionary, and creates one if there was no data yet.
This would only happen the first time we call the 'cached' function.

```pyhton
    if 'data' not in cached.__dict__:
        cached.data = {}
```

Then we create a key using the input parameters in a tuple. In the case of the Levenshtein distance the order of the parameters
does not matter and thus we can theoretically save some memory if we sort the parameters first, but in the more generic case
we might need to stick to the order. So I'll do that here as well.

```pyhton
    k = (a,b)
```

Then, if the key is not in the caching dictionary yet, we call the real Levenshtein function and store the result in the cache.

```pyhton
    if k not in cached.data:
        cached.data[k] = pylev.levenshtein(a, b)
```

Finally we return the value from the cache. Regardless wheteher it was calculated now, or in one of the earlier calls.

```pyhton
    return cached.data[k]
```


I picked two rather random strings to compare and we use `timeit` to run the function several times and measure the
elapsed time.

The actualy number of repetition is received from the command line. This allows us to run the file with varius numbers
like this: `python levenshtein_pylev.py 42`.


Here are the results for some numbers:


```
 N non_cached               cachced
 1 0.0005512761417776346    0.000554962083697319
10 0.009959910064935684    0.000820280984044075
100 0.06429028487764299 0.000595971941947937
1000 0.5230045560747385 0.0012550328392535448
10000 5.692702914122492 0.009364967932924628
```


## Editdistance

In the second example we use the editdistance module.

{% include file="examples/python/levenshtein_editdistance.py" %}


