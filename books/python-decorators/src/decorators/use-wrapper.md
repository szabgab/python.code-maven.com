# Use wrapper as a function

We can take any arbirary fuction, for example the `myfunc`, pass it to the `wrap` function
and assign the returned value back to the `myfunc` name. This will replace the original myfunc by one returned by the `wrap` function.

So far `myfunc` was not called.

Then we call the new `myfunc`.

This will basically call the `new_function` that will call the original `myfunc`.

We did not use any "decoration" for this. Just plain function calls.

{% embed include file="src/examples/decorators/use_wrapper.py" %}

```
$ python use_wrapper.py

start new 'myfunc'
myfunc started
myfunc ended
end new 'myfunc' 1.0002148151397705
```
