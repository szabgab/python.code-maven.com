---
title: "Print HTML links using Python HTML Parser"
timestamp: 2015-07-06T22:30:01
tags:
  - HTMLParser
  - handle_starttag
  - urllib2
published: true
books:
  - python
author: szabgab
archive: true
---


Now that we know how to [fetch an HTML page with Python using urllib](/urllib-vs-urllib2) we take another step
and try to extract all the links from the HTML file. For this we are going to use the
[HTMLParser](https://docs.python.org/2/library/htmlparser.html) module.


{% include file="examples/python/print_links_html_parser.py" %}

The `extract` function first expects a URL on the command line, and then using that URL
and the urllib2 library, it fetches the HTML served on that URL.

Then we create an HTMLParser instance and call the `feed` method passing
the HTML to it. More precisely, we are subclassing HTMLParser and we create an instance
of that subclass.

The way HTMLParser works is that it goes over all the elements of the HTML and every time
it encounters an opening tag it calls the `handle_starttag` method with two parameters,
(besides the object itself): the name of the tag and the attributes as a list of tuples.

When it encounters an end-tag it calls `handle_endtag` with the name of the tag.

When it encounters text inside a tag (for example the anchor of a link), it calls the
`handle_data` method with the text.

If we subclass the HTMLParser, and implements some, or all of the above methods, then
when we call the `feed` method, it will call the methods we have overridden
in the subclass.

So we have created a subclass called `MyHTMLParser` and we have implemented
the `handle_starttag` in it. In this task we are only interested in the
URLs of the links and those are the `href` attributes in the opening part of the `a` tags.

Inside the method we check the tag and if it is not an `a` then we call `return`:
We don't need to do anything with such tags.

If it is an `a` tag, we convert the attributes to a dictionary and then print
them out.

In the next article we'll see how can we [collect this information](/extract-html-links-using-python-html-parser)
for later use.
