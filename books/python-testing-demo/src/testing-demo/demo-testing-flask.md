# Testing Flask

* [Flask](https://flask.palletsprojects.com/)
* [Flask on GitHub](https://github.com/pallets/flask)


Before getting to our own simple example, let's see the tests of one of the most popular Python libraries.
[Flask](https://flask.palletsprojects.com/) is a minimalistic framework to write web applications in Python.
It is an open source project that has been around for many year.

We can, of course, install it using the regular tools, e.g. `pip install flask`, but what we are really interested in
is to see how a developer of Flask can check that changes made to the project or a newer version of Python does not break
anything that was working before. For this we need to get a local copy of the developmen version of the source code.

We can do this by cloning the [GitHub repository of Flask](https://github.com/pallets/flask)

```
git clone https://github.com/pallets/flask.git
cd flask
pip install -r requirements/dev.txt
pip install -e .
pytest
```
