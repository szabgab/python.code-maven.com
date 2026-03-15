# Testing class and methods

Pytest allows us to write our tests in an object oriented fashion as well.
In that case we need to create one or more classes called `ClassSomething` in the files
that are called `test_something.py`. In the classes there have to be methods called `test_something`
that are similar to the function in the previous case.

{% embed include file="src/examples/testing/good/test_mymath_with_pytest_class.py" %}

We run the tests the same way.

```
$ pytest test_mymath_with_pytest_class.py
=========================================== test session starts ============================================
platform linux -- Python 3.13.7, pytest-9.0.2, pluggy-1.6.0
rootdir: /home/gabor/github/code-maven.com/python.code-maven.com
configfile: pyproject.toml
plugins: anyio-4.12.0, cov-7.0.0
collected 1 item

test_mymath_with_pytest_class.py .                                                                   [100%]

============================================ 1 passed in 0.07s =============================================
```

Shall we use OOP for writing tests?

Test are supposed to be a lot less complex than our real code. Therefore in general I discourage using OOP in the tests.

