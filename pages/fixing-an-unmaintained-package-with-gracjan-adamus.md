---
title: Fixing an unmaintained package, spanning Python, C++, nanobind and Github Actions
timestamp: 2026-08-04T10:30:01
author:
published: true
description:
tags:
---

<a class="button is-primary" href="https://luma.com/exyszwcp">register</a>

DESCRIPTION

nanobind is the official successor to the widely used pybind11 library, allowing you to quickly create seamless and maintainable Python bindings for C++ code.

For pybind11, an extension called pybind11_json was developed to easily pass JSON objects between Python and C++. This package has been used in an open-source project that I contribute to. However, when we decided to migrate to nanobind, we discovered a major issue: the nanobind equivalent - which is even linked directly from the pybind11_json README - did not work at all. 

In this talk, I will share the fun (and not-so-fun) parts of my journey to fix this package. I'll go over what pybind11 is and how nanobind improves it. I'll provide a brief overview of the open-source project I was working on, and explain why we needed JSON interoperability. From there, I’ll dive into the specific bugs, quirks, and issues I encountered while resurrecting nanobind_json. Throughout the whole talk I will showcase necessary examples and code snippets.

BIO

Gracjan Adamus is an Applied Computer Science student at AGH University of Kraków. His main interests span GPUs, High-Performance Computing, and open-source software. He is a former Summer Student at the Paul Scherrer Institute and a current Summer Student at CERN. Griger5 @ Github.Here it is 🙂

