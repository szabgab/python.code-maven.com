# Application that prints to STDOUT and STDERR

A very simple function that print to the screen. How can we test this?

An even wors situation is when a function both does some (computational) work and prints to the screen, something not ideal from a design point of view. However even if the sole job of a function is to print to the screen, we still need a way to test it.

{% embed include file="src/examples/pytest/greet.py" %}

We can write a separate program that uses this function and "eyeball" the result, but we can do better.

{% embed include file="src/examples/pytest/use_greet.py" %}

**Output:**

{% embed include file="src/examples/pytest/use_greet.out" %}


