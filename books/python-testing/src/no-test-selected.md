# No test selected

If you run pytest and it cannot find any tests, for example because you used some
selector and no test matched it, then Pytest will exit with exit code 5.

This is considered a failure by every tool, including Jenkins and other CI systems.

On the other hand you won't see any failed test reported. After all if no tests are run, then none of them fails.
This can be confusing. "CI failed, but no test failed and nothing is reported."

```
$ pytest -k long test_by_marker.py

```

{% embed include file="src/examples/pytest/no_test_selected.out" %}

```
$ echo $?
5
```


