---
title: daffodil, data frames for optimized data inspection and logical processing with Ray Lutz
timestamp: 2025-02-18T16:30:01
author: szabgab
published: true
description:
tags:
    - data
    - data frame
---

<a class="button is-primary" href="https://www.meetup.com/code-mavens/events/305731787/">register</a>

2025.03.05

Speaker: [Ray Lutz](https://www.linkedin.com/in/raylutz/)

![Ray Lutz](images/ray-lutz.jpeg)

[daffodil](https://github.com/raylutz/daffodil) (data frames for optimized data inspection and logical (processing)), which can create data frame instances similar to pandas, but using conventional python data types.

This means no conversion to/from the Pandas world, which I have found
from testing has a very high overhead. In fact, unless you plan to do at
least 30 repetitive column-based operations (like sums, etc) then you
should just stay in python world and avoid the conversion time, and you
win. But for many, time is not of the essence, or they stay in Pandas
world and never need any python. The syntax is easy to use and I am
extending it to use SQL database to allow for large table size and use
of the robust joins, etc. The SQL part is under work and not released yet.


