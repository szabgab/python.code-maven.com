---
title: "Static code analysis for Python code - PEP8, FLAKE8, pytest"
timestamp: 2019-09-21T07:30:01
tags:
  - pytest
  - flake8
  - pytest
published: true
books:
  - python
author: szabgab
archive: true
---


Install

```
pip install flake8
pip install flake8-builtins
pip install pytest-flake8
```

Run

```
pytest --flake8 .
```


If you'd like to run the static analysis on the directory where you have the tests files, and if you want the test-run
to only include the flake8 tests then you need a way to exclude all the other tests. For this I can recommend you use a
fake marker. That is, using `-m qqrq` you tell pytest that only run the test-functions that have a marker "qqrq".
Hopefully none of your tests will use this marker and thus none of your tests will run.

Only the flake8 static code analysis.

```
pytest --flake8 -m qqrq .
```


Configure by including the following in the `setup.cfg` file in the root of your project.

{% include file="examples/setup-with-flake8.cfg" %}


## PEP8

Flake already includes PEP8, so the following is only needed if for some reason you cannot use flake8:

```
pip install pytest-pep8
```

{% include file="examples/setup-with-pep8.cfg" %}


## Cyclomtic complexity

* [Reducing cyclomatic complexity](https://audiolion.github.io/python/2016/10/17/reducing-cyclomatic-complexity.html)
* [hfcca](https://pypi.org/project/hfcca/)
* [radon](https://pypi.org/project/radon/)
* <a
href="https://adrianmejia.com/most-popular-algorithms-time-complexity-every-programmer-should-know-free-online-tutorial-course/">Algorithms</a>


## Use-case for flake8

```
data = 42
other = "Data: {}".format(data)
```

Converted to:

```
data = 42
other = "Data: {data}"
```

forgetting the "f" of the f-string. Now we have a variable called data that is not in use. Flake8 will report:
<b>F841 local variable 'data' is assigned to but never used</b>




