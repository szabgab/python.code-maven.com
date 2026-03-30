# filehandle

We can iterate over a filehandle. On each iteration we'll get one line from the file.

{% embed include file="src/examples/functional/iterable_fh.py" %}

Running this program will print itself.

We can also print the filehandle: `print(fh)`, but the output will be:

```
<_io.TextIOWrapper name='iterable_fh.py' mode='r' encoding='UTF-8'>
```

not the content of the file.

So the "thing" that the `open` function returned is iterable, but it is different from the previous 3 types.


