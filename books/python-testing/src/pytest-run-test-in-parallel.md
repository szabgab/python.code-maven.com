# PyTest: Run tests in parallel with xdist

By default pytest runs the test-unctions sequentially. So if we have 4 test-function each of them taking 2 seconds, the whole test-suite will run 8 seconds.

The [pytest-xdist](https://pypi.org/project/pytest-xdist/) plugin adds a new command-line flag `-n` that allows us to set the number of workers. This makes it possible to run tests in parallel.

For this it is extremly important that the tests are indpendent and they don't use the same resource.
(eg. each one will use its own folder or its own database)

```
$ pip install pytest-xdist
$ pytest -n NUM
```

We have two test files, each of them two tests taking 2 seconds each:

{% embed include file="src/examples/pytest/xdist/test_animals.py" %}
{% embed include file="src/examples/pytest/xdist/test_colors.py" %}

```
$ time pytest          8.04 sec
$ time pytest -n 2     4.64 sec
$ time pytest -n 4     3.07 sec

$ time pytest -n auto  3.96 sec using 8 workers
```


