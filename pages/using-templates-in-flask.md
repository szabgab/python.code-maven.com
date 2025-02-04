---
title: "Using templates in Flask"
timestamp: 2015-02-05T06:30:01
tags:
  - flask.render_template
published: true
books:
  - python
  - flask
  - jinja
author: szabgab
archive: true
---


In the previous example we created a simple Flask application that accepted an input value
and [echoed it back](/echo-with-flask-and-python). In order to reduce the scope of the
article I have not used templates, instead I included an HTML snippet in the Python code.

That won't be a good idea in any application that is bigger than a few lines. Let's fix that.

Instead constructing HTML within the Python script, let's use a templating system.


[Flask](http://flask.pocoo.org/) comes with the [Jinja](http://jinja.pocoo.org/)
templating system.

We'll take the example that was using the `POST` method and change it step by step:

{% include file="examples/flask/echo_post.py" %}


After copying the file to `examples/flask/echo_template.py`,
the first thing was to cerate a directory called `templates/` next to the script and move
the HTML snippet of the form to a file called `examples/templates/echo.html`. I even
broke the HTML code into several lines to make it clearer:

```html
<form action="/echo" method="POST">
<input name="text">
<input type="submit" value="Echo">
</form>
```

Now that we have the HTML in an external file we need to tell Flask to load it. The HTML in the
script was replaced by `render_template('echo.html')`. This will look for the `echo.html`
file in the `templates/` directory next to the Flask script.


```python
@app.route("/")
def hello():
    return render_template('echo.html')
```

I have launched the script

`python examples/flask/echo_template.py` and browsed to `http://127.0.0.1:5000/`.
The response:

`Internal Server Error`

That's not good. Let's take a look at the console:

```
$ python examples/flask/echo_template.py 
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [05/Feb/2015 05:52:58] "GET / HTTP/1.1" 500 -
```

Nothing useful there either.

## Debugging

After wasting some time staring at the code, and moving the templates directory around,
I gave in to the obvious next step: Let's turn debugging on.

It can be done easily inside the script by adding `debug=True` to the `app.run()`
method and re-starting the script. (Ctrl-C to stop the previous one, and then run it again.)

```python
if __name__ == "__main__":
    app.run(debug=True)
```

When I re-loaded the page in the browser I saw a nicely rendered page with the following error at the top:

```
NameError: global name 'render_template' is not defined
```

Looking at the console (where I ran the script) I saw the same error message with the full stack-trace in the Python code.

OK, so I've just forgotten to import the `render_template` function.

I went back to the script and updated the first line to have:

```python
from flask import Flask, request, render_template
```

This time I did not even have to manually stop and start the script.

Because we are in debug-mode, Flask was monitoring the file and when it notice that change it has
reloaded the code and printed the following on the console:

```
 * Detected change in '/Users/gabor/work/code-maven/examples/flask/echo_template.py', reloading
 * Restarting with stat
```

I went back to the browser, reloaded the page and voila, I had the input form as earlier. It even worked as earlier.

This is what we have now in the script:

```python
from flask import Flask, request, render_template
app = Flask(__name__)
 
@app.route("/")
def hello():
    return render_template('echo.html')

@app.route("/echo", methods=['POST'])
def echo(): 
    return "You said: " + request.form['text']

if __name__ == "__main__":
    app.run(debug=True)
```


## Passing a parameter to the template

So far we have moved the HTML of the main page to a template. Let's do the same with the response.
If we are already doing it, let's show the form again on the response page, so the user won't have to click
on the "back" button if he wants to echo another text. For this we need two things:

<ol>
  <li>A way to display the content of a variable in the template.</li>
  <li>A way to pass a variable to the template.</li>
</ol>

So I've updated the template and added:

```html
You said: {{ text }}
```

This syntax tells [Jinja](http://jinja.pocoo.org/) to put the content of the `text`
variable instead of the `{{ text }}` snippet.

Then we can pass a value to the `text` variable by passing it to the `render_template` function.
The new `echo()` function looks like this:

```python
@app.route("/echo", methods=['POST'])
def echo(): 
    return render_template('echo.html', text=request.form['text'])
```

After I've saved these changes the server was automatically reloaded and I could go back to the
browser and submit the form again. This time the result included both what I typed and the form again.

<img src="/img/flask_echo_with_form.png" />

It looked good, but I wanted to test it from scratch and thus loaded the main page again. This time I saw
the form an the text `You said:` without anything after it.

<img src="/img/flask_echo_form.png" />

Of course, I did not say anything yet, so it has nothing to display, but then I'd rather it did not show
that text either.

So in our template we need to add a conditional and display the whole
`You said: {{ text }}` business only if there is something in the `text` variable.

This is also supported by [Jinja](http://jinja.pocoo.org/). In side `{%   %}`
pairs we can add some code. This is how the new version of our template looks like:

```html
{% if text %}
  You said: {{ text }}
{% endif %}
```

I am not sure how to describe the code, it is certainly not Python, but you can do all kinds of things with it.
For now we have an `if-endif` conditional pair.
The HTML inside the `if-endif` pair does not have to be indented, but it makes the code cleaner
and thus I recommend to do it.

With this change we have reached the following two files:

{% include file="examples/flask/echo_template.py" %}

and

{% include file="examples/flask/templates/echo.html" %}

That work as planned.

## A warning

The debug-mode is awesome, but it is also very dangerous. Do <b>not</b> use it on anything accessible
by others. It allows people to see details of your computer and to execute arbitrary code on your machine.
Luckily, Flask by default only accepts connections from your local computer so, during development
it is OK to use debug-mode.

