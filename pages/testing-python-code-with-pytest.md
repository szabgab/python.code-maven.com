---
title: Testing Python code with pytest
timestamp: 2024-06-19T12:30:01
author: szabgab
published: true
description:
tags:
    - pytest
todo:
    - TODO
---

{% youtube id="I43eplQafcg" %}

# Notes


* [Slides](https://code-maven.com/slides/python/pytest)

* A little background about functional testing.
* How to test the [Meetup web site](https://www.meetup.com/)?
* Very complex.

* The difficulty to introduce testing late in the process.

* Start simple, test a function.
    * mymath - add two numbers
    * how to use it from another file
    * the same way we test it

* Copy paste it to multiply two numbers
    Show failure

* Fixing the code or marking the test as "expected to fail"?

* `-rx`

* Warn about running code but not verifying it with assert

* Fibonacci - exception

* Verbose `-v`
* print STDOUT `-s`
* Stop on first failure `-x`   `--maxfail 42`

