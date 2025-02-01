---
title: "Introduction to Python unittest"
timestamp: 2017-10-11T08:30:01
tags:
  - unittest
published: true
books:
  - python
author: szabgab
archive: true
---


Using [doctest](/doctest-in-python) is nice, but it is not very good for large test suites.

The [unittest](https://docs.python.org/3/library/unittest.html) module is another standard module
that provides a much more powerful way to write tests and despite its name it can be used to write integration
and acceptance tests just as well as unittests.


## Simple use case of unittest

From the [previous article](/doctest-in-python) you might be familiar with
the extremely complex Python module that we wanted to test:

{% include file="examples/python/dt/mymod_1.py" %}

It has a single function called `is_anagram` that checks if two strings passed to it are anagrams of each other.

## First tests

{% include file="examples/python/dt/test_mymod_1.py" %}

<h3>The infrastructure</h3>

Unittests usually go into a separate file which is usually called test_*.
This naming is not required for the basic usage, but later we'll see that
the `unittest` module can "autodiscover" the test file and then having
the files named test_* is one way to let it do its job.

Besides, it makes it easier to the humans looking at your code to set the
application code and the test code aside.

Inside the code we need to load the `unittest` module.
We need to create a class that inherits from `unittest.TestCase`.
Naming the class `TestSomething` is not required but that's another
nice convention.

Lastly we need to create methods that start with `test_*`.

We might also need some helper methods that won't be called test_*.

Inside the test-methods we use the `assertTrue` and `assertFalse`
methods inherited from `unittest.TestCase` to assert whether the function
returns `True` or `False` as expected from it.

As opposed to the `assert` statement of Python, these `assert...`
methods will not raise exceptions and thus even if some of them fail, the rest
will still be executed. That way we can get the overall picture of our test
and won't stop on the first failure.

The last piece of infrastructure is the conditional running of the `main`
function. It is only used as convenience to make it easy to run the tests.

```
if __name__ == '__main__':
    unittest.main()
```

<h3>The actual tests</h3>

So far we talked only about the infrastructure of the tests.
In order to actually execute out code, the AUT (Application Under Test)
we need to load it as we would in the "real world". e.g. by `from mymod_1 import is_anagram`
and then inside the `assert..` methods we just call the function we would like to
test. For example: `is_anagram("abc", "acb")`

<h3>Running the tests</h3>

As we included the condition running of the tests in the test-file itself we can run the test-file
directly: `python test_mymod_1.py`

```
$ python test_mymod_1.py

.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

The single dot `.` and the number 1 indicate that we had one test_* method in our file.
It does not count the individual assertions.

The `OK` tells us that every assertion in every test_* method passed.

## Dealing with failures

As in the previous article, here too we would like to see what happens if a test fails.
In our case someone was not satisfied with single-word anagrams and expected to be
able to have spaces in at least one of the "words". We test this by adding 
another test_* method to our file:

{% include file="examples/python/dt/test_mymod_2.py" %}

Running this file we get the following output:

```
$ python test_mymod_2.py

.F
======================================================================
FAIL: test_multiword_anagram (__main__.TestAnagram)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_mymod_2.py", line 12, in test_multiword_anagram
    self.assertTrue( is_anagram("anagram", "nag a ram") )
AssertionError: False is not true

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
```

Here we can see a single dot `.` indicating a single test_* method that had
all its assertions passed and a single `F` that indicates the test_* method
that failed at least one of its assertions.

The `FAIL` part indicates the test_* method that failed.

The `Traceback` provides detailed information about the actual failure.

## Running individual test methods

If you encounter a failure in one of the tests in your test suite, you will usually want
to fix the problem that generated that test-failure.
For that you'll want to run the tests repeatedly, but when focusing on one part of the code
and on a single test_* method, it might be a waste of time to keep running the whole
test-suite. Luckily `unittest` allows us to run the test methods individually.
for that we need to pass the name of the test-class and the name of the test-method on
the command line: `python test_mymod_2.py TestAnagram.test_anagram`.

The output for the successful test method looks like this:

```
$ python test_mymod_2.py TestAnagram.test_anagram

.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

Here you can see that there is only a single dot `.` indicating that only a single
test-method was executed.


The output of the failing test method looks like this:

```
$ python test_mymod_2.py TestAnagram.test_multiword_anagram

F
======================================================================
FAIL: test_multiword_anagram (__main__.TestAnagram)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_mymod_2.py", line 12, in test_multiword_anagram
    self.assertTrue( is_anagram("anagram", "nag a ram") )
AssertionError: False is not true

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

Here you can see a single `F` and no dot `.` indicating that only a single failing
test-method was executed.

## Running tests without the conditional running

The last part of the test-files are actually not really necessary.
We could eliminate the

```
if __name__ == '__main__':
    unittest.main()
```

and have the following:

{% include file="examples/python/dt/test_mymod_3.py" %}

Then we need to load the `unittest` module on the command line as well.
Like this:

```
python -m unittest test_mymod_3
```

The result would be the same.

We can also run the individual test-methods by providing the exact, dot-separated path
on the command line: (test-file.test-class.test-method)

```
python -m unittest test_mymod_3.TestAnagram.test_multiword_anagram
```


## Test discovery

Finally, as we named our test-files test_* we can also make use if the `autodiscovery` feature
of the `unittest` module. We can run `python -m unittest discover` and let it find
all the tests files.

In our case this will be a bit funny as we have 3 files in our directory with (almost) the same tests.
That's because of the examples above. However this can also show that the `discover` feature
runs all the 3 files.

The report actually does not indicate that there were 3 files only, that we have a total of 5 test-methods.
3 dots `.` indicating 3 methods that were successful. 2 `F` characters indicating that
two of the methods failed. (Yes, I know, they are copies of each other.)


```
$ python -m unittest discover

..F.F
======================================================================
FAIL: test_multiword_anagram (test_mymod_2.TestAnagram)
----------------------------------------------------------------------
Traceback (most recent call last):
  File ".../examples/python/dt/test_mymod_2.py", line 12, in test_multiword_anagram
    self.assertTrue( is_anagram("anagram", "nag a ram") )
AssertionError: False is not true

======================================================================
FAIL: test_multiword_anagram (test_mymod_3.TestAnagram)
----------------------------------------------------------------------
Traceback (most recent call last):
  File ".../examples/python/dt/test_mymod_3.py", line 12, in test_multiword_anagram
    self.assertTrue( is_anagram("anagram", "nag a ram") )
AssertionError: False is not true

----------------------------------------------------------------------
Ran 5 tests in 0.001s

FAILED (failures=2)
```

In Python 3 you don't even add the `discover` to the end. This will already start the discovery process:

```
$ python -m unittest 
```


## Conclusion

In any case you can now write tests using the `unittest` module.
You can run them and if something fails you can focus on the failing test
instead of running the whole suite again and again.

BTW as you can see the test-methods are the smallest units the `unittest`
module can operate on, so it is probably a good idea to keep them very short
and focused on specific features.

## Comments

That was awesome explanation about uninttest.
Would like to know one thing, is there a possibility of collecting all failed test cases & rerunning ?


