---
title: "Python helper: Let all CI jobs fail separately"
timestamp: 2022-10-09T08:20:01
tags:
  - GitHub
  - fail-fast
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


When you use a <b>matrix</b> in GitHub Actions to run your tests in different environments
(e.g. different operating system, different version of Python), there is a parameter called <b>fail-fast</b>
that controls what should happen to the jobs that have not finished yet when one job fails.

The default is <b>true</b> meaning they should be cancelled.

This usually makes sense because you already have something to fix and you don't want to waste the resources of GitHub Actions
to run many other similar jobs if one fails.

This case was different.


{% youtube id="ktVOqQxoOtw" file="python-helper-let-all-ci-jobs-fail-separately.mp4" %}

As usual I started at [PyDigger](https://pydigger.com/search/has-github-no-ci) listing all the Python packages that have a link to their
GitHub repository, but no CI configured.
I found and cloned [python-helper](https://github.com/SamuelJansen/python-helper) and ran the tests. First using <b>pytest Tests.py</b>.
That failed and I [reported it](https://github.com/SamuelJansen/python-helper/issues/1).

Soon I got a response that the tests should be run as <b>python Tests.py</b>. The author also made some changes to improve the output of the test-failures.

I did not understand why is it a good idea to have an implementation of the pytest test-runner, but I tried it as recommended. It failed that way as well.

I reported the new failure.

However, seeing the new output I was a bit surprised that the author expects the tests to pass.

This was the last line

```
 datetime.datetime.now() == DateTimeHelper.dateTimeNow() => 2022-10-09 07:07:15.742111 == 2022-10-09 07:07:15.742118
```

So, as I understand the <b>DateTimeHelper.dateTimeNow</b> function should return the same timestamp as the <b>datetime.datetime.now()</b>.

As far as I understand this can only happen in two cases:

* If either the computer is very-very-very fast so the two calls happen in less than 0.000001 second. Even then the test can be flaky.
* The time is mocked

So is the authors machine that much faster than mine? Should I be envy?

## Add GitHub Actions to run the tests

I've added a GitHub Actions configuration file to run the tests using <b>python Tests.py</b> and pushed it out to my forked version of the repository.

The tests failures looked like this:

![](static/img/python-helper-ci-cancelled.png)

that is, they failed on Ubuntu Linux on two different versions of Python and were cancelled on OSX and Windows.

I thought it would be more useful for the author to see all the failing results so I added the configuration option to GitHub Actions:

```
      fail-fast: false
```

This time the results looked like this:

![](static/img/python-helper-ci-failed.png)

That is, the tests failed on all 3 version of Python both on Ubuntu Linux and on OSX.
However, I was surprised to see that they passed on all 3 versions of Python when running on MS Windows.

So in this case it was quite useful to see that the results are different depending on the platforms.

Given that the test pass on the machine of the authors I assume they use MS Windows or, as I wrote earlier, a machine much faster than mine.

Given that we are talking about timestamps, I am now wondering, is <b>datetime.datetime.now</b> less precise on Windows?
Was that the reason for the difference in test-results?

Anyway, here is the configuration file I added as <b>.github/workflows/ci.yml</b>

{% include file="examples/python-helper-ci.yml" %}


## Quick action

By the time I finished writing this post the author already merged my pull-request and fixed the tests for Ubuntu.
As I can see he is now working on the fix for OSX.

I love the quick action by the author. It encourages me very much to continue checking Open Source projects, opening issues and sending Pull-Requests.

