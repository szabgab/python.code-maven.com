# PyTest print STDOUT and STDERR using `-s`

{% embed include file="src/examples/pytest/test_stdout_stderr.py" %}

Using also `-q` makes it easier to see the printed text.

```
$ pytest -s -q test_stdout_stderr.py
stdout during testing
stderr during testing
.Adding 2 to 3
.
2 passed in 0.01 seconds
```


