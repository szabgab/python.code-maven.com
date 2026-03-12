# Doctest for bad module

{% embed include file="src/examples/testing/bad/mymath.py" %}

```
python3 -m doctest -v src/examples/testing/bad/mymath.py
```


{% embed include file="src/examples/testing/failure/mymath.py" %}

```
python3 -m doctest -v src/examples/testing/failure/mymath.py
```
