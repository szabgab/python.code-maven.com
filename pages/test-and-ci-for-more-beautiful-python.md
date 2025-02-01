---
title: "Test and CI for MoreBeautifulPython"
timestamp: 2022-12-01T14:30:01
tags:
  - GitHub
  - python
description: "Write a simple test and set up GitHub Actions for the MoreBeautifulPython package"
types:
  - screencast
published: true
books:
  - ci
author: szabgab
archive: true
show_related: true
---


For the first day of the [2022 December CI Challenge](https://code-maven.com/2022-december-ci-challenge) I was looking for something relatively easy.
This was partially successful though I ended up with a project that did not have tests yet, so I also had to write one.



## Finding the project

In order to find a package that does not have CI I went over the first page of [Has GitHub but no CI](https://pydigger.com/search/has-github-no-ci) on the [PyDigger](https://pydigger.com/).

I saw a few projects with Machine Learning, I skipped over them as those probably include a lot more CPU power and installation than other projects.

I saw some CLI tools. Those are much more light-weight, but testing CLI in a headless environment might be tricky. So I skipped these too for now.

Web scraping depends on some web site that might change and if it is in Japanese that would be extra difficult for me who does not speak Japanese.

API clients will probably need some API secret.

Finally I found a project that seemed reasonably simple to work on. It is called [MoreBeautifulPython](https://github.com/sudongqi/MoreBeautifulPython).

## How to run the tests?

One thing I noticed with Python projects is that I rarely see instructions in the README or anywhere else on how to
run the tests of the project or how to release it to pypi. That despite the fact that there are <b>more than one ways to do it in Python</b>.
Even more than there are in Perl, where this aspect is quite standardized.

In this project I could not find any file with a name starting with <b>test_</b> which is the standard naming for test-files in Python.
Luckily the README pointed to an example in the repository called <b>examples.py</b>.

I could run it <b>python examples.py</b>. It worked and I saw some output. I looked into the file where I saw two functions with a name
starting with <b>test_</b>. Good, so there might be some test. However the content of those was not very convincing.

I tried `pytest examples.py` but it was broken. I don't know if I ran the test incorrectly or if they are some experiments,
so I [reported the problem](https://github.com/sudongqi/MoreBeautifulPython/issues/1).

So I guess there are no tests.

## Do not import *

Looking at that code, I find the importing everything using <b>*</b> disturbing. This is a bad practice as a change in the module
being imported (e.g. a new version) could break our code. I know that in this case the author of the imported module is using it,
so the chances for the breakage are small, but it is still a dangerous practice. By using this others will also be encouraged to
use the <b>import everything blindly</b> mode instead of the <b>explicit import</b> which is safer and which is much more aligned
with the philosophy of Python of <b>explicit is better than implicit</b>.

## Adding CI to run the examples

As there are no working test first I decided to add a CI that would only run the <b>examples.py</b>. Without even checking its output.
This is far from perfect, but at least we'll have a CI in place and that at least it will verify that the example can run on multiple
versions of Python and various platforms.

My first attempt failed, because I left in some code in the GitHub Actions configuration file that I copied from the
[GitHub Action for Python skeleton](https://code-maven.com/github-actions) I used.

## Adding a test

However, while GitHub was trying to do its job I started to work on a test.

I had to fiddle quite some time till I figured out how to test it. I think the fact that the code uses multiprocessing
is what made my first attempts to fail, but I have not researched that.

Eventually I create a very small example script I called:

{% include file="examples/MoreBeautifulPython/example_log.py" %}

It does not do much, but at least I import the log function explicitly.

I also added a test file called

{% include file="examples/MoreBeautifulPython/test_examples.py" %}

In it I added a function called <b>run_process</b> that can run an external program and capture its output.
I tried it with <b>capsys</b> that comes with <b>pytest</b> but it did not work. I have not invested too much time
into trying to understand why.

After pushing this out to GitHub and letting GitHub Actions do its thing, it still failed on Windows.
I had to deal with the differences in newlines on Windows vs Mac OSX and Linux.
This surprised me a bit, but I did not want to argue with the system so I added some code to expect the appropriate line-ending.


## Installing the requirements

I am used to having <b>requirements.txt</b> in a python project and running <b>pip install -r requirements.txt</b>
to install the dependencies, but this package had its dependencies listed in the <b>setup.cfg</b> file.
I could not find the way to install the dependencies listed there so I ended up running <b>pip install .</b>
on the CI server and installing the whole package. Not the ideal solution, but it will work for now
till someone sends a better solution.


## The CI configuration file

Finally I managed to put together a configuration file as well that I saved here:

{% include file="examples/MoreBeautifulPython/ci.yml" %}


## Pull-Request

I also sent a [pull-request](https://github.com/sudongqi/MoreBeautifulPython/pull/2) where
you can also see my individual commits as I tried the whole thing to work together.

