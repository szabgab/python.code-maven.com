---
title: Size of integer in Python
timestamp: 2024-07-05T13:30:01
author: szabgab
published: true
description: A Python variable can hold any integer, but this flexibility comes at a price.
tags:
    - getsizeof
    - int
---


In some programming language and in `numpy` as well, you have some pre-defined integer types taking up 8, 16, or even 256 bits of memory.
Accordingly they can hold integer numbers to the appropriate exponent of 2. So an 8-bit unsigned integer uses 8 bits (1 byte) and can hold values between 0-255 (that is 2**8-1).

Python hides the need to make a decision and a variable in Python can hold an arbitrarily large integer. This, however comes at a price.
The following little program demonstrates, using the powers of 2, that Python can hold very large integers. It also shows that even for a small integer such as 1, Python uses
28 bytes(!) very wastefull compared to other programming languages and to `numpy`. It also demonstrats how the used memory will grow as the number grows.


{% include file="examples/size_of_integer.py" %}


{% include file="examples/size_of_integer.txt" %}


