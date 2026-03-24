# Returning a closure

In this example the internally created function depends on a parameter the `create_incrementer` received.
This parameter will go out of scope at the end of the `create_incrementer` function, but because it is used inside the internal function which was returned the caller, inside it will stay alive.

This is called a closure and it can be extremly useful in certain cases.

{% embed include file="src/examples/decorators/incrementer.py" %}

{% embed include file="src/examples/decorators/test_incrementer.py" %}


