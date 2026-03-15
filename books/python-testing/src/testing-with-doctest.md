# Testing with doctest

[doctest](https://docs.python.org/3/library/doctest.html) allows us to verify that the implementation of our functions and the example we provide in their documentation are aligned.

For every Python function we can add an string as the first thing in the body of the function. (We usually use tripple quotes for this as we are including several lines. In this documentation we can include both free text and examples that look as if we were using the interactive shell.

That is we'll include a prompt `>>>`, after the prompt we'll write a call to the function. Underneath we'll show the values the function is supposed to return.

Doctest will read our source code. It will read our functions and their documentation.

It will extract the examples from the documentation. Run the function as shown after the `>>>` prompt and compare the results to what can be found next.

This is sometimes referred to as "literate testing" or "executable documentation".


