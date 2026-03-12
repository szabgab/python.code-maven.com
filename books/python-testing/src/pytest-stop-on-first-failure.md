# PyTest: stop on first failure

Seeing all the failures might help in some case, but in in some other cases, especially during development, you might not want to wait for all the tests to run.

You might want to stop at the first test failure and fix that.

You can achieve that by using the `-x` flag. In the more generic case you can also use the `--maxfail N` flag where you can explicitely say to stop running after N failures.

```
pytest -x
pytest --maxfail 1
```

