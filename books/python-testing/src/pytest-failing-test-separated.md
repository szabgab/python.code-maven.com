# Pytest failing test separated

Instead of putting the several asserts in the same test function we could also put them in separate ones like in this example.

{% embed include file="src/examples/testing/bad/test_fibonacci_with_pytest_failing_separated.py" %}

The result of running this test file shows that it `collected 4 items` as there were 4 test functions.

Then next to the test file we see an F indicating the failed test and 3 dot indicating the successful test cases. The more detailed test report helps.

At the bottom of the report you can also see that now it indicates 1 failed and 3 passed test.


```
$ pytest test_fibonacci_with_pytest_failing_separated.py
=========================================== test session starts ============================================
platform linux -- Python 3.13.7, pytest-9.0.2, pluggy-1.6.0
rootdir: /home/gabor/github/code-maven.com/python.code-maven.com
configfile: pyproject.toml
plugins: anyio-4.12.0, cov-7.0.0
collected 4 items

test_fibonacci_with_pytest_failing_separated.py F...                                                 [100%]

================================================= FAILURES =================================================
________________________________________________ test_fib_1 ________________________________________________

    def test_fib_1():
>       assert fib(1)  == 0
E       assert 1 == 0
E        +  where 1 = fib(1)

test_fibonacci_with_pytest_failing_separated.py:5: AssertionError
========================================= short test summary info ==========================================
FAILED test_fibonacci_with_pytest_failing_separated.py::test_fib_1 - assert 1 == 0
======================================= 1 failed, 3 passed in 0.09s ========================================
```

Writing those separate test functions is annoying and creates too much repetition. We'll fix that later.

For now we should just appreciate the simplicity of the test code.

Again you might feel the urge to fix the bug, but our focus is writing tests. Besides, you might be busy working on a feature or on another bug.


