# PyTest Selective running of test functions

During development you will probably want to focus on a specific test (or a specific group of tests).
You can run a specific test by providing its name:

```
pytest test_failures.py::test_one

pytest test_failures.py::test_two
```


Using the verbose flag (`-v`) can help you get the list of tests.

