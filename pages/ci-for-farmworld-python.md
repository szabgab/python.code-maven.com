---
title: "CI for farmworld, a Python package - a failed attempt"
timestamp: 2022-12-03T11:00:01
tags:
  - GitHub
  - Docker
  - Python
published: true
books:
  - github
author: szabgab
archive: true
show_related: true
---


[FarmWorld](https://github.com/tomgrek/farmworld) is a reinforcement learning library for agriculture written in Python.



This package had instruction in the README file on how to install and how to release.

It came with a <b>Makefile</b> which is a bit strange as there are python-based tools that could do the same job,
but that makefile did not have a "test" target either.

I tried to follow the instruction in the README file.

On Python 3.11 the installation failed with

```
Unable to find installation candidates for ale-py (0.7.4)
```

I reported it: [Dependencies are missing on python 3.11](https://github.com/tomgrek/farmworld/issues/1)

On Python 3.10 the installation worked, but the tests failed with

```
pytest: command not found
```

Fair enough. There is no pytest installed.

At this point however I got a bit fed up and thought I should try it locally in a Docker container:


## Trying to run in Docker container

After cloning the repository:

Start the container:

```
docker run -it -v$(pwd):/opt --workdir /opt --name farm ubuntu:22.04 bash
```


Install make, python and virtualenv:

```
apt-get update
apt-get install -y make
apt-get install -y python3
apt-get install -y python3.10-venv
```

Just to make sure we have a good version of Python I also ran <b>python3 --version</b> and the response was <b>Python 3.10.6</b>.
So it is fine.

I tried to run <b>make venv</b> but that relies on the command <b>python</b> being available. However in Linux the package is called
<b>python3</b>. So instead I executed the command manually:

```
python3 -m venv .venv
```

I also reported it: [python is called python3 on Linux - Makefile assumes python](https://github.com/tomgrek/farmworld/issues/2)

Then I continued:

```
make install
```

Everything installed fine.

Apparently at first looking at the README file I missed the instructions on how to run the tests, but I saw two test scripts in the `test/` folder
so I installed <b>pytest</b> and then tried to run the tests:

```
.venv/bin/pip install pytest
PYTHONPATH=. .venv/bin/pytest test/
```

This gave me an error:

```
pygame.error: No available video device
```

At this point I feel I am stuck. I found some instruction on how to add video device to Docker,
but I somehow doubt I'd be able to do this on GitHub Actions.

## Including test-running in the Makefile

Although I don't particularly like the use of Makefile here, but if that's what the author prefers then let's go
all the way and add the test running to it as well.

I sent a [Pull-request](https://github.com/tomgrek/farmworld/pull/3) adding <b>tests</b> target to the Makefile


## No available video device

Finally I opened and issue with the [pygame.error: No available video device](https://github.com/tomgrek/farmworld/issues/4)
asking if there could be tests that don't require a video device.

## GitHub Actions configuration file

It does not work yet (?), but let me share the configuration file I created so far. It might be useful later on.

{% include file="examples/farmworld/ci.yml" %}

## Conclusion

This time my attempt to add GitHub Actions failed, but I hope I managed to contribute a bit to this project.


