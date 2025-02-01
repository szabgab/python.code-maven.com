---
title: "Extract HTML links using Python HTML Parser"
timestamp: 2015-07-08T09:30:01
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


We have seen how to [parse the HTML file and print the links](/print-html-links-using-python-htmlparser) using
the HTMLParser module of Python, but instead of printing them to the screen we should somehow process the links.

That's what we are going to do now. We are going to extract the links and let some other code collect or process them.


## Using a global variable

{% include file="examples/python/extract_links_html_parser_global.py" %}

In this solution we added a  global variable called `links` that
starts out as an empty list (line 5).

```python
  links = []
```

Then within `MyHTMLParser`, the subclass of
[HTMLParser](https://docs.python.org/2/library/htmlparser.html),
we append each link to this list (line 12).

```python
links.append(attr)
```

Finally, once the processing is over, we can go over the extracted list of links
and print them or do whatever we need to do with them (lines 31-32).

```python
for l in links:
    print(l)
```

An alternative would be to do some processing instead of collecting the links,
that would mean calling a function from within the parser (on line 12)
and passing the link to it. That would still probably need some global variable where we collect
the results of that processing.

Another alternative would be to use an attribute of the parser object to
collect the links:

## Using attribute of the parser

{% include file="examples/python/extract_links_html_parser_attribute.py" %}

In this solution, right after creating the parser, in line 27, we attached a new attribute to it:

```python
parser.links = []
```

then, inside the parser subclass we append the links to this attribute (line 10):

```python
self.links.append(attr)
```

And finally we loop over the collected links (lines 29-30):

```python
for l in parser.links:
    print(l)
```

This seems to be cleaner than the previous solution because we don't use a global
variable, but we take a risk. We have assumed the HTMLParser class does not
have an attribute called `links` and if in the future it gets one, our
code will break. Which means we need to be more careful with upgrades.
Maybe we should also add a comment explaining the problem.
