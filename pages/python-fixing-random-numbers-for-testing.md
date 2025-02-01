---
title: "Python: fixing random numbers for testing"
timestamp: 2019-01-25T21:30:01
tags:
  - random
  - seed
  - pytest
  - -e
  - -q
published: true
books:
  - python
author: szabgab
archive: true
---


How do you test any python code that uses the `random` module?

You might know about [mocking methods of the random module](/testing-random-numbers-in-python) and
fixing the returned values. It is good because you can exactly say what should be the (fake) random values,
but that is only reasonable if you have a very limited number of values that should be randomly generated.

If you have a need for a potentially much bigger set of random numbers you need something else.
You might have read about [repeating the same random number using seed](/repeat-the-same-random-numbers).
That's what we are going to use. We are going to fix the seed for testing.


To show how this works I've created a scrip to pick N random names from a file where each line is a name.

{% include file="examples/python/pickaname.py" %}

If you look carefully you will notice there is a bug in the code. If you have not found it yet, don't worry, that's
part of the point of testing. To find cases where our brilliant code fails our expectations.

Basically it gets a name of a file and a number on the command line and prints that many names. Without repetition.

In order to demonstrate it I've download a list of 20 names (The 10 most popular boy and girl names in some
country in some year.)

{% include file="examples/data/names.txt" %}

So what happens if we run the code?

```
$ python examples/python/pickaname.py examples/data/names.txt 3
CHLOE
HARRY
OLIVER

$ python examples/python/pickaname.py examples/data/names.txt 3
RUBY
GRACE
JACK

$ python examples/python/pickaname.py examples/data/names.txt 3
CHLOE
DANIEL
```

The first two times it worked well and returned 3 random names. The 3rd time it only returned 2 names.

If you have not noticed found the bug earlier this will probably make it a bit easier.

In any case the problem was that once the code ensures that there is no repetition, it does not try again.

Let's write a test for this code:

{% include file="examples/python/test_pickaname_1.py" %}

We run the test a few times and it is successful...

```
$ pytest test_pickaname_1.py
============================= test session starts ==============================
platform linux -- Python 3.6.7, pytest-4.0.2, py-1.7.0, pluggy-0.8.0
rootdir: /home/gabor/work/code-maven.com/examples/python, inifile:
collected 1 item

test_pickaname_1.py .                                                    [100%]

=========================== 1 passed in 0.00 seconds ===========================
```

... but at one point it fails:

```
$ pytest test_pickaname_1.py
============================= test session starts ==============================
platform linux -- Python 3.6.7, pytest-4.0.2, py-1.7.0, pluggy-0.8.0
rootdir: /home/gabor/work/code-maven.com/examples/python, inifile:
collected 1 item

test_pickaname_1.py F                                                    [100%]

=================================== FAILURES ===================================
________________________________ test_pickaname ________________________________

    def test_pickaname():
        names = pickaname.select_names('../data/names.txt', 3)
>       assert len(names) == 3
E       AssertionError: assert 2 == 3
E        +  where 2 = len(['AMELIA', 'CHLOE'])

test_pickaname_1.py:5: AssertionError
=========================== 1 failed in 0.02 seconds ===========================
(venv3) gabor@thinkpad:~/work/code-maven.com/examples/python$
```

So we can't use this test because it will randomly. We cannot even use it to
consequently show that there is an error.

That's  the nature of random.

So what can we do?

We know that the random numbers the `random` module generates are actually
<a href="">pseudo random numbers</a> and that by fixing the `seed` we will
get the exact same random values every time we run the code.

So let's try this.

{% include file="examples/python/test_pickaname_2.py" %}

42 is just an arbitrary number I picked.

If we run this test it will succeed. But what happens if we run it several time?
How many time do we have to run to conclude that it will always succeed.

We can print the actual names picked by the code that observe they are always the same.

```
$ pytest test_pickaname_2.py  -sq
['GRACE', 'OLIVIA', 'AMELIA']
.
1 passed in 0.00 seconds
```

Here `-s` told pytest to to print the output of the test script to the console.
I also used `-q` to tell pytest to be as silent as it can be so it is easier to see
the results.

Run the same code several times and observe that not only the number of names remains 3,
we also get the exact same names every time.


OK, so we have a test that reliably checks one random case. How can we reproduce the case
when the function only returns 2 names.

For that we'll have to pick another number.

I had to dig a bit, actually I wrote a look that checked the whole numbers from 0 as seeds and found that using the
number 2 as seed will reliably make the function return only two elements. (What a coincidence.)
I could use that number, but I am sure some reader of my code down the road might think that the number of elements
is somehow 2 because the seed was 2 so I looked for another number and found that 11 caused the same issue, albeit
returning two different names.

So here is a test case that will reliably fail.

{% include file="examples/python/test_pickaname_3.py" %}

That's it, until someone fixes the function.

## Going further

We could go further and test that the returned names are exactly the same on every run. This might be a good idea
if we had some random-based algorithm that should get us some real results.

## Conclusion

It can be really useful to fix the `seed` when testing some code that uses random numbers.


