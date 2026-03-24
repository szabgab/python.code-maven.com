# Decorator

* A function that changes the behaviour of other functions.
* The input of a decorator is a function.
* The returned value of a decorator is a modified version of the same function.


Normally a decorator is used with the `@` prefix just above the declaration of a function:

```python
from some_module import some_decorator

@some_decorator
def f(...):
    ...
```

However, that syntax is only to make it look nice. In reality it is basically the same as this code:

```python
def f(...):
    ...

f = some_decorator(f)
```

