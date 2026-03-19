# Pytest: Mocking slow external API call - manually replace function

We can create a function (we call it `mocked_remote_compute`) that we'll use to
replace the remote API call. However, ee don't need to re-implement the whole complex algorithm of
computing the square of numbers provided by the remote service.
It is enough that we hard-code the responses we should get from the API for the values we are going to use in the tests.

Then we can manuall monkey-patch the method in the `externalapi` library.

{% embed include file="src/examples/pytest/external-api/test_mymath.py" %}

```
time pytest test_mymath.py
```
