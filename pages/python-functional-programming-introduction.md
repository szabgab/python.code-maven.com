---
title: "Python Functional Programming: Introduction"
timestamp: 2022-11-25T10:00:01
tags:
  - Python
published: true
books:
  - python
author: szabgab
types:
  - screencast
archive: true
show_related: true
---


In this series we are going to take a look at Functional programming in Python.

I am not trying to convince you to write in Functional programming. I definitely don't want you to write everything in functional programming style.
Partially because probably you cannot.

If you really want to explore pure functional programming then pick up one of the purely functional programming language.

Instead of that I'd like to show you that you are probably already using various features of Python that are more aligned with the
functional programming paradigm.

I am going to show you various further tools to improve that.


{% youtube id="bVh79psbqDE" file="english-python-functional-programming-introduction.mkv" %}

## Programming paradigms


There are a number of [Programming paradigms](/slides/python/programming-paradigms) that you might be familiar with.

On the [Programming paradigms](https://en.wikipedia.org/wiki/Programming_paradigm) page of Wikipedia you will see one of the
ways to categorize programming languages.

There is [imperative](https://en.wikipedia.org/wiki/Imperative_programming) programming and underneath there are
[procedural programming](https://en.wikipedia.org/wiki/Procedural_programming) and [Object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming).


Then there are [functional](https://en.wikipedia.org/wiki/Functional_programming), [logic](https://en.wikipedia.org/wiki/Logic_programming), and <a
href="https://en.wikipedia.org/wiki/Mathematical_optimization">mathematical programming</a>. Since I recorded that video people also added
[reactive programming](https://en.wikipedia.org/wiki/Reactive_programming) to this list.

There are, of course, other ways to categorize programming paradigms.

Basically <b>procedural programming</b> is what we are used to: just writing one statement after the other.

<b>Object Oriented programming</b> is when you create classes and call methods.

These are both supported by Python so you can write in both paradigms in Python.

Then there is the <b>Functional programming</b> that is also partially supported by Python. That's what we are going to focus on.

One more to mention is the [Declarative programming](https://en.wikipedia.org/wiki/Declarative_programming) paradigm.
The language using this paradigm that you are most familiar with is probably [SQL](https://en.wikipedia.org/wiki/SQL).



## What is Functional Programming?

[Functional programming](https://code-maven.com/slides/python/functional-programming) has several features:


<b>immutability</b> - Python has a number of data-type that are immutable. For example strings and tuples.

The problem with variable is that they change. Well, they name indicates that, but apparently it is also a source of a lot of bugs.

Instead of changing the content of the immutable data-types Python allows you to replace the content of a variable with the new value.

<b>Separation of data and functions</b> is quite the opposite to what Object Oriented programming says. In OOP you have a class that has
both attributes (data) and methods (functionality).

<b>Pure functions</b> are function without side-effects that given the same input will always return the same result. (So no counter, no print).

<b>First-class functions</b> (you can assign function to another name and you can pass function to other functions and return them as well. We can also manipulate functions)
You can do all this in Python.

<b>Higher order functions</b> a functions that either takes a function as a parameter or returns a function as a parameter.

In python you can write a function that will receive a function as its parameter and returns another function based on the one that was just passed in.
Basically this is what decorators do in Python.

We are going to talk about such features of Python in the following episodes.
