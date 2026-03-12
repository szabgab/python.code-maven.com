# Doctest for bad module with failure

We can add another test case that was reported to return bad results.


{% embed include file="src/examples/testing/failure/mymath.py" %}


We can run doctest:

```
python3 -m doctest src/examples/testing/failure/mymath.py
```

```
$ python -m doctest mymath.py
**********************************************************************
File ".../src/examples/testing/failure/mymath.py", line 8, in mymath.add
Failed example:
    add(2, 3)
Expected:
    5
Got:
    6
**********************************************************************
1 item had failures:
   1 of   2 in mymath.add
***Test Failed*** 1 failure.
```

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


At this point we probably need to fix our code or comment out the failing test-case.

