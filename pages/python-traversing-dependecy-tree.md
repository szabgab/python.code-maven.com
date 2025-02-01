---
title: "Python: traversing dependency tree"
timestamp: 2019-07-19T15:50:01
tags:
  - read
published: true
books:
  - python
author: szabgab
archive: true
---



{% include file="examples/python/project/traversing_dependency_tree.py" %}

{% include file="examples/python/project/a.txt" %}

{% include file="examples/python/project/b.txt" %}

{% include file="examples/python/project/a.txt" %}


```
$ python traversing_dependency_tree.py a

Processing a
Processing b
Processing e
Processing d
Processing c
Processing f
Processing g
Processing d
{'d', 'g', 'c', 'b', 'a', 'e', 'f'}
```

