# Pytest - passing test for the Fibonacci function


{% embed include file="src/examples/testing/bad/test_fibonacci_with_pytest.py" %}

We can run the tests in two different ways. The regular would be to type in `pytest` and the name of the test file.
In some setups this might not work and then we can also run `python -m pytest` and the name of the test file.

```
pytest test_mymath.py
python -m pytest test_mymath.py
```

``
$ pytest test_fibonacci_with_pytest.py
=========================================== test session starts ============================================
platform linux -- Python 3.13.7, pytest-9.0.2, pluggy-1.6.0
rootdir: /home/gabor/github/code-maven.com/python.code-maven.com
configfile: pyproject.toml
plugins: anyio-4.12.0, cov-7.0.0
collected 1 item

test_fibonacci_with_pytest.py .                                                                      [100%]

============================================ 1 passed in 0.07s =============================================
```

The top of the output shows some information about the environment, (version numbers, plugins) then "collected" tells us how many test-cases were found by pytest. Each test function is one test case.

Then we see the name of the test file and a single dot indicating that there was one test-case and it was successful.

After the test run we could also see the exit code of the program by typing in `echo $?` on Linux or Mac or `echo %ERRORLEVEL%` on Windows.

```
$ echo $?
0
```

```
> echo %ERRORLEVEL%
0
```


