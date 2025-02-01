---
title: "Python unittest"
timestamp: 2017-01-01T07:30:02
tags:
  - files
published: false
books:
  - python
author: szabgab
archive: true
---


## Order of the tests

The test me

{% include file="examples/python/ut/test_order.py" %}



(The dots are the regular output of `unittest`)

```
$ python -m unittest  test_order

test_another
.test_one
.test_third
.
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```


## Verbose mode

Adding the `-v` flag would actually tell `unittest` to print
out the names of the test functions as the are being called, but where is the
fun if we don't reinvent the wheel a bit?

```
$ python -m unittest -v test_order

test_another (test_order.TestOrder) ... test_another
ok
test_one (test_order.TestOrder) ... test_one
ok
test_third (test_order.TestOrder) ... test_third
ok

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```


## Fixture: setUp and tearDown

Except of the most simple unittests, most test need to have some environment set up before
the actuall test can be done. This can be as simple as creating an instance object
of some class, or very complex that might involve setting up a database, a web server etc.
This environment is usually referred to in the littreature as `fixture`.

The same setup code might need to be repeated for many test methods. Instead of repeating
the code in every test function the natural improvement is to factor it out to a common
method and then call that method at the beginning of each test method.

The `unittest` class provide an even better technique.

If we implement a method called `setUp` then before each test method this
`setUp` method will be called.

In addition we can implement a method called `tearDown` that will be called
after each test method.

These can provide a familiar structure to tests.

In this example we can see what is the order of the various method calls,
including one that is a helper method. As it does not start with `test_`
and it is not one of the special method names, it will not be called by
the `unittest` framework. The purpose of any such helper method
would be to call them from our test methods.
(The dots are the regular output of `unittest`)

{% include file="examples/python/ut/test_order_with_setup.py" %}


```
$ python -m unittest  test_order_with_setup

in setUp
test_another
in tearDown
.in setUp
test_one
in tearDown
.
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```


{% include file="examples/python/ut/test_some.py" %}

