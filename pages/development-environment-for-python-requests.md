---
title: "Development environment for Python requests"
timestamp: 2023-03-11T19:00:01
tags:
  - requests
published: true
books:
  - python
author: szabgab
archive: true
show_related: true
---


To make it easier to start to contribute to an open source project, one needs to know how to set up a development environment locally and how to run the tests of the project locally.

As I did not find this information for the [requests](https://requests.readthedocs.io/) Python library I am now trying to describe it myself.


## Clone the repository

This part can be found in the README of the [GitHub repository](https://github.com/psf/requests).

You need to have Python installed and some libraries. You can run it natively on your operating system in a virtual environment or you can run it in a Docker container.

## Start Docker

```
docker run -it --rm --workdir /opt -v$(pwd):/opt python:3.11 bash
```

```
make init
```

That basically runs

```
pip install -r requirements-dev.txt
```

To run the tests you could type

```
make test
```

but it needs <a href="">tox</a> so first you'll have to run

```
pip install tox
```

then you can run

```
make test
```

That will actually run

```
tox -p
```

I also like to be able to run the tests and generate code-coverage report and run the tests in random order.

```
pip install pytest-random-order pytest-coverage

pytest -svv --random-order --cov-config .coveragerc --cov=requests --cov-report html --cov-report term --cov-branch
```

## Virtualenv

```
virtualenv -p python3 venv
. venv/bin/activate
```


```
pip install pytest-coverage
pytest --cov-config .coveragerc --verbose --cov-report term --cov-report xml --cov-report html --cov=requests --cov-branch tests
```

## Adding this to the project

Ideally this and more information about contribution would be included either in the README file or in the CONTRIBUTIONS file of the project. So I opened an [issue](https://github.com/psf/requests/issues/6378) asking if they would be interested in it.


