---
title: "A polling station using Flask"
timestamp: 2015-02-17T17:30:01
tags:
  - render_template
  - request
published: true
books:
  - flask
  - python
author: szabgab
archive: true
---


In this series of articles we are going to build an application to run polls and maybe even surveys using Flask.

In addition to the articles, you can follow the development of the application in [this](https://github.com/szabgab/flask-poll) repository.

Let's get started by creating a simple Flask-based application.


We create an new directory and in that directory we create a Python script with the following content:

{% include file="examples/flask/poll1/poll.py" %}

We created a route for `/` that will invoke the `root()` function that will return the content of
the `poll.html` template. The template itself was added in the `templates/` subdirectory.

{% include file="examples/flask/poll1/templates/poll.html" %}

This is how the directory of the project looks like:

```
$ tree
.
├── poll.py
└── templates
    └── poll.html
```

We can now run `python poll.py` that will tell us

```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
```

If we open the browser to the give URL, we'll see the following:

<img src="/img/flask_poll_1.png" alt="Flask poll" />

Not much, but it is working. Just like the [hello world](/hello-world-with-flask-and-python), but with a template.

```
$ git init
$ git add .
$ git commit -m "step 1 - hello world with a template"
```

[commit](https://github.com/szabgab/flask-poll/commit/c78124201aeb49a2853cac6dc9d28fc1ee03edb3).


## Display the poll

In order to have a poll we need a question and we need a list of values to pick from.
Later this should be probably placed in a configuration file, but for now let's create
a dictionary in our application holding the data:

```python
poll_data = {
   'question' : 'Which web framework do you use?',
   'fields'   : ['Flask', 'Django', 'TurboGears', 'web2py', 'pylonsproject']
}
```

We also change the call to `render_template` and pass this dictionary to it
with an arbitrary key we called `data`.

{% include file="examples/flask/poll2/poll.py" %}

In the template we use the expression `{{ data.question }}` to include the
question. We use that both as the title of the whole page that will show up as the title
of the browser tab, and in an `h1` element to have something more visible.

Then we create a form with `action="/poll">` which means we'll have to create another route
for this in our application. Inside the form, we create a number of `radio` input elements.
One for each value in the list of possible values. Radio input fields are good here as we would like
to get exact one answer.

{% include file="examples/flask/poll2/templates/poll.html" %}

After the changes, if we visit our website we'll see the following:

<img src="/img/flask_poll_2.png" alt="Flask poll" />

If we select one of the items and click on the "Vote" button we get this response:

<img src="/img/flask_poll_2_2.png" alt="Flask poll" />

This just means we have not implemented the `/poll` route yet. Let's do that now.

```
$ git add .
$ git commit -m "add poll data and display it"
```

[commit](https://github.com/szabgab/flask-poll/commit/2a293a4051bc4ba3ae4c8b95dd1e02b669a76b82)

## Accept the vote

First step is to add a function to handle the `/poll` route, accept the value from
the `field` of the form using `request.args.get('field')`. At fist let's just return
this value to the user:

```python
@app.route('/poll')
def poll():
    vote = request.args.get('field')
    return vote 
```

We can reload the browser and it will show our selection:

<img src="/img/flask_poll_3_1.png" alt="Flask poll" />

The next step is to save the vote somewhere. To be simple, we are going to use a flat file for this.
At the beginning of the `poll.py` script we add the name of the file in a variable:
`filename = 'data.txt'` (it is always good to have values in variables),
and then we open the file to append more content (using `'a'` as the parameter to the `open` function),
write the vote to the file and close the file.

We are going to have one vote in every line. It will be easy to collect the data later.

```python
@app.route('/poll')
def poll():
    vote = request.args.get('field')

    out = open(filename, 'a')
    out.write( vote + '\n' )
    out.close()

    return vote 
```

At this point, if we reload the web page, it will already save our vote in the data file, but it will still just echo
back the vote. Instead of that let's add a slightly nicer thank-you page:

```python
    return render_template('thankyou.html', data=poll_data)
```

The Flask script looks like this now:

{% include file="examples/flask/poll3/poll.py" %}

The thank-you template is this:

{% include file="examples/flask/poll3/templates/thankyou.html" %}

```
$ git add poll.py templates/thankyou.html
$ git commit -m "save the vote and thank the voter"
```

[commit](https://github.com/szabgab/flask-poll/commit/ba5a516c7e1506d7c25807ebd18e9ef388df2b9b)

This version of the voting station could already work, but let's add another page showing the results.

## Show the results

In order to show the results we'll create another route called `/results` that will read the data file
and display the number of votes for each one of the candidates.

This is the route:

```python
@app.route('/results')
def show_results():
    votes = {}
    for f in poll_data['fields']:
        votes[f] = 0

    f  = open(filename, 'r')
    for line in f:
        vote = line.rstrip("\n")
        votes[vote] += 1

    return render_template('results.html', data=poll_data, votes=votes)
```

At first we create a dictionary called `votes` where we are going to collect the number of votes.
Then we go over the list of expected names from the original list of fields and put an entry for each one of them
with 0 votes. That will make sure each one of the fields will have a representation in the results, even if no-one voted for it.

Then we open the data file for reading, read line-by-line. Before updating the `votes` dictionary we need to
remove the trailing newline from the line which we do using `line.rstrip("\n")`.

Finally we pass the votes to the `render_template` function.

The template itself looks like this:

{% include file="examples/flask/poll4/templates/results.html" %}

and this is the full script:

{% include file="examples/flask/poll4/poll.py" %}

If we visit the http://127.0.0.1:5000/results url we'll see a response like this:

<img src="/img/flask_poll_4.png" alt="Flask poll" />


```
$ git add poll.py templates/results.html
$ git commit -m "show the results"
```

[commit](https://github.com/szabgab/flask-poll/commit/9c0f04d7c7d80da68c681dfec2c0f7ad4f4d605a)

## What next?

[Testing the Flask Poll](/testing-the-flask-poll).


## Comments

hello in part where we add "

```
@app.route('/poll')
def poll():
vote = request.args.get('field')
return vote "
the /poll pagedoesn't show me the selection I've made

The code:
from flask import Flask, render_template
import os
app = Flask(__name__)

poll_data = {
'question' : 'Which web framework do you use?',
'fields' : ['Flask', 'Django', 'TurboGears', 'web2py', 'pylonsproject']
}

@app.route('/')
def root():
return render_template('poll.html', data=poll_data)
@app.route('/poll')
def poll():
vote = request.args.get('field')
return vote

if __name__ == "__main__":
app.run(debug=True)

```
