# Testing demo: doctest

The first way we are going to look at is using the "doctest" module. It is a very nice tool that allows us to test our code
and to also verify that our documentation is aligned with the code.
In addition to that, doctest is a standard module. It comes with every installation of Python so you don't need
to worry about installation.

The big drawback is that it is not really useful for anything complex.

Anyway, how does it work?

In Python if you add a string immediately after the declaration of the function - meaning the line immediately after the "def" statement -
that string becomes the documentation of the function. It can be a one-line string using regular quotes or a multi-line string using triple-quotes.

In the documentation you can write free text and you can also write examples as if one was using the interactive shell of Python.
For these examples we have code snippets preceded with 3 greater-than signs `>>>`, the prompt of the in Python interactive shell. The lines immediately
after that contain the result that you'd see if you actually typed in the expression into the interactive shell.

Having such examples in the documentation is great as it makes it easy for most programmers to see how the specific function is expect to be called and what results
it is expected to give. But how can we, the authors of the code and the documentation make sure that the examples are really correct?
How can we make sure that we'll update the examples if the function changes its behaviour and thus it changes the results.
(e.g. it becomes more precize having more digits after the decimal point)

## Doctest

Doctest will read your source code, look at all the functions you have and for each function it will look at the documentation of the function.
If in the documentation it sees examples staring with 3 greater-than signs `>>>` then it will take the content of that line as code to be executed
and it will take the next line as the expected result. Doctest will execute each code snippet and compare it with the expected results.
Effectively checking if the examples in your documentation and the implementation are aligned.

Of course it cannot check if that is really the correct answer. If you make the same error both in the code and in the example then it will still think
that everything is fine, but at leas now it might be easier for a user to point out the mistake as it will be seen in the documentation already. No need
to read the source code.

We can run doctest in the following way: `python -m doctest mymath.py`. If all the tests pass, then this execution will print nothing.
This lack of positive feedback is a bit strange, but that's how it work. You might want to check the so-called "exit code" of the execution.
On Unix systems such as Linux and macOS, you'd inspect the `$?` environment variable while on MS Windows you need to inspect the `%ERRORLEVEL%` variable.
On all of these systems you can use the `echo` command to inspect the variables. In either case 0 indicates success and any other number indicates failure.

The new `mymath.py` file:

{% embed include file="src/examples/testing-demo/doctest_first/mymath.py" %}

Run the tests and check the exit code on Linux or macOS:

```
$ python -m doctest mymath.py
$ echo $?
0
```

Run the tests and check the exit code on MS Windows:

```
> python -m doctest mymath.py
> echo %ERRORLEVEL%
0
```

Once you see this you might conclude that you have tested the `add` function (for now let's forget about the `multiple` function) and you might release you "application".
However soon someone will come complaining that it does not work correctly in all the cases. If you are lucky they will even provide you with at least one pair of numbers
where the result is incorrect.

---

* doctest
* $?
* %ERRORLEVEL%



