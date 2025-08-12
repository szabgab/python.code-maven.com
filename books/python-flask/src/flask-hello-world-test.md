# Flask: testing hello world

Before we go ahead learning how to create more complex web applications we need to learn another very important feature of Flask.

Flask makes it very easy to test your web application without even running a web server.

In order to do this we created a file called `test_app.py` in the same folder as we have the `app.py` with the following content.
The name of the files must start with the word `test_`, but otherwise you can pick any filename.

Inside we import the application using `import app` and we add a test function. Its name must start with `test_`, but otherwise we can pick any name.

From the `app` object we imported, that is, from our Flask application, we can get the `test_client` which is a representation of our running web application.

Then we can send in various requests. In this case we sent in an `HTTP` `GET` request to the root of the site using `web.get('/')`.

We get back a response object that we can then interrogate with various assertions.

To run this we'll need to install `pytest`:

```
pip install pytest
```

Then we can just type in `pytest`. It will find and run the tests.

```
pytest
```

## The test file

{% embed include file="src/examples/flask/hello_world/test_app.py" %}


