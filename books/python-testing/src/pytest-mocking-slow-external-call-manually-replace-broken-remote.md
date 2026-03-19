# Pytest: Mocking broken external API response

How can we test the behaviour of our code on wrong response from the API?

In a way it is similar to testing our code with invalid or broken input, except the API call is initiated by our code and we don't have control over the API service.

Unless, of course, we mock it.

So in this example we made the mock returned a string instead of a number.
Our code raised a python-level exception. This is obviously not good.
Now you need to decide whether you'd like to improve the application to check the values returned by the API or expect this test to fail?

{% embed include file="src/examples/pytest/external-api/test_mymath_broken_remote.py" %}
