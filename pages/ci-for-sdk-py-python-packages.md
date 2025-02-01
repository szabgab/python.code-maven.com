---
title: "CI for sdk-py Python packages"
timestamp: 2022-12-12T07:20:01
tags:
  - GitHub
published: true
books:
  - github
author: szabgab
archive: true
show_related: true
---


[sdk-py](https://github.com/dimchat/sdk-py) is a Decentralized Instant Messaging (SDK in Python).
It has a <b>tests</b> directory with a <b>test.py</b> file in it that has some Unit-test-based tests.


After playing with a bit locally I found out - something I was missing in a previous package - that I can use
the <b>-e</b> flag for <b>pip install</b> to install the dependencies.

I also found out that in order to make the tests work in this project I have to install the dependencies from both
the root directory and from the <b>plugins</b> directory. Once this was cleared setting up the CI was easy.

Here is the [pull-request](https://github.com/dimchat/sdk-py/pull/1)

## GitHub Actions configuration

{% include file="examples/python/sdk-py/ci.yml" %}

## Conclusion

I think I am a bit tired of this daily CI work. For example this is for day 12, but I already  prepared it on Day 11 and
I am not sure I have the self-discipline to hold it back and only publish it tomorrow. Especially as I already sent the PR.
(Well, I had, so I am publishing this article really on December 12.)

Moreover, now that I sent a PR I would like to go on and try to send a few more. Then maybe for a few days I would not do any.

In addition I think I am letting my readers and certainly myself down by repeatedly doing similar work. At the beginning there were
a few interesting ones with databases, but that required way too much work to sustain on a daily base. In addition, I found them by chance.
If I'd like to have more of these I should look for them. It probably would not be too difficult to find a Python project that uses some X
database, but then it also needs to be one that does not have a CI.

Anyway, it is a good experiment.
