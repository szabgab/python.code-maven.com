---
title: "Python unittest fails, but return exit code 0 - how to fix"
timestamp: 2019-06-01T07:30:01
tags:
  - unittest
  - TestSuite
  - TextTestRunner
  - wasSuccessful
published: true
books:
  - python
author: szabgab
archive: true
---


There are several different ways to run the tests written using the Python unittests package.


Let's test this code, with the obvious bug in it:

{% include file="examples/python/unit_test/app.py" %}

We can write a test-case like this:

{% include file="examples/python/unit_test/test_app.py" %}

## Running with unittest.main

The "standard" or "default" way to run the test is by calling `unittest.main`
as in this code:

{% include file="examples/python/unit_test/with_main.py" %}

It can be executed by running that file using `python with_main.py`

The result looks like this:

```
F
======================================================================
FAIL: test_add (test_app.SomeTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "../examples/python/unit_test/test_app.py", line 7, in test_add
    assert app.add(2, 3) == 5
AssertionError

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
```

If we check the exit code it is

```
echo $?
1
```


## Running TestSuite with unittest.TextTestRunner

{% include file="examples/python/unit_test/with_text_test_runner.py" %}

Just calling `>unittest.TextTestRunner().run(suite)` won't exit the
script and thus won't set the exit code. This is not a good idea as external
tools (e.g. CI systems) will rely on the exit code to determine if running
the tests was successful or not.

So we capture the result of the test run in a variable and then call the
`wasSuccessful` method on it to determine what should be the exit code.



