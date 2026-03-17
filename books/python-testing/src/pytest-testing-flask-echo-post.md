# Pytest: testing Flask echo POST


Here we can observe how to send data to a "POST" request in a test.

In this case we used a class to write the test. I'd probably prefer the procedural tests as we saw in the previous example, but I wanted to show this as well.

We create a new attribute called "flapp" for the class, something you would not be able to do it stricter languages such as Java. We can only hope that the existing object does not have such an attribute and
we are not ruining the class.

{% embed include file="src/examples/pytest/flask/test_echo_post.py" %}
