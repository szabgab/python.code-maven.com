---
title: "Calling Java from Python"
timestamp: 2019-06-17T20:30:01
tags:
  - Java
  - Python
  - jpype
published: true
books:
  - python
author: szabgab
archive: true
---


```
pip install JPype1
```

{% include file="examples/python/java.py" %}

See the [jpype userguide](https://github.com/jpype-project/jpype/blob/master/doc/userguide.rst)

I tried this Python 3.7.3 running on Linux.

```
$ java -version
openjdk version "1.8.0_242"
OpenJDK Runtime Environment (build 1.8.0_242-8u242-b08-0ubuntu3~19.10-b08)
OpenJDK 64-Bit Server VM (build 25.242-b08, mixed mode)
```


```
$ sudo apt-get install openjdk-8-jdk-headless

$ javac -version
javac 1.8.0_242
```

{% include file="examples/python/java1/Calculator.java" %}
{% include file="examples/python/java1/org/pkg/MyMath.java" %}
{% include file="examples/python/java1/calc.py" %}

```
javac Calculator.java
javac org/pkg/MyMath.java
python calc.py
```

Directory layout (before running javac):

```
.
├── calc.py
├── Calculator.java
└── org
    └── pkg
        └── MyMath.java
```

