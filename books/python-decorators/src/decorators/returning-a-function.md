# Returning a new function from a function

As we can pass a function as a parameter to a function, we can also return
a function from another one.

Combining it with the previouse example, iniside our `create_function` we define a new function. Normally it only exists inside the `create_function`, but we can return it to the caller and then it stays around.

{% embed include file="src/examples/decorators/return_function.py" %}

{% embed include file="src/examples/decorators/return_function.out" %}


