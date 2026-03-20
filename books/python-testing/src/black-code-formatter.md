# Black code formatter

The [black](https://pypi.org/project/black/) code formatter.


```
$ pip install black
```

In the CI one can use the `--check` flag. It won't change the code. It will only report if the code is formatted according to its rules. It will fail if `black` would want to change the format.

```
$ black --check .
```

Read the help and the [documentation](https://black.readthedocs.io/)

```
black -h
```

