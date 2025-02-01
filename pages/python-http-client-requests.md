---
title: "Python: requests, the HTTP client"
timestamp: 2020-04-20T15:30:01
tags:
  - requests
published: false
books:
  - python
author: szabgab
archive: true
show_related: true
---


The [requests](https://requests.readthedocs.io/) module of Python is one of the most common libraries to
be used as an HTTP client.

[httpbin.org](http://httpbin.org/) is a nice service that you can use to try various HTTP requests.

In this articel I have collected a couple of the examples written using Python requests.


## HTTP GET

{% include file="examples/python/httpbin/get.py" %}

The output will look like this:

{% include file="examples/python/httpbin/get.out" %}

## HTTP POST

{% include file="examples/python/httpbin/post.py" %}

The output will look like this:

{% include file="examples/python/httpbin/post.out" %}

## Basic Authentication

{% include file="examples/python/httpbin/basic_auth.py" %}

What happens if you don't provide the credentials:

{% include file="examples/python/httpbin/basic_auth_no_credentials.py" %}

What happens if you provide the wrong credentials?

{% include file="examples/python/httpbin/basic_auth_wrong_credentials.py" %}


