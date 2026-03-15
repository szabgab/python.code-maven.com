# PyTest: compare long strings

However, comparing long strings would be extremely difficult for us.

Luckily pytest will point us to the first character that differs.

{% embed include file="src/examples/pytest/test_long_strings.py" %}

```
$ pytest -q test_long_strings.py
```


**Output:**

{% embed include file="src/examples/pytest/test_long_strings.out" %}


