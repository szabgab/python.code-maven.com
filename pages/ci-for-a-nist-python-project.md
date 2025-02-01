---
title: "CI for a Python project of the National Institute of Standards and Technology"
timestamp: 2022-12-13T06:30:01
tags:
  - GitHub
published: true
books:
  - github
author: szabgab
archive: true
show_related: true
---


Interesting coincidences.

Just a few days ago as I started to work on the [Open Source Developer Course](https://osdc.code-maven.com/) I started
to collect [Open Source projects by governments](https://github.com/szabgab/open-source-by-government) and today
the first project I found on [PyDigger](https://pydigger.com/search/has-github-no-ci) that I wanted to try to contribute to
was a project of the [NIST - the National Institute of Standards and Technology](https://www.nist.gov/).


Side note: I find it funny that in this age of globalization when anyone can easily bump into any organization (barring language barrier),
organizations still call themselves "National" without including an indication of <b>which nation</b>, in their name. At least on the web
site of [NIST](https://www.nist.gov/) you can see <b>US Department of Commerce</b> in their logo.

## The process

Anyway, what did I do?

I noticed that the project has a folder called <b>tests</b> but that it also has a file called <b>runtests.py</b>.
I am not sure why do some projects have their own test-runner instead of just running <b>pytest</b>, but I seem to recall I saw this
in other Django-related projects as well.

So I set started a Docker container that I use for better isolation of the foreign code I run from my computer and ran

```
python runtests.py
```

Not surprisingly it failed complaining about missing Django.

So I went ahead and installed all the requirements I could find:

```
pip install -r requirements.txt
pip install -r requirements.core.txt
```

Running again

```
python runtests.py
```

still failed. This time it was missing <b>psycopg2</b> which is the Python package to connect to PostgreSQL.

So I tried to install it:

```
pip install psycopg2
```

It failed, but it pointed me at the [installation documentation](https://www.psycopg.org/docs/install.html).
That's a very nice touch!

From that website I understood I need to install <b>libpq</b>. So I ran

```
apt-cache search libpq
```

(I use an Ubuntu 22.10 based Docker container for my experiments.)

In the results of this command I saw <b>libpq-dev</b>. This is the development package. Libraries usually need that so I installed it:

```
apt-get install -y libpq-dev
```

and ran the installation again:

```
pip install psycopg2
```

After that I ran the tests again:

```
python runtests.py
```

The output looked very much like an output from a test-run and it ended with

```
Ran 86 tests in 0.271s
```

It was not hard at all.

I created the GitHub Actions configuration file using a Docker container and configured python 3.11. I let the developers of the package
decide which other versions of Python they might want to test with and if they might want to test on Windows and macOS as well.

I sent the [Pull-Request](https://github.com/usnistgov/core_curate_app/pull/8)

## GitHub Actions

{% include file="examples/python/core_curate_app/ci.yml" %}

## Conclusion

I am already quite experienced setting up CI in general and GitHub Actions in particular, but I think even people who are new to this area
could do similar task within a few hours. So I think these will be reasonable assignments in the [Open Source Development Courses](https://osdc.code-maven.com/).


