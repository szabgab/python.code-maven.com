---
title: "Skeleton: A minimal example generating HTML with Python Jinja"
timestamp: 2018-05-19T19:30:01
tags:
  - jinja2
  - Environment
  - PackageLoader
  - FileSystemLoader
published: true
books:
  - python
author: szabgab
archive: true
---


[Jinja](http://jinja.pocoo.org/) is a templating system usually used together with the [Flask](http://flask.pocoo.org/) web framework, but it can also be used separately. I often start projects generating some static HTML files based on some data in JSON file as was the case in the [Code And Talk](https://codeandtalk.com/) project. In other cases data is taken from a database, but I might still start by generating a few static HTML pages.

Every time though I have to spend some time figuring out how to lay out my files and how to load the template. So here is an example that you can also use as a skeleton for your next application.


## Layout of the directories and the files

```
.
├── generate_from_filesystem.py
├── html
│   └── index.html
└── templates
    └── index.html
```

{% include file="examples/python/jinja-skeleton-flat/generate_from_filesystem.py" %}

{% include file="examples/python/jinja-skeleton-flat/templates/index.html" %}


In our example, the result is saved in the 'html' directory and it looks like this:

{% include file="examples/python/jinja-skeleton-flat/html/index.html" %}



## Another case more suitable for code with modules

## Layout of the directories and the files

```
.
├── app
│   ├── __init__.py
│   └── templates
│       └── index.html
├── generate.py
└── html
    └── index.html
```

Jinja, or at least my example, wants to load a Python module and thus there is a directory called `app`, that can be any arbitrary name, just one that is not the name of any of the module we are going to use. In the `app` directory we have an empty file called `__init__.py`. This file is just standard Python practice. This indicates to Python that "app" is a module. In the "app" directory there must be a directory called `templates` and in that directory the actual HTML templates with Jinja code in them. The directory name must be `templates`, the template files can have any name and any extension.

The Python program that actually loads the template and generates the html pages is called `generate.py`. That again can have any name. I put it in the root of the project as that seemed convenient.

There is also a directory called `html`. This is where the end-results are going to be saved. This directory can have any name and can be placed anywhere. You'd just need to adjust the code that generates the path to it.

## The code

{% include file="examples/python/jinja-skeleton/generate.py" %}

Jinja deals with "environments", hence we import the `Environment` and the `PackageLoader` form Jinja.
Then in line 3 we create a variable that we cleverly called `env` that represents the environment and know where to load the files from. The Template itself can be loaded using the `get_template` method of this object. Python adds the directory of the executable (in our case the directory of the generate.py file) to the path where it looks for modules. So Jinja also knows how to find the "app" directory. So we don't have to deal with that.

In the next two lines we use the `os` module of Python to compute the path to the output file. In our case we wanted it to be relative to the location of the `generate.py` and we wanted to make sure no matter what is our current working directory when we invoke the program.

Then it is only a matter of opening the file for writing and then writing out the string created by the `render` method of the `template` object. The parameters we pass to the `render` method will be accessible in the Jinja template itself.

That's the whole thing.

## The template

{% include file="examples/python/jinja-skeleton/app/templates/index.html" %}

The Jinja Template uses the Mustache-like markup for inserting the values of individual attributes: `{{ name }}`.
It also uses `{%  %}` pairs to embed some Jinja code. You can do a number of things with it. In our example we see a condition and a loop. Note, unlike Python, here you need to end the blocks with `endif` and `endfor` respectively.

## The end result

Finally, just for completeness, let's see how the generated HTML file looks like:

{% include file="examples/python/jinja-skeleton/html/index.html" %}

Of course, you might be better off starting by one of the other [HTML skeletons](https://code-maven.com/skeletons),
but I wanted to make this example as simple as possible.

