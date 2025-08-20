# Testing Flask

Before getting to our own simple example, let's see the tests of one of the most popular Python libraries.
[Flask](https://flask.palletsprojects.com/) is a minimalistic framework to write web applications in Python.
It is an open source project that has been around for many year.

We can install it using the regular tools, e.g. `pip install flask`, but what we are really interested in
is to see how a developer of Flask can check how Flask behaves on a newer version of Python, on a different operating system,
or after some changes were made to the project?

* Do they break any of the existing features of Flask?
* How things that were working earlier behave now? Do they still work?
* Are there any regressions?

For this we need to get a local copy of the development version of the source code.

We can do this by cloning the [GitHub repository of Flask](https://github.com/pallets/flask) and running the tests locally.

Follow [these instructions](https://palletsprojects.com/contributing/quick)

The following commands were used on my Linux machine:

* Clone the project and enter the cloned folder:

```
git clone https://github.com/pallets/flask.git
cd flask
git switch stable
```

* [Install uv](https://docs.astral.sh/uv/getting-started/installation/)

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

* Setup the virtual environment which is basically a folder called `.venv`:

```
uv sync
```

* Activate the virtual environment:

```
. .venv/bin/activate
```

* Run the tests, the type-checker, and the documentation checker

```
pytest
mypy
tox run -e docs
```

If that's not enough you can also install the `coverage` module

```
uv pip install coverage
```

run the test using it

```
coverage run -m pytest
```

and then generate the coverage report:

```
coverage report -m --include=src/*
```

It will show you that **92%** of the code has tests.

That means the developers have invested a lot of time and energy making sure their code works the same way day in, day out.

---

* [Flask](https://flask.palletsprojects.com/)
* [Flask on GitHub](https://github.com/pallets/flask)


