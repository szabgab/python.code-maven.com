# Doctest for bad module

In this case we have a function that works for some input and returns incorrect results for other input.

It can still have documentation with working examples:

{% embed include file="src/examples/testing/bad/fibonacci.py" %}

We can run the tests and they will pass.

```
python -m doctest src/examples/testing/bad/fibonacci.py
```

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


What if someone reports the bug? What shall we do?

