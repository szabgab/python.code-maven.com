---
title: "Print version number of Python module"
timestamp: 2019-01-17T23:30:01
tags:
  - python
  - __version__
  - version
  - bash
published: true
author: szabgab
archive: true
---



## Check the module version number on the command line

```
python -c"import urllib3; print(urllib3.__version__)"
```

## Bash Shell script to check Python module version number

{% include file="examples/shell/python_module_version.sh" %}

Use:

```
chmod +a python_module_version.sh
./python_module_version.sh urllib3
```


## Check Python module version number with a Linux Bash Shell function

{% include file="examples/shell/python_module_version_function.sh" %}

