# Manually test the `mymath` module

We can create a command line application using the module

{% embed include file="src/examples/testing/good/run_mymath.py" %}

And then we can ask our QA team to try it:

```
$ python src/examples/testing/good/run_mymath.py add 19 23
42
$ python src/examples/testing/good/run_mymath.py div 19 23
0.8260869565217391
```

