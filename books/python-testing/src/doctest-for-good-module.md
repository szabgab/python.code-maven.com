# Doctest for good module

```
python3 -m doctest src/examples/testing/good/mymath.py
```

In case of success there is no output.

However we can check the exit code which is 0 on success and some other number on failure.

Exit code on Linux and macOS:

```
$ echo $?
0
```

Exit code on Windwos:

```
> echo %ERRORLEVEL%
0
```



We can also use the verbose mode to see the progress:

```
python3 -m doctest -v src/examples/testing/good/mymath.py
```


