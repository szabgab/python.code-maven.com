# Flask Jinja template

In every web application we need to use multiple languages. We need some programming language for the backend. In our case it is Python. We probably need to use SQL in order to talk to the relational database behind the application. If this is not just an API then we need to generate HTML content. It probably uses some CSS to make it look nicer and it probably has some JavaScript code to enhance the interactivity. (e.g. to have a navigation bar that can collaps to a hamburger.) That's already 5 different languages.

In the 90s we used to put all these languages in a single file, but our code-base is much more maintainable if we can have these in separate files.

So far in our code we used Python and a bit of HTML. A template system allows us to separate the HTML templates into their own files.

Then, when we would like to return an HTML to our client, we need to render the templat with some data that we provide from our Python code.

[Jinja](https://jinja.palletsprojects.com/) is one of the most popular template systems
and it is the default template system of Flask.

In this example we'll use the `render_template` function of Jinja to render a page without any parameter.
Of course this is a bit boring as this means the HTML will be exactly the same as the template.

Nevertheless, this is a good first step.

```
$ tree
.
├── jinja_plain.py
├── templates
│   └── index.html
└── test_jinja_plain.py
```


{% embed include file="src/examples/flask/jinja-plain/jinja_plain.py" %}

{% embed include file="src/examples/flask/jinja-plain/templates/index.html" %}


