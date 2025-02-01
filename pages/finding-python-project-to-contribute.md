---
title: "Finding an Open Source Python project to contribute to"
timestamp: 2020-11-21T19:30:01
tags:
  - Python
  - GitHub
published: true
author: szabgab
archive: true
show_related: true
---


Finding a project to contribute to is not always an easy task. Especially if you are a beginner.

The first and probably the obvious suggestion is to contribute to a project you use as there you will have much more motivation.

That's true, however it is quite likely that you use mostly well-known and well-established projects where most of the easy things are already done.

So it will be relatively hard to make a difference, especially if you are relatively new to Python.


## Find a project you use

So the first suggestion is to find a project you use and care about and try to contribute there.

Within a project I would also recommend first you look at the tests. Is the project well tested? Check the test coverage.
It is usually much easier to write a test for a module than to make changes in the code so that would be an easier way in.


## Find a relatively new project

Rather than picking a well established an popular project probably a better suggestion is to find a new project where there is a lot to do.
Your impact on the whole world will be smaller, but your impact on the specific project is, relatively speaking, much bigger.
It will also probably be easier to find something relatively easy to do.

Here too I'd start with external things, like writing tests, setting up a Continuous Integration system etc.

One [GitHub](https://github.com/) there is a link called [Explore](https://github.com/explore) where you can find projects.
You can select the [Topics](https://github.com/topics) and there find [Python](https://github.com/topics/python) (there are 176,059 projects).

That might be too wide of a topic. You might want to go to a more specific one, for example
[Django](https://github.com/topics/django) (25,961  projects),
[Flask](https://github.com/topics/flask) (20,057 projects),
[FastAPI](https://github.com/topics/fastapi) (683  projects),
or [Scarpy](https://github.com/topics/scrapy) (2,367 projects),
or [SciPy](https://github.com/topics/scipy) if that is your direction.

As far as I understand the topic is based on the topics set by the owner of each repository.

Within each topic you can filter by language. As I understand this is something GitHub guesses based on the code in the repository.

For example within the [Flask](https://github.com/topics/flask) (20,057 projects) topic I selected Python
and I can see that [Flask Python](https://github.com/topics/flask?l=python) has (11,374 projects).

In itself it could be interesting to check out all the other projects that used the Flask tag but GitHub thought they are not written in Python.

Anyway, back to finding projects. There is another option on this page that sets the sorting. The default, as I can see is something called "Best match"
which might be nice for some purposes, but I think I need something else.

## Recently updated

I tried the [Recently updated Flask projects](https://github.com/topics/flask?l=python&o=desc&s=updated) and then I looked for a project that
does not have many starts.

I assume that the if a project has been recently updated then it is being worked on so I have a higher chances getting response from the author and having
my work integrated. After all I would like my work to be useful to someone.

The number of stars is an indication of the popularity of the project. I do not want to work on a popular project as there my chances of finding something
easy to do are low. So I'll go with something that is not (yet) popular. I am not sure at what start-count should I aim. 0 ? Lower than 5?
Between 2-10. That is something that has been already noticed by others, but has not become very popular yet?

I guess you'll also have to figure this out for yourself.

## PyVideo

With that said, let me also point you at a project I have contributed a bit to, but that also needs more contributions.

[PyVideo](https://pyvideo.org/) is a site that indexes YouTube videos from Python conferences around the world.

It has two repositories [pyvideo code](https://github.com/pyvideo/pyvideo) (217 stars) and [pyvideo data](https://github.com/pyvideo/data) (339 stars).
As I can see both have quite a few stars and yet there are a number of things to improve. Some, such as improving the meta-data in the data repository, does not
even require programming knowledge.

Others need some programming, and probably more time to make yourself familiar with the project.

