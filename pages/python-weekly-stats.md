---
title: "Python Weekly statistics (using urllib2, HTMLParser and pickle)"
timestamp: 2015-08-02T17:30:01
tags:
  - urllib2
  - pickle
  - HTMLParser
published: true
books:
  - python
author: szabgab
archive: true
---


The [Python Weekly](http://www.pythonweekly.com/) is a weekly newsletter curated by Rahul Chaudhary
and sent out every Thursday. It has an [archive](http://www.pythonweekly.com/archive/),
though unfortunately I only found the first 81 issues in there and on July 30 2015 it was already issue 202.

Nevertheless, I think it is an interesting exercise to collect link statistics from these issues.

Specifically, I wanted to know which hosts are featured the most in the Python Weekly.


The result is that there were a total of 2399 links to 910 different hosts in the first 81 issues of the Python weekly.
The top featured hosts were:

* [github.com](http://github.com/) 420
* [www.meetup.com](http://www.meetup.com/) 134
* [jobs.pythonweekly.com](http://jobs.pythonweekly.com/) 106
* [www.amazon.com](http://www.amazon.com/) 66
* [www.youtube.com](http://www.youtube.com/) 45
* [meetup.bostonpython.com](http://meetup.bostonpython.com/) 31
* [bitbucket.org](http://bitbucket.org/) 27
* [launchbit.com](http://launchbit.com/) 21
* [code.google.com](http://code.google.com/) 20
* [www.slideshare.net](http://www.slideshare.net/) 20
* [vimeo.com](http://vimeo.com/) 17
* [meetup.dcpython.org](http://meetup.dcpython.org/) 15
* [www.djangoproject.com](http://www.djangoproject.com/) 14
* [cloud.google.com](http://cloud.google.com/) 14
* [eli.thegreenplace.net](http://eli.thegreenplace.net/) 14
* [www.ibm.com](http://www.ibm.com/) 13
* [morepypy.blogspot.com](http://morepypy.blogspot.com/) 12
* [blog.pythonisito.com](http://blog.pythonisito.com/) 12
* [www.djangonyc.org](http://www.djangonyc.org/) 11
* [speakerdeck.com](http://speakerdeck.com/) 11
* [jakevdp.github.com](http://jakevdp.github.com/) 11
* [inventwithpython.com](http://inventwithpython.com/) 10
* [charlesleifer.com](http://charlesleifer.com/) 10
* [emptysquare.net](http://emptysquare.net/) 10
* [www.mightydeals.com](http://www.mightydeals.com/) 10
* [pycon.blogspot.com](http://pycon.blogspot.com/) 10
* [www.blog.pythonlibrary.org](http://www.blog.pythonlibrary.org/) 9
* [www.jeffknupp.com](http://www.jeffknupp.com/) 8
* [radiofreepython.com](http://radiofreepython.com/) 8
* [agiliq.com](http://agiliq.com/) 8
* [pydanny.com](http://pydanny.com/) 8
* [googleappengine.blogspot.com](http://googleappengine.blogspot.com/) 8
* [net.tutsplus.com](http://net.tutsplus.com/) 8
* [tech.yipit.com](http://tech.yipit.com/) 8
* [www.mutualmobile.com](http://www.mutualmobile.com/) 8
* [www.python.org](http://www.python.org/) 8

## The code behind the stats

While the numbers themselves might be interesting, the main point of this exercise
was to write and explain the code behind it. So let's see the full script,  and then
let's explain it:

{% include file="examples/python/python_weekly_stats.py" %}

The code has two major parts. One of them fetches the URLs of the archive pages,
parses the HTML and enters all the data into a dictionary.
The other part generates the report from this dictionary.

In order to avoid repeatedly downloading all the pages while working on the
report the data collected by the first part was serialized using the standard
[pickle](https://docs.python.org/2/library/pickle.html) module.

This technique would be also very useful if the archive was actually growing every
week and if we wanted to update our stats every week. In that case having the
previously collected and processed data stored in a local file would allow us
to retrieve only the new issues. That would be more considerate of the web site
and would not waste our bandwidth either.

The two classes in the script are the `Collector` class and the `ArchiveHTMLParser` class.
The latter is a subclass of the [HTMLParser](https://docs.python.org/2/library/htmlparser.html)
that parses the retrieved HTML files, the individual archive pages.

The `Collector` class has a method `collect`, that does the data collection (using the `ArchiveHTMLParser` class),
and another method called `report` that generates the report.

## Construction and loading the serialized data

In the body of the script we create an instance from the `Collector` class and immediately call it `run` method
that will process the command line options.

When the the Collector instance is created Python calls the `__init__` constructor where we
set the name of the file in which we keep the serialized data and set up a dictionary to represent the
data if the file does not exist yet. Then we call the `read_cache` method that will load the
data from the pickled file, if the file already exists. When we run the script for the first time
this method does not do anything and then we rely on the `data` attribute created in the
constructor.

```python
class Collector(object):
    def __init__(self):
        self.cache_file = 'python_weekly.pickle'
        self.data = { 'issue': 0, 'hosts' : {} }
        self.read_cache()

    def read_cache(self):
        if os.path.exists(self.cache_file):
            fh = open(self.cache_file, 'r')
            self.data = pickle.load(fh)
            fh.close()
```

## Saving the serialized data

A separate `save_cache` method was added to serialize the data using pickle
and save it in a file.

```python
def save_cache(self):
    fh = open(self.cache_file, 'w')
    pickle.dump(self.data, fh)
    fh.close()
```

## The Data

The dictionary `data` itself has two keys. `issue` holds the number of most
recent issue processed. It defaults to 0 and is updated every time we fetch a new page.
The other key is `hosts` which itself holds a dictionary in which the key/value
pairs are the hostnames and the number of occurrences.

## Data collection

The `collect` method has an infinite loop in it. On every iteration we increase
the number of the issue we are processing and we leave the loop using `break`
when the retrieval of the HTML page fails. Assuming that means we reach the end of the archives.

The first step in the collection is to create the URL of the current issue using the `base_url`
and the number of the current issue. (and an .html extension).
We then use [urllib2](https://docs.python.org/2/library/urllib2.html) to fetch the page.
If the fetching fails we leave the infinite loop using `break`.

If the fetching of the HTML was successful we create a parser instance and feed the html
to it. The parser is very simple. It will extract the links and put the URLs into an
attribute called `urls`. That way we'll be able to access the list of urls after
the parsing has finished.

Once the parsing is finished we iterate over the urls hold in the `parser.urls`
attribute. We eliminate the self links that only have a "#" in them and check if the
current url stars with either http:// or https:// . We used a Regular Expresion for this.

Using another Regular Expression we extract the fully qualified hostname form the URL,
removing the http:// from the beginning and the path in the URL after the host and domain name.

```python
def collect(self):
    base_url = 'http://www.pythonweekly.com/archive/'
    while (True):
        self.data['issue'] += 1
        url = base_url + str(self.data['issue']) + '.html'
        try:
            f = urllib2.urlopen(url)
            html = f.read()
            f.close()
        except urllib2.HTTPError as e:
            print(e, 'while fetching', url)
            break

        parser = ArchiveHTMLParser()
        parser.urls = []
        parser.feed(html)
        for u in parser.urls:
            if u == '#':
                continue
            if not re.search(r'^https?://', u):
                print("Unhandled url: " + u)
                continue
            match = re.search(r'^https?://([^/]+)', u)
            if match:
                host = match.group(1)
                if host not in self.data['hosts']:
                    self.data['hosts'][host]  = 0
                self.data['hosts'][host] += 1
        self.save_cache()
```

If you are not familiar with regexes, then this regex might need some explanation:

```python
match = re.search(r'^https?://([^/]+)', u)
```

`^` means match at the beginning of the string.

`?` in `https?` means the character `s` is optional in the match.

`://</lh> just matches `://`, nothing special there.

`[^/]` means match any character that is not a slash. `[^/]+` match
as many non-slashes as possible, but at least match one. (+ means 1 or more).

The parenthese `()` tell the regex engine to capture whatever was matched by
the regex inside the parentheses and make that accessible via `match.group(1)`.

On every iteration, after retrieving a url and adding its links to the `data` dictionary
we call the `save_cache` method to serialize the data and save it to the disk.

## Parsing HTML with HTMLParser

the HTMLParser subclass is quite simple, and it was actually explained in
the article about [extracting html links using Python](/extract-html-links-using-python-html-parser).
As the HTMLParser goes over the HTML page it will call the `handle_starttag` method on every start tag.
We only handle the `a` tags and save their `href` attribute.

```python
class ArchiveHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag != 'a':
            return
        attr = dict(attrs)
        if 'href' in attr:
            self.urls.append(attr["href"])
        else:
            print("Missing href from a with attributes: ", attr)
```

## Generate Report

The last part of the `Collector` class is the `report` method, that
will use the data in the `data` attribute to sort the URLs and their hit count
sorted by the count.

```python
def report(self):
    hosts, total = 0, 0
    for k in sorted(self.data['hosts'].keys(), key=lambda x: self.data['hosts'][x], reverse=True):
        hosts += 1
        total += int(self.data['hosts'][k])
        #print(k, self.data['hosts'][k])
        print('<li>[{0}](http://{0}/) {1}</li>'.format(k, self.data['hosts'][k]))
    print("A total of {} links to {} hosts in {} issues.".format(total, hosts, self.data['issue']))
```


## Conclusion

As I wrote in the opening these numbers only represent the first 81 issues of the
[Python Weekly](http://www.pythonweekly.com/) It could be interesting
to track down the other, more than 140 issues and create the stats based on that.

It might be also interesting to merge the different blogspot gTLDs.
(If you are visiting a Blogspot site from Italy, it will redirect you to blogspot.it and if the author
of the weekly does not notice it the localized link will be included in the article. It is not a
problem, but it changes the stats.)
