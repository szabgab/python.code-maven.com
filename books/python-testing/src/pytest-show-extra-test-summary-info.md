# Pytest: show extra test summary info with `-r`

Soon we'll learn about the ability to mark certain test functions as expected to fail and others to be skipped in some condition. When running these tests we'll want to be able list these based on their special feature.

Using the `-v` flag would just list all of them which, if you have a lot of tests, would be messy.

The letters one can use with the `-r` flag:

* (f)ailed
* (E)error
* (s)skipped
* (x)failed
* (X)passed
* (p)passed
* (P)passed with output
* (a)all except pP


```
pytest -rx  - xfail, expected to fail
pytest -rs  - skipped
pytest -ra  - all the special cases
```

{% embed include file="src/examples/pytest/test_r.py" %}


