# Doctest for bad module with failure

We can add another test case that was reported to return bad results.


{% embed include file="src/examples/testing/failure/fibonacci.py" %}


We can run doctest:

```
$ python3 -m doctest fibonacci.py
**********************************************************************
File "src/examples/testing/failure/fibonacci.py", line 5, in fibonacci.fib
Failed example:
    fib(1)
Expected:
    0
Got:
    1
**********************************************************************
1 item had failures:
   1 of   4 in fibonacci.fib
***Test Failed*** 1 failure.
```

It still checked all the 4 test cases and reported that one of them failed.

The exit code will also indicate the failure.

Exit code on Linux and macOS:

```
$ echo $?
1
```

Exit code on Windwos:

```
> echo %ERRORLEVEL%
1
```


At this point we probably need to fix our code, but for this course we are more intereste in the various ways
we can test code and how failures are reported.


