# Use the function in the module


Before we start writing an "automated test", let's see how one could test this code "manually". In reality I see this
many times. I see people write short snippets of code to check if their real code works properly, but they
don't turn these small snippets into real tests. They don't add them to version control and they don't set
up a Continuous Integration (CI) system that would run all the tests on every push to GitHub or GitLab.

Basically the question is "How can we use the add function of the mymath module?"

The code using the module is straight forward. We import the `mymath` module. We also import the `sys` module to be able to access the command line arguments.
We take two arguments from the command line, call the `add` function, and print the result.

Then, if we would like to make sure our code works well, we can compare that result to the expected result we calculated in our head.

We try to see if `2+2=4`. Based on this everything works fine.

The `use_mymath.py` file:

{% embed include file="src/examples/testing-demo/use_mymath.py" %}


Usage:

```
python use_mymath.py 2 2
4
```



