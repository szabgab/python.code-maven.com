---
title: "Make it easy to setup CI environment - python (once-utils)"
timestamp: 2022-10-08T21:30:01
tags:
  - GitHub
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



While trying to enable GitHub Actions CI to this small Python package called [once-utils](https://github.com/szabgab/once-utils/) I bumped into two issues:

1. Some of the tests required <b>gradle</b> to be installed, somehting that seemed arbitrary and not very straigh forward to have.

2. There was no easy way to install all the dependencies. (No requirements.txt file)

See the [PyDigger stats page](https://pydigger.com/stats) for more modules that don't have Continuous Integration.


{% youtube id="aSGAqGyg_KY" file="python-make-it-easy-to-setup-ci-environment-python-once-utils.mp4" %}

As I did not want to fiddle with the installation of gradle I decided that instead of running <b>pytest</b> and expecting it to find all the tests file,
for the initial Pull-Request I'll list the test files I'd like to be checked. Not ideal, but I think it is better to go in small steps than to
be stuck in-front of a big step. So the command I used was

```
pytest -vs tests/test_iter.py tests/test_random.py
```

The ideal way to find out the dependencies was creating a separate virtual envioronment locally and trying to run the tests locally.
I was lazy and did not do that so I had to add them one-by-one as GitHub Actions reported failures. Luckily there were only 2 missing dependencies
besides <b>pytest</b>.


I ended up adding a <b>requirements.txt</b> file with the following lines in it:

```
httpx
requests
```

And adding the following file as <b>.github/workflows/ci.yml</b>

{% include file="examples/once-utils-ci.yml" %}

I also had to disable testing on Windows as that was failing and I also removed the testing on Python 3.11.0 RC 2, though that turned out to be a misunderstanding on my behalf
so I added it back.


