# A programming language


* Built-in words: print, len, type, def, ...
* [Literal values: numbers, strings](https://en.wikipedia.org/wiki/Literal_(computer_programming))
* [Operators: + - * = , ; ...](https://en.wikipedia.org/wiki/Operator_(computer_programming))
* [Grammar (syntax)](https://en.wikipedia.org/wiki/Syntax_(programming_languages))
* User-created words: variables, functions, classes, ...

---

## Variables and data types

Programming is about manipulating data. So in a programming language we need to somehow store data. For this we have variables. Each variable hold some type of data for examples:

```python
temperature = 30.2    # This is a variable holding a single numeric value, more specifically a floating point number (`float`).
grade  = 93          # This variable hold a single integer (`int`) number
name = "Foo Bar"     # This variable holds a string (`str`), a series of characters.
found = True         # This is a boolean (`bool`) value that can be either `True` or `False`.

planets = ["Mercury", "Venus", "Earth", "Mars"]
    # This variable holds a `list` of strings
grades = [67, 83, 92. 74]
    # A list of integers


grades = {
    "Jane": 89,
    "Joe":  63,
    "Mary": 75,
    "Peter": 100,
}
    # A dictionary (`dict`) that holds key-value pairs. This one is mapping strings to integers.

point = (10, 23)
    # A `tuple` (an immutable list) of two integers representing a point.


colors = {"red", "green", "blue", "orange", "white", "black"}
    # A `set` of strings representing colors.
```

When you would like to represent a value you can do that in many ways. You will need to pick the "best one for the circumstances".
Which is a nice way to say I don't want to get into the details now, but we'll talk about it later and you'll figure it out.


For example if we would like to represent a given time we can do it as

* a string
* a tuple
* a dictionary
* a `datetime` object
* ...

Each representation has advantages and disadvantages.

```
current_time = "2025.08.20 07:23:17"
current_time = (2025, 8, 20, 7, 23, 17)
current_time = {
   "year": 2025,
   "month": 8,
   "day": 20,
   "hour": 7,
   "minute": 23,
   "second": 17,
}
current_time = datetime.fromisoformat("2025-08-20T07:23:17")
```

## IO Input/Output

A program somehow needs to be able to receive the data (input) and it somehow needs to give results back to the user (output).
So we need to learn how to handle input and output.

Input can come from
* keyboard
* mouse
* files
* camera
* microphone
* network ("the Internet")
* ...

Output can go to
* Screen
* files
* printer
* network ("the Internet")
* ...

## Operations on the data

Throughout the program we have various operations on the data, for example we might have "mathematical" operations on a number. These can be complex mathematical thing, though usually they are very simple. e.g. counting how many times the word "cake" appears in a text.

On variables holding other data-type we might have different operations. For example we can add a new key-value pair to a dictionary. We might remove a pair. We might change the value of a specific key. etc.


## Control flow

The process in which a program manipulates the data is called an "algorithm" and it is expressed with control flow.

To express a conditional statement and thus to execute some operations if the condition is met we can use `if, else, elif`

* `if`
* `else`
* `elif`

To go over a list of values or just to repeat some operation multiple times we can use loops and loop-controls:

* `for in`
* `while`
* `break`
* `continue`

There are some other tools used to control the flow of operations

* `exit`
* `return`

## Error handling

We need to think about problems. What if the input or in general the data contains unreasonable values? e.g. we were expecting a number but we got a string.
We expected a positive number but we got a negative one. etc. How can we handle this.


## Modularization

In order to make our code easier to read and maintain and to make our code reusable we can group together certain operations and wrap them in a function defined with the `def` keyword.
We can also move these functions to separate files, called modules.

## Testing / Verification

An integral part of programming is making sure that your program runs correctly and in general behaves as expected. Both now and later after you make some improvements to it.




