---
title: "Python's Achilles Heel: C++ and Python Interop for Audio Processing"
timestamp: 2026-09-08T14:30:01
author:
published: true
description:
tags:
---

Unfortunatelly this event has been cancelled

## Description

Python is pleasant to write but slow to run once the data gets big. Using a silence-stripping algorithm as an example, I look at why the per-block loop costs so much (158 million samples in an hour of 44.1 kHz audio), then move it into C++ for SIMD and pre-allocated memory, with Boost.Python handling the bridge.

## Bio

[Ron Shabi](https://ronsh.net/) is a Computer Science student at the Open University of Israel, focusing on networks and operating systems. He completed a B.A. in Accounting and Economics at Bar-Ilan University before changing course.

## Length

30 min
