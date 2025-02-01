---
title: "Testing random numbers in Python using mocks"
timestamp: 2018-05-24T08:30:01
tags:
  - random
  - randrange
published: true
books:
  - python
author: szabgab
archive: true
---


If there is an algorithm that uses random numbers then it is probably not possible to write a test
as the results will be based on the random number. Even in cases when that is not an issue, we usually want
to make our test repeatable.

In some cases the best solution is to mock the random number generation and provide pre-defined fake random to
the application.

This is what we are going to demonstrate here.


## Application using random

This is a very simple "application" that generates two random numbers and adds them together. I know it is very simple and stupid,
but it is better to keep it that way as the application itself is not the interesting part.

{% include file="examples/python/mock-random/app.py" %}

## Mocking random

The interseting is the test. Here we prepare a list of random numbers we would like to be retturned by the `randrange` function
and then we override the `randrange` function of the `random` object inside the `app` by an anonymous
lambda-function that will return the values one-by-one.

Once we have that setup we can call the `app.main()` and check if it returns the expecte value, which is 42 in this case.

{% include file="examples/python/mock-random/test_app.py" %}

That's it. Nothing fancy. We can prepare the random number we would like to see and then let the application think
that it uses the real random generator.


