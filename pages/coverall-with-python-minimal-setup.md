---
title: "Minimal setup for Coverage report at Coveralls for Python projects hosted on GitHub"
timestamp: 2018-02-16T18:30:01
tags:
  - Travis-CI
  - Coveralls
  - pytest
  - coverage
published: true
books:
  - python
author: szabgab
archive: true
---


[Coveralls.IO](https://coveralls.io/) is one of the cloud-based services that can collect and display test coverage reports.
It is free for Open Source projects hosted on GitHub or BitBucket.


Make sure [Travis-CI](https://travis-ci.org/) is already enabled for your project and the tests pass.

Register on the [Coveralls.IO](https://coveralls.io/) web site using your GitHub account. Look for the "Add repos" button,
select the GitHub repo that you'd like to enable.

You already have a `.travis.yml` file in the root of your repository, now you only need to add a few more entries.

Mine looks like this as I am using [pytest](https://pytest.org/):

```
language: python
python:
  - "3.6"
install:
  - pip install pytest
  - pip install pytest-cov
  - pip install coveralls
script:
  - pytest --cov=YourModule/
after_success:
  - coveralls
```

The important part is to install `pytest`, `pytest-cov` that allows us to generate the coverage report locally. (Meaning on the Travis-CI server.)
We also need to install `coveralls` that can submit the the report to the Coveralls.io site.

In the script part we need to run `pytest` with the `--cov` flag. You don't need to give a parameter to that
flag, but then you might get reports on code that is not relevant to your application. It is better to pass the directory name
of your module to it (as I did with `--cov=YourModule/`) so the coverage report will be restricted to code
in that directory.

You also need to tell Travis-CI to run the `coveralls` command after the test ran successfully.

That's it. Your coverage reports should start flowing to Coveralls.io.

<img src="/img/coveralls-stomp-out-bugs.png" "coveralls logo stomp out bugs">
