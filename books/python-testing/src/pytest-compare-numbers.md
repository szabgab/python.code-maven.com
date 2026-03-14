# PyTest: compare numbers

{% embed include file="src/examples/pytest/test_number_equal.py" %}

```
$ pytest -q test_number_equal.py
```

{% embed include file="src/examples/pytest/test_number_equal.out" %}

In this case it is easy to see what is the difference between the expected and the actual value.

Well except that pytest does not have a notion of which side is the expected side and which is the actual value,
but you can clearly see if from the code.

