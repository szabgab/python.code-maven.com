---
title: "GitHub Actions for Colombian Spanish. In Python"
timestamp: 2022-12-04T09:30:01
tags:
  - GitHub
description: "A simple pull-request after a lot of failed attempts"
published: true
books:
  - github
author: szabgab
archive: true
show_related: true
---


Today I wanted to add GitHub Actions based Continuous Integration to a Ruby Gem, but after several failed attempts I went with Python.



## Ruby failures

First I tried some Ruby gems I found on the [Ruby Digger](https://ruby-digger.code-maven.com/).

At first I tried the [act-form](https://github.com/simple-and-powerful/act-form) Ruby gem, but got stuck on
an error: [wrong number of arguments (given 3, expected 1..2)](https://github.com/simple-and-powerful/act-form/issues/9).
I was not sure if the problem is in the code or my own setup, but for my experiments I am using an Ubuntu-based Docker container
where I installed Ruby using apt-get. So unless the version of Ruby is incorrect I don't know what could be wrong on my side.
I hope I'll get an answer to that. Even if it is that the author cannot reproduce the issue.


Then I tried [ach_client](https://github.com/ForwardFinancing/ach_client) written also in Ruby. There I got
several types of errors:
[undefined method 'new' and ArgumentError: wrong number of arguments](https://github.com/ForwardFinancing/ach_client/issues/65)
but I see some overlap. So now I started to worry. Maybe after all the problem is on my setup.


## Python failures

Then I switched to Python and [PyDigger](https://pydigger.com/).

The first I encountered was [GalSim](https://github.com/GalSim-developers/GalSim). As it turned out the GitHub link included
in the distribution was incorrect and that's why PyDigger reported it as having GitHub link but not CI on GitHub.
So I sent a [Pull-Request fixing that](https://github.com/GalSim-developers/GalSim/pull/1196).

Side note: Pydigger should [Report when the URL provided as GitHub repo is invalid. (e.g. returns 404)](https://github.com/szabgab/pydigger.com/issues/61).

Same happened with [flask-fs-router](https://github.com/JarriqTheTechie/flask_fs_router) so here I also sent a
[pull-request fixing that](https://github.com/JarriqTheTechie/flask_fs_router/pull/1).
Though in this case the author might want to go the other way and rename the repo instead. We'll see.


Then I looked at [sphinx-console](https://github.com/zqmillet/sphinx-console) but the tests failed there.
As I have not seen any instructions how to run the tests I was not sure if I am even running them correctly.
So I opened an issue with it: [How to run the tests? No module named 'sphinx_console'](https://github.com/zqmillet/sphinx-console/issues/1)


You might guess that at this point I was already quite exhausted and I have not even mentioned several other failed attempts where
I could not even get to the point to have a reasonable issue to open.


However, I still have not added any CI to any project.

## Adding GitHub Actions to col-spanish

Then I got lucky and bumped into the [col-spanish](https://github.com/sergioasb8/col-spanish) project.

At first this too made me scratch my head as it came with a <b>pyproject.toml</b> file and it was using <b>poetry</b>,
but then I realized this project does not have any dependencies so I could just install <b>pytest</b>
and run with it. This is what I did and it was successful on first try. Here is the [pull-request](https://github.com/sergioasb8/col-spanish/pull/1).

## GitHub Actions configuration file

{% include file="examples/col-spanish/ci.yml" %}

## Conclusion

Sometimes we have a lot of failed attempts till something works and on the way one can help improve other projects as well.

