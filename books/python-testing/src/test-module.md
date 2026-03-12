# Test the mymath module

Unittests are usually written in separate files.

We need to create one or more classes called `TestSomething` and inherit from [unittest.TestCase](https://docs.python.org/3/library/unittest.html#unittest.TestCase).

Inside the class there have to be one or more test-methods. Each one must start with `test_`.


{% embed include file="src/examples/testing/good/test_mymath_with_unittest.py" %}

```
$ python test_mymath_with_unittest.py
.
-------------------------------------------------
Ran 1 test in 0.000s

OK
```

The single `.` in this output indicates that we had a single test function and it was successfull.


Alternatively we can leave out the last two lines:

```python
if __name__ == '__main__':
    unittest.main()
```

And use the unittest itself to run the tests.

```
python -m unittest test_mymath_with_unittest.py
```


