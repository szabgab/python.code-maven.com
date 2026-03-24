# wrapper

We created a wrapper function called `wrap` that receives a function as a parameter.

Inside it creates a new funcion called `new_function`. (I am really not very creative with names.)
The return value of the `wrap` function is this `new_function.

The `new_function` first prints something on the screen and saves the current time.

Then it calls the function that was received as a parameter.

Then gets the current time again and prints the elapsed time.

That's the `new_function`

On the next pages we'll see how we can use this function.

{% embed include file="src/examples/decorators/wrapper.py" %}
