---
title: "Fight or Flight? - dealing with real world applications in Python"
timestamp: 2017-08-30T08:30:01
tags:
  - pytest
  - mock
published: true
books:
  - python
author: szabgab
archive: true
---


You have just landed a new job as a Python developer. Your first task is simple. Make a little tweak to an existing application.
To your horror you discover the code is a mess written in the past 10 years by many different people who have just started their career as Python programmers.
They all have already move on. They left behind the code, but it has no tests and no documentation. Oh and by the way, the company depends on the application.
What do you do now? Fight or flight? In this talk you will hear about a couple of ways to fight with such a beast.


<iframe width="840" height="480" src="https://www.youtube.com/embed/3DVmalYSN0s" frameborder="0" allowfullscreen></iframe>

[On PyVideo](http://pyvideo.org/pycon-israel-2016/fight-or-flight-dealing-with-real-world-applications-in-python.html)

This presentation was recorded at [PyCon Israel 2016](http://il.pycon.org/2016/)

## The ideal situation

When you join a company, or switch teams you have certain expectation about the development environment and process.
The ideal situation looks something like this:

The team uses some distributed <b>version control system</b>.  [Git](https://git-scm.com/) is your preference,
but you'd be ok with something similar as well.

The code is divided into small functions or methods with clear input and output for each function with very little, or possibly no side-effects.
If there are side effects they are well documented.

The modules and objects are loosely coupled. While this might be harder to measure than length or complexity of functions,
but circular dependencies (e.g  module A loads module B which loads module C which load module A) is likely an indication of something
problematic. If you cannot give good names to thing (e.g. you have too many variables called <b>data</b> or <b>input</b> or <b>text</b>)
that's usually also a good indication.

Microservices. Well, that's just a modern buzz-word, but the point is that if the application is separated in
clear units with clear borders, that's usually much better than a large monolithic application.

Documentation of the decisions made and the external API of each module. Many people don't like to write documentation
because of various reasons. For example they saw too much boiler-plate documentation where a large chunk of it is redundant
or irrelevant. (Who wrote the code, what changes were made, when. All this can be extracted from the version control system.)
The main purpose of the function should be clear from its name.
Others just fear their writing capabilities in English are not good enough.

You expect to have plenty of unit and integration tests together with the code covering most if not all the codebase.

You expect to have Continuous Integration (CI) system running on the code base reporting if anything gets broken.

You also expect to have a separate development environment for each developer, including your own copy of
the data. A separate testing or staging environment that is identical to the production environment even it is much smaller.

## The real situation

The real situation is however very different. There are cases where the source code lives on the production server.
There might be a script to save backup copies with time stamp (the first seeds of a home-made version control system)
but that's it. You don't have a development environment not to even mention a testing environment.

In other cases you might have a separate development environment, even a version control system,
but there is only a single central database of the production data. You have to work on that.

The functions are huge, several hundred sometimes even a few thousand lines each.
In addition they call each other in a rather unpredictable manner in many cases
creating circular dependencies of tightly coupled modules.

Here are two modules that each depends on the other:

{% include file="examples/python/fof/my_a.py" %}

{% include file="examples/python/fof/my_b.py" %}

You can run `python my_a.py` and get a response:

```
run of my_b
run of my_a
```

but the circular dependency makes it very hard to follow what's going on.

The code is full of global variables and code that touch attributes in other modules.

For example this module looks ok (except the naming):

{% include file="examples/python/fof/xb.py" %}

But then if we use it this way: 

{% include file="examples/python/fof/xa.py" %}

then it will be very difficult to understand the code. Especially in large, applications
where any piece of code might access `xb.var`.

Running `python xa.py` gives:

```
23
42
```

People might have even employed <b>monkey patching</b> to make some code
work the way they want it to work.

In most of the cases there are no tests and there is no documentation either, or if there is
it is either redundant out of date.

## The Solution

There are basically two solutions for this. Fight or Flight.

## Flight - find another workplace

If you feel the whole organization is soaked in a bad culture that won't allow for change then your best
bet might be to find another place to work. There are plenty of places that need good developers.

Just make sure you understand that the ideal situation you hope for rarely exist. In every place
you'll see entropy in action.

If this is what you decide, you don't need to read on.

Or maybe you do, so you'll know what to do when things are not so perfect.

## Fight

The real solution is to fight the situation. To start moving from the current situation towards the ideal one.
It will be a long process, but you'll learn a lot. It will bring a lot of frustrating days, you'll encounter setbacks,
but step-by-step you'll be able to improve the situation.

Both for yourself and for the company in general which is crucial.
After all if you don't think the company will benefit from your work then you probably should not
do it while getting paid.

It is also important because once you get management to understand the real value in the changes
you make it will be much easier for you to do them.

Therefore before we talk about the value this process will bring you, the developer, let's see
what does this bring to the business?

## Business Value

I think we can describe this in two points:

* Increased speed of development (reduce the time to market)
* Increased quality of the products/services

Of course when you talk to people in management you might want to provide
a more detailed explanation. A few additional points that you might mention.

* Smaller number of bugs.
* Smaller number of system crashes for given period of time.
* Reduce the time spent in QA while increasing the quality.
* Shorter development cycles.
* Elimination of the "returning bugs".
* Reduce the possibility of changes breaking old code.

Is employee satisfaction a real thing? If your company cares, then you might mention the following
points as well. If not, then these are mostly for you and for your co-workers when you talk to them.

Try to get management buy-in, but if you cannot, and you still think the company will benefit from it, do it anyway.
It is for your sanity.

## Programmer value

* Protect your code.
* Reduce the fear, uncertainty, doubt to make changes.
* Reduce the difficulty to make changes.
* Reduce the WTF/minute in the code.
* Your sanity.

I am not really sure which one might be the most convincing among these. Maybe the idea
that writing tests for the feature you add will help you protect your code from bugs caused by future changes.
Both from your own future changes and from the changes other developers might introduce
in libraries that your code uses.

I don't know about you, but when I touch an untested piece of code I get nervous. I don't know how the changes I make 
might impact the rest of the application which slows me down a lot. I spend a lot of time worrying and a lot
of time trying to figure out if my changes don't break anything. I am never sure.

## Measure your progress

Unlike developers, managers don't have a gut feeling about the code as they are too removed from it.
They need some way to measure your work. What is interesting for them, mentioned above, is the speed of development
and the quality of code.

Unfortunately in our industry we don't have really good way to estimate the length of a project. We are often off by
100-200% in our time estimate. This means that a 20% increase in development speed is still within the
"margin of error" for the estimation of the project. That's very hard to show. Especially as the projects we do
have a lot of differences and thus it is hard to compare them.

Number of bugs might be a better indication, but that too requires some way to compare projects. Having
1 bug in an implementation of FizzBuzz is much worse than having 100 bugs in the implementation
of a flight management application, but having any of those 100 bugs can have a much worse impact.

You probably won't be able to properly measure any of these.
So we have to find other ways to measure our progress.

There are a number of other ways, that don't have a clear and direct impact on the business,
but they are measurable and provide some indication that we are in the right track.

* Code complexity.
* Test coverage  (which is probably 0 when you start).
* Standards or "best practices" compliance.
* Execution time, if relevant.
* Number of open tickets.

## Version Control System: Git

If the company does not have it yet, then the very first thing you need to do is to set up some kind of a version control system.
It will help you make changes to the code and make it easy to go back to earlier version if you break something.
It will also help you notice if someone else has changed the code.

If the company already has a version control system, they might have made the development process cumbersome.
For example they might require a ticket in the bug tracking system to be opened and signed by a manager for each change.
This usually means people will tend to wait with their commit till "everything is finished" which eliminates one of the most
valuable aspects of a version control system. Having you own version control system will allow you to make lots of small commits and
then, when you are done you can commit to the official VCS of the company.

[Git](https://git-scm.com/) is great for this as it does not need a server.

Of course if the official VCS is Git or something as flexible as Git, then you don't need this extra work.

## virtualenv

[virtualenv](https://pypi.python.org/pypi/virtualenv) allows you to create an isolated environment for your Python code.
This will allow you to install packages you might need for testing without bothering others.

## Write tests

Use one of the test frameworks of Python.

[doctest](https://docs.python.org/2/library/doctest.html) and 
[unittest](https://docs.python.org/2/library/unittest.html)
(and [unittest2](https://pypi.python.org/pypi/unittest2)) come with the installation
of Python.

[nose](https://pypi.python.org/pypi/nose/) is more powerful but it is not in favor any more.

These days [pytest](http://pytest.org/) seems to be the most recommended testing framework.

It does not really matter which one you start using. As a new programmer on this team you'll have to learn a lot
about the code-base and the challenges it imposes for writing tests.

The more important question though is what kind of tests you should be writing?

People tend to use all kinds of magic words for various aspects of testing. I'd just point at two. OK maybe three.

## Regression Test

There is no such thing as "writing regression test".
Every test becomes a regression test when you run it more than once.

That's where the real value of tests are.

## Integration or unit tests ?

That's a much more reasonable question, but the distinction is far from clear.

In the ideal case, a unit test checks the behavior of a single function. It should not depend on
the behavior of the functions called by the "function under test".

An "integration test" on the other hand would test how various subsystems work together.

In reality, however these can be seen as two extremes of a wide range of possible test.

They don't differ from each other much. They all have the simple equation of


<b>Input + Action == Expected result</b>


Or possible more correctly:


<b>Input + Action == Expected result + bugs</b>

In other words <b>"Integrations tests"</b> are the same as <b>"unit tests"</b>, just the units are bigger.

Moreover in spaghetti code every unit test is also an integration tests as all the units are tightly "integrated".

In a nutshell, don't fret about the naming. Especially not at the beginning.
But be prepared to constantly refactor your tests as well.

In this article I don't provide a deep tutorial to testing Python code, but let's just see a simple example.

## First simple test

We have a module called `my_calc.py` that has a function called `sum`.
We can observe its behavior with the following code:

{% include file="examples/python/fof/use_my_calc.py" %}

Some people will actually write such examples while developing code to observe the behavior of their new code.
Then they will either discard it or let it lay around without turning them into proper test scripts. It is quite unfortunate
because with little investment they could have converted it to long-lasting test.

In other words, they have paid the price of writing the tests without reaping the real benefits of it down the road
that they can execute the tests thousands of times.

{% include file="examples/python/fof/test_my_calc.py" %}

We can easily run the test script and if everything works fine we get a report that looks like this:

```bash
$ py.test test_my_calc.py 
============================================ test session starts =============================================
platform linux2 -- Python 2.7.9, pytest-2.9.1, py-1.4.31, pluggy-0.3.1
rootdir: /vagrant/code-maven.com/examples/python/fof, inifile: 
collected 1 items 

test_my_calc.py .

========================================== 1 passed in 0.10 seconds ==========================================
```

If on the other hand something is broken we get results like this:

```bash
$ py.test test_my_calc.py 
============================================ test session starts =============================================
platform linux2 -- Python 2.7.9, pytest-2.9.1, py-1.4.31, pluggy-0.3.1
rootdir: /vagrant/code-maven.com/examples/python/fof, inifile: 
collected 1 items 

test_my_calc.py F

================================================== FAILURES ==================================================
________________________________________________ test_mycalc _________________________________________________

    def test_mycalc():
        assert(my_calc.sum(2, 3) == 5)
>       assert(my_calc.sum(2, 3, 4) == 9)
E       assert 5 == 9
E        +  where 5 = <function sum at 0xb6cef79c>(2, 3, 4)
E        +    where <function sum at 0xb6cef79c> = my_calc.sum

test_my_calc.py:6: AssertionError
========================================== 1 failed in 0.30 seconds ==========================================
```

Just in case you'd like to try it, the actual code looks like this:

{% include file="examples/python/fof/my_calc.py" %}

## Continuous Integration

Once you have any tests it is time to set up some kind of Continuous Integration system. You can pick one of the
ready made CI systems such as [Jenkins](https://en.wikipedia.org/wiki/Jenkins_%28software%29),
[Buildbot](https://en.wikipedia.org/wiki/Buildbot), but I think I'd just start
with a simple cron-job and a few lines of Python code to fetch the latest revision of the code, run the tests
and send me an e-mail if something got broken.

This too will have to improve with time, but most likely the system you need to deal with is so specific to the company
that you'll have a lot of work setting up either of those CI systems.

## Mocking

Writing test for simple stand alone function is easy, but your situation will probably not allow that.
The code you have to deal with have a lot of interdependencies. Functions calling each other. Possibly even in a circular manner.
That's where <b>Mocking</b> or its nastier cousin <b>Monkey Patching</b> can help.

Mocking is a totally legitimate technique while testing. Especially if you have to deal with some <b>External services</b>.
In that case you don't want to hit the external API every time you run the test and you don't want to make your test depend
on the current availability of that external API or service. For example at one of my clients they had an issue with a test randomly failing
as their code, that was using some feature on Facebook got a random captcha. This taught the developers to accept that
"this test sometimes fails" which late become "some tests fail".
This is a horrible situation because it means we won't notice when the code starts to fail due to a real problem.

In addition, having a mock for this external interface allows us to easily test how our code behaves when that external service is not available
or when it returns incorrect responses. Something would be hard to test with the real service.

Another case if you would like to write <b>"pure unit tests"</b>. In that case you might want to mock all the functions called
by the "function under test".

The case that might be most relevant to our situation is however, if we have to deal with <b>complex, interdependent functions</b>.
In that case we might have no choice but to fake the behavior of some of the functions, a whole subsystem, or even the database
in order to have a <b>controlled environment</b> for our tests.

Let's see two such cases:

## Mocking a function

In the first case we have a module, cleverly named <b>library.py</b> in which there is a `main`
function and a `helper` function. While both of these functions are quite banal, try to imagine that both of
them are several hundred lines long and do a lot of complex stuff.

However, as you can see, the helper function has a fault. It will randomly throw an exception.
When `unit`-testing the `main` function we don't want to deal with the problems the helper function has
we would like to assume that it behaves correctly.

{% include file="examples/python/fof/library.py" %}

That's where we can use the [mock](https://pypi.python.org/pypi/mock) module. Basically we replace the `helper`
function by the new `my_helper` for the duration of the tests. This fake helper function has hard-coded return values for every
input that will be encountered during our test (which, in our case is the number 2).

{% include file="examples/python/fof/test_library.py" %}

This allows us to write as many test as we want and control the results we receive from the helper function.

The difficulty here might be if we have a number of such "helper" function and if we don't know what to expect from them.

## Mocking print

Another really problematic case is when the function we are trying to test has side-effect. Chief among those side-effects
is printing to the screen. We would like to capture the output and see if it is what we expect.

A simplified example:

{% include file="examples/python/fof/echo_calc.py" %}

Here is how we can use this module:

{% include file="examples/python/fof/use_echo_calc.py" %}

Here is how we can test it:

{% include file="examples/python/fof/test_echo_calc.py" %}

This way we mock the `print` statement of Python 2
and collect the output in a string that we can retrieve using the
`getvalue` method.

## Get others on board

Once you set up your testing environment and started to write tests it is time to expand your reach.
A couple of ideas what to do:

* Lead by example. - Write lots of tests for the code you write or change.
* Show how tests saved you time.
* Offer to write tests for their code.
* Introduce code-review, but ask the other developers to review your code before you review theirs.

## Resources

Some of the resources I've used for this talk and article that I recommend you read:

* [Best Coding Practices](https://en.wikipedia.org/wiki/Best_coding_practices)
* [How to motivate co-workers to write unit-tests?](http://programmers.stackexchange.com/questions/157287/how-to-motivate-co-workers-to-write-unit-tests)
* [How do you persuade others to write unit tests?](http://stackoverflow.com/questions/416231/how-do-you-persuade-others-to-write-unit-tests)
* [Python Testing blogs and podcast by Brian Okken](http://pythontesting.net/)
* [Writing Great Unit Tests: Best and Worst Practices](http://blog.stevensanderson.com/2009/08/24/writing-great-unit-tests-best-and-worst-practises/)

