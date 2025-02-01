---
title: "GitHub Action CI for wsblib Python"
timestamp: 2022-12-03T12:30:01
tags:
  - GitHub
  - Python
published: true
books:
  - github
author: szabgab
archive: true
show_related: true
---


After the failure to create GitHub configuration for [farmworld](https://code-maven.com/ci-for-farmworld-python)
I did not know if I should call it a day or try to find something else where I manage to set up GitHub Actions.
I went back to [PyDigger](https://pydigger.com/search/has-github-no-ci) and found the
[wsblib](https://github.com/firlast/wsblib) Python package where the name stands for <b>Web Server Base Library</b>.


It had some tests in the `tests/` folder.

After looking at the test files I saw that they are using [BuPyTest](https://pypi.org/project/bupytest/).
I have not hear about it.
I saw that both files were prepared to be executed directly using the following:

```
if __name__ == '__main__':
    bupytest.this()
```

so I went on running them as <b>python tests/test_server.py</b>.

Later, when I went and looked at the [documentation of BuPyTest](https://github.com/jaedsonpys/bupytest/blob/master/README.md)
and saw that it can be also used as a command-line tool.


## Stages

First I only configured the CI to run on Ubuntu using Python 3.11.


Then I extended it to run the tests on all 3 operating systems and 3 different versions of Python. That's when I found out that
one of the test files consistently fails on Windows and OSX. So I configured the CI that on of the tests files will always run
and the other one only when the operating system is Ubuntu Linux.

Finally I switched from running the tests with <b>python</b> to running them using <b>bupytest</b>.

## GitHub Actions configuration file

This is the most recent version of the file:

{% include file="examples/wsblib/ci.yml" %}

## Conclusion

Sometimes it is simple to set up GitHub Actions, even with testing frameworks that I don't know yet.

