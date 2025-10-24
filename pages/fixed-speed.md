---
title: Fix speed
timestamp: 2025-10-24T13:30:01
author: szabgab
published: true
description:
tags:
    - speed
---

Based on a recent discussion about teaching programming and if speed of execution matters I wrote this snippet.


{% include file="examples/fix-speed/calculate.py" %}

Can you suggest how to improve the speed of this code?

In order to try it create a file called `config.csv` with this content

{% include file="examples/fix-speed/config.csv" %}

and then run

```
time python3 calculate.py 1000 500
```

On my computer this takes 5 seconds to run.




