---
title: "Testing interval-timer, a Python module"
timestamp: 2022-10-04T11:30:01
tags:
  - pytest
  - time
types:
  - screencast
published: true
books:
  - testing
  - python
author: szabgab
archive: true
show_related: true
---


[interval-timer](https://github.com/morefigs/interval-timer) is a new Python module that will make it easy to ensure
that your jobs are executed at a fix interval as well as possible. Meaning that if you'd like to run some function every 1 second
then if the function takes only 0.4 seconds the system will wait 0.6 second to run the next iteration, but if the task takes 1.2
seconds then it will run immediately as it was due to run after 1 second.


{% youtube id="SNvyDq8g7S4" file="python-testing-interval-timer.mp4" %}

There are several example in the Git repository of the project, but there were no tests and there was no CI system configured.
So I figured I could write some tests first.

There are two ways to write tests for a module that handles time.

One is to use the real time of the computer, the other is to fake the time using mocking (aka. monkeypatching).

In this case I decided to use implement the tests using the real clock of the computer.
It means the tests will take more time to run as they really need to wait the expected amount of time,
but there will be no funny business with the time handling.

As I implemented the tests I found something that felt to be off. There is a flag that indicates for each iteration
if the iteration has missed its expected scheduled time. Right now it seems to indicate if the scheduled task
has started only after it should have been already finished (and a new task should have been started).
So I opened an [issue](https://github.com/morefigs/interval-timer/issues).

After quite a lot of fiddleing with the tests I came up with the following way to describe a tests-case:

```
    # start   0     1     2     3      4     5     6
    starts = [0,    1,    2.2,  3.5,   5.1,  5.6,  6]
    misses = [F,    F,    F,    F,     T,    F,    F]
    sleeps = [0.5,  1.2,  1.3,  1.6,   0.5,  0.2,  0.1]

```

* The 1st line which is commented out indicates the seconds when each iteration should start (assuminig we schedule them 1 second apart)
* The 2nd line show at which second the iteration is expected to really start given the time spent in the iteration that is listed in the last row.
* The 3rd line indicates if the "missed" flag should be False or True. I used this abbreviated variables to make the row shorter.
* The 4th row indicates how much each iteration will last.

So in effect the last row, the "sleeps" is what could be considered the input of the test and lines 2 and 3 are the expected output.
Line 1 was only added to help me think through the expected values.

So here is what we see - read column-by-colum:

<ol>
   <li>1st column: The 1st iteration startes at 0 second and so it has not missed its schedule (row 3 is F). The iteration takes 0.5 seconds.</li>
   <li>2nd column: The first iteration ended at 0.5, but is should start only after 1 second (indicated by the 1st line) so we expect it to start 1 second after the test starts (row 2). It has not missed it schedule so row 3 is F. The work in the iteration takes 1.2 second.</li>
   <li>3rd colum:  The 2nd iteration started at 1, lasts 1.2 so ends at 2.2. The 3rd iteration was expected to start at 2, so there is no reason to wait and thus the 3rd iteration is expected to start at 2.2 and in the current behavior to be marked as not missed. The work in this iteration lasts 1.3 seconds.</li>
   <li>4th column: The 3rd iteration started at 2.2 took 1.3 so ends at 3.5. The 4th iteration was expected to start at 3, so there is no reason to wait and thus the 4th iteration is expected to start at 3.5 and in the current behavior to be marked as not missed. The work in this iteration lasts 1.6 seconds.</li>
   <li>5th column: The 4th iteration started at 3.5 took 1.6 so ends at 5.1 The 5th iteration was expected to start at 4, so there is no reason to wait and thus the 5th iteration is expected to start at 5.1 and in the current behavior to be marked as <b>missed</b>. The work in this iteration lasts 0.5 seconds.</li>
   <li>6th column: The 5th iteration started at 5.1 took 0.5 so ends at 5.6 The 6th iteration was expected to start at 5, so there is no reason to wait and thus the 6th iteration is expected to start at 5.6 and in the current behavior to be marked as <b>not missed</b>. The work in this iteration lasts 0.2 seconds.</li>
   <li>7th column: The 6th iteration started at 5.6 took 0.2 so ends at 5.8 The 7th iteration was expected to start at 6, so the system is expected to wait 0.2 seconds and the 7th iteration is expected to start at 6 and in the current behavior to be marked as <b>not missed</b>. The work in this iteration lasts 0.1 seconds.</li>
</ol>


I've included the full copy of the test file as I have submitted to be a pull-request so even if it is later changed you can take a look at it.

{% include file="examples/python/test_interval_timer.py" %}

At the top of the file you can see the definition of T and F to be used instead of <b>True</b> and <b>False</b> and a variable called <b>delta</b>.
I need this because time-related operations are never exact. After all we don't have control over what else the computer is doing. So when we verify
that the iteration was indeed started at the expected time we allow for an error of delta.

## Pytest parametrize

The tests could have been set up using the [pytest.mark.parametrize](https://code-maven.com/slides/python/pytest-with-parameters) facility as shown in the linked example,
but I felt that using this layout for the data makes it easier to understand and maintain them.


