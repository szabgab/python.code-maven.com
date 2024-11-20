---
title: Creating an istallable Python package to print hello world
timestamp: 2024-11-04T14:30:01
author: szabgab
published: false
description:
tags:
    - Python
todo:
    - TODO
---



```
$ tree hello-package/
hello-package/
├── hello
│   ├── app.py
│   └── __main__.py
└── setup.py
```

{% include file="examples/hello-package/hello/app.py" %}


{% include file="examples/hello-package/hello/__main__.py" %}


{% include file="examples/hello-package/setup.py" %}


`cd` into the `hello-package` folder and we can run the code using `python -m hello`




