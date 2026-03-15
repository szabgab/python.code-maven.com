# Pytest - passing test for the Fibonacci function


{% embed include file="src/examples/testing/bad/test_fibonacci_with_pytest.py" %}

We can run the tests in two different ways. The regular would be to type in `pytest` and the name of the test file.
In some setups this might not work and then we can also run `python -m pytest` and the name of the test file.

```
pytest test_fibonacci_with_pytest.py
python -m pytest test_fibonacci_with_pytest.py
```

{% embed include file="src/examples/testing/bad/test_fibonacci_with_pytest.out" %}

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


