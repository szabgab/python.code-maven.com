---
title: "Echo with Flask and Python"
timestamp: 2015-02-04T13:30:01
tags:
  - request
  - args
  - form
  - GET
  - POST
published: true
books:
  - python
  - flask
author: szabgab
archive: true
---


In order to see how does Flask give access to the information the user sent to the server we are going to
create a very simple application echoing back the data.

The main page has a text-form and a button. If we type something in the box and click on the button,
the request will be sent to the server that will echo it back on another page.


There are two major methods to send data to the server via HTTP. One using a GET request, the other one using a POST request.
First let's see the solution with a GET request:

## Using GET requests

{% include file="examples/flask/echo_get.py" %}

We have two routes here. The first one, responding to the request of `/` will send back and HTML snippet that
was embedded in the code. Once we pass the most basic examples we are going to start using templates
to separate HTML from the Python code, but for this example we can still get by including the HTML in our script.

This HTML snippet will show up in our browser as a text-box and a button. The `action` property
of the `form` element tells the browser where to send the data when the user clicks on the `submit` button.
The `method` attribute tells the browser which method to use and while `GET` is the default I added it
explicitly to make the example clearer.

In our case this means when the user clicks on the button the browser will send a `GET` request to `/echo`.

If we typed in "hello" and clicked on the button, we would see the URL in the address-bar of our browser changed to

`http://127.0.0.1:5000/echo?text=hello`

The name of the field "text" is the `name` of the `input` element in the HTML the main page sent back.
"hello" is what we typed in.

The second route maps the `/echo` url to `echo` function.

The really interesting part in that function is the use [request](http://flask.pocoo.org/docs/0.10/reqcontext/)
context. `request` has an attribute called `args` which is a dictionary holding the data
received in the URL. In our case that would be a key called "text" and a corresponding value "hello".

Instead of directly accessing the "text" key using `request.args['text']` we use the `get` method
and even supply the empty string as the default value.  `request.args.get('text', '')`

The reason we prefer the latter here is that in Python, if we try to access a dictionary key that does not exist,
even just for reading, Python will throw an exception. (In other words, Python does not provide
[/autovivification](https://perlmaven.com/autovivification).

The user can easily edit the values in the address bar. If she decides
to remove all the attributes and send in a request to `http://127.0.0.1:5000/echo` then request will throw an
exception that will show up in the browser as <b>Bad Request</b>.
We could add code to catch these exceptions, but it seems to be simpler to call `get` and if there is no such key
then let it return the empty string.
This route just sends back the text "You said: " followed by the text the user typed in.

## Using POST request

{% include file="examples/flask/echo_post.py" %}

There were a few changes here: 

<ol>
  <li>In the embedded HTML we replaced the `GET` method to be `POST`</li>
  <li>In the route definition we explicitly said this route handles POST requests: `@app.route("/echo", methods=['POST'])>`</li>
  <li>We fetch the value sent by the user from the `form` dictionary of `request`</li>
</ol>

Not only do we use the `form` dictionary but the recommendation of the Flask tutorial is to access the key directly.
with square brackets: `request.form['text']`.

The reasoning is that it is much harder for the regular user to send in a form without the proper keys, but if
that happens we would probably want to throw an exception anyway. We won't need to do that manually because
Python will already throw the exception for us.

(If we did not want those exceptions, we could go with code similar to the earlier solution:
`request.form.get('text', '')`

Before running this script, make sure the other one has been stopped. Otherwise you'll get a nasty exception:

```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
Traceback (most recent call last):
  File "examples/flask/echo_post.py", line 14, in <module>
    app.run()
  File "/Library/Python/2.7/site-packages/flask/app.py", line 772, in run
    run_simple(host, port, self, **options)
  File "/Library/Python/2.7/site-packages/werkzeug/serving.py", line 624, in run_simple
    inner()
  File "/Library/Python/2.7/site-packages/werkzeug/serving.py", line 602, in inner
    passthrough_errors, ssl_context).serve_forever()
  File "/Library/Python/2.7/site-packages/werkzeug/serving.py", line 512, in make_server
    passthrough_errors, ssl_context)
  File "/Library/Python/2.7/site-packages/werkzeug/serving.py", line 440, in __init__
    HTTPServer.__init__(self, (host, int(port)), handler)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/SocketServer.py", line 419, in __init__
    self.server_bind()
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/BaseHTTPServer.py", line 108, in server_bind
    SocketServer.TCPServer.server_bind(self)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/SocketServer.py", line 430, in server_bind
    self.socket.bind(self.server_address)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/socket.py", line 224, in meth
    return getattr(self._sock,name)(*args)
socket.error: [Errno 48] Address already in use
```

At least this one, unlike [Node.js](/getting-started-with-nodejs) will show the correct explanation
on the last line of the exception.

Once you launched the new script successfully, you also have to remember to reload the page
at http://127.0.0.1:5000/

Without reloading it you'll still have the old HTML in it that sends that using `GET`.
If you click on the submit button while the old HTML is still in the browser, but the new script
runs you'll see the following error in the browser:

```
Method Not Allowed

The method is not allowed for the requested URL.
```

That happens because the browser sent a `GET` request, but the new script only handles
`POST` request at the `/echo` URL.


## How to trigger the error in POST request?

As we saw, when using `GET` requests, the user can easily send in a request with missing or even incorrect
fields. The user can just load http://127.0.0.1:5000/echo  or  http://127.0.0.1:5000/echo?txt=hello

When using `POST` requests, it is a bit more difficult to send such bad requests.
One cannot do it from a plain browser, though there are plugins that would let you do that.

On the other hand it is very easy to send such broken requests using `curl` on the
Linux/Unix command line:


Send a POST request without any data and see the error:

```
$ curl --data '' http://127.0.0.1:5000/echo

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>400 Bad Request</title>
<h1>Bad Request</h1>
<p>The browser (or proxy) sent a request that this server could not understand.</p>
```

Send a POST request with incorrect field name (txt instead of text), and see the error:

```
$ curl --data 'txt=world' http://127.0.0.1:5000/echo

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>400 Bad Request</title>
<h1>Bad Request</h1>
<p>The browser (or proxy) sent a request that this server could not understand.</p>
```

... and just to show you that the problem is not in `curl`, if we send in the proper key then we can a correct
response:

```
$ curl --data 'text=world' http://127.0.0.1:5000/echo

You said: world
```


## Conclusion

You can access the values passed in the URL via `request.args` and the values passed in a POST-request via
`request.form`

The recommended way to access the values is via `request.args.get('key', '')` for GET requests and
`request.form['key']` though in both cases we can use the "other" way as well.



