---
title: "GitHub Actions CI for the pcr_optimizer Python package"
timestamp: 2022-12-06T19:30:01
tags:
  - GitHub
published: true
books:
  - github
author: szabgab
archive: true
show_related: true
---


Today I was quite busy and first worked on some other project that I hope will be done in a few days, but I also managed
to add CI to a relatively simple Python package called [pcr_optimizer](https://github.com/Ara101/pcr_optimizer/)


When I first added GitHub Actions it failed to install the dependencies listed in the <b>requirements.txt</b> file with a
nasty error:

```
Collecting logging
  Downloading logging-0.4.9.6.tar.gz (96 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 96.0/96.0 kB 33.1 MB/s eta 0:00:00
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'error'
  error: subprocess-exited-with-error

  × python setup.py egg_info did not run successfully.
  │ exit code: 1
  ╰─> [27 lines of output]
      Traceback (most recent call last):
        File "<string>", line 2, in <module>
        File "<pip-setuptools-caller>", line 14, in <module>
        File "/opt/hostedtoolcache/Python/3.9.15/x64/lib/python3.9/site-packages/setuptools/__init__.py", line 18, in <module>
          from setuptools.dist import Distribution
        File "/opt/hostedtoolcache/Python/3.9.15/x64/lib/python3.9/site-packages/setuptools/dist.py", line 32, in <module>
          from setuptools.extern.more_itertools import unique_everseen
        File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
        File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
        File "<frozen importlib._bootstrap>", line 666, in _load_unlocked
        File "<frozen importlib._bootstrap>", line 565, in module_from_spec
        File "/opt/hostedtoolcache/Python/3.9.15/x64/lib/python3.9/site-packages/setuptools/extern/__init__.py", line 52, in create_module
          return self.load_module(spec.name)
        File "/opt/hostedtoolcache/Python/3.9.15/x64/lib/python3.9/site-packages/setuptools/extern/__init__.py", line 37, in load_module
          __import__(extant)
        File "/opt/hostedtoolcache/Python/3.9.15/x64/lib/python3.9/site-packages/setuptools/_vendor/more_itertools/__init__.py", line 1, in <module>
          from .more import *  # noqa
        File "/opt/hostedtoolcache/Python/3.9.15/x64/lib/python3.9/site-packages/setuptools/_vendor/more_itertools/more.py", line 5, in <module>
          from concurrent.futures import ThreadPoolExecutor
        File "/opt/hostedtoolcache/Python/3.9.15/x64/lib/python3.9/concurrent/futures/__init__.py", line 8, in <module>
          from concurrent.futures._base import (FIRST_COMPLETED,
        File "/opt/hostedtoolcache/Python/3.9.15/x64/lib/python3.9/concurrent/futures/_base.py", line 7, in <module>
          import logging
        File "/tmp/pip-install-aq23csim/logging_1a1a3bc0ef754163a6f124b9848cdcfe/logging/__init__.py", line 618
          raise NotImplementedError, 'emit must be implemented '\
                                   ^
      SyntaxError: invalid syntax
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
error: metadata-generation-failed

× Encountered error while generating package metadata.
╰─> See above for output.

note: This is an issue with the package mentioned above, not pip.
hint: See above for details.
Error: Process completed with exit code 1.
```

I recalled seeing this already, but I was not sure where. It looked like a Python 2 vs. Python 3 issue and started to scratch my head.

Then I noticed it is trying to install the <b>logging</b> module which comes with Python. There is no need to install.
Maybe it was not coming with early versions of Python 2 ? I don't know. I think it was part of Python since I am using Python.

Anyway, I removed <b>logging</b> from the <b>requirements.txt</b> file.

I also had to set the <b>PYTHONPATH</b> environment variable to let the tests find the module.

Finally, I noticed that <b>__pycache__</b> was generated while I ran the tests on my computer. So I added it to the <b>.gitignore</b> file
to make sure this folder is not added to github by mistake.

That's it. The tests passed and I sent the [Pull-Request](https://github.com/Ara101/pcr_optimizer/pull/4).

Here is the configuration file:

{% include file="examples/pcr_optimizer/ci.yml" %}

## Conclusion

Sometimes you need to make slight changes for the CI to start working.

