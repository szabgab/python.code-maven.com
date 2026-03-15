# Pytest failing test in one function

Once we had that passing test we might have shared our code just to receive complaints that it does not always work properly. Specifically passing in 1 should return , but it returns 1.

So for your investigation the first thing you need to do is to write a test case expecting it to work proving that your code works. So you add a second assertion.

{% embed include file="src/examples/testing/bad/test_fibonacci_with_pytest_failing.py" %}

To your surprise the tests fails with the following output:


```
$ pytest test_fibonacci_with_pytest_failing.py
=========================================== test session starts ============================================
platform linux -- Python 3.13.7, pytest-9.0.2, pluggy-1.6.0
rootdir: /home/gabor/github/code-maven.com/python.code-maven.com
configfile: pyproject.toml
plugins: anyio-4.12.0, cov-7.0.0
collected 1 item

test_fibonacci_with_pytest_failing.py F                                                              [100%]

================================================= FAILURES =================================================
_________________________________________________ test_fib _________________________________________________

    def test_fib():
>       assert fib(1)  == 0
E       assert 1 == 0
E        +  where 1 = fib(1)

test_fibonacci_with_pytest_failing.py:5: AssertionError
========================================= short test summary info ==========================================
FAILED test_fibonacci_with_pytest_failing.py::test_fib - assert 1 == 0
============================================ 1 failed in 0.12s =============================================

```

We see the `collected 1 item` because we still only have one test function.

Then next to the test file we see the letter F indicating that we had a single test failure.

Then we can see the details of the test failure. Among other things we can see the actual value returned by the `fib` function
and the expected value.

Knowing that `assert` only receives the True or False values of the comparison, you might wonder how did this happen.
This is part of the magic of pytest. It uses some introspection to see what was in the expression that was passed to `assert` and it can print out the details
helping us see what was the expected value and what was the actual value. This can help understanding the real problem behind the scenes.


You can also check the exit code and it will be something different from 0 indicating that something did not work.
The exit code is used by CI-systems to see which test run were successful and which failed.

```
$ echo $?
1
```

```
> echo %ERRORLEVEL%
1
```

One big disadvantage of having two or more asserts in the same test function is that we don't know what would be the result of the other asserts.


