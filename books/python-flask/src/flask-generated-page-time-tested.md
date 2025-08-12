# Flask generated page - time tested

How can we test this application?

We have two pages and need to test both of them. One is a static page. That will be relatively easy, but how can we test the generated page that always changes?

We'll get to that, but first, how should we organize the tests of the two separate pages?

* We could put all the tests in a single test-function.
* We could have two test-functions in the same test-file.
* We could have two test-functions in two separate test-files.

Putting them in separate functions allows us to run them separately. It also means that if one fails the other might still pass.
Usually we put independent test-cases in separate functions.

Because our application is still very small, putting the tests in two separate files seems like an overkill.

So we are going to have a single test file with two test-functions.

The `test_home` function is relatively straight forward. We get the main page and then we check the status-code and the exact match for the content.

The `test_time` function is trickier. We can't check an exact match as the timestamp will be different every time we run the code. We could **mock**
the time and for a real application I'd probably do that, but for now we are looking for a simpler solution.
So instead of an exact match we use a Regular Expression (a regexp) to check if the result looks like a number we would expect.

You can run the tests by running `pytest`.

## The test:

{% embed include file="src/examples/flask/time/test_app.py" %}

## To run it

```
pytest
```


