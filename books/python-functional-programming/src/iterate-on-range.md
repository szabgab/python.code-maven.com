# range

The `range` function returns something, that we can use in a **for-in** loop to iterate over and we'll get the expected numbers.

However, if we print the value that we got back from the `range` function it looks strange. It looks exactly as we called it.
This is the representation of the `range` object.

Unlike in Python 2, here in Python 3 the `range` function does **not** return a list of numbers.
It returns an object that allows us to iterate over the numbers, but it does not hold the numbers.

{% embed include file="src/examples/functional/iterable_range.py" %}

**Output:**

{% embed include file="src/examples/functional/iterable_range.out" %}

`range` is interesting. We are going to take a closer look in the next few pages.

