---
title: "Testing invariants, not just examples: Property-based testing with Hypothesis"
timestamp: 2026-10-27T08:30:01
author:
published: true
description:
tags:
---

## Description

Some calculations are too important to get wrong, but surprisingly difficult to test. They often live inside code that also talks to a database, calls an API, or depends on a framework, making even a simple test complicated.

What if we could take the calculation out of all that and test it on its own?

In this talk, we'll take a small piece of logic from a real application and turn it into a plain Python function. We'll start with the kind of example-based tests we're all familiar with. Then we'll ask a different question:

What should always be true, no matter what numbers we give it?

That shift takes us from testing individual examples to testing invariants (rules that should hold for every valid situation).

We'll use Hypothesis to explore those rules automatically. Instead of deciding in advance which examples to test, we let the computer generate many different situations and try to find one that breaks the rule. And when it does, Hypothesis reduces the problem to a small example that makes the bug easier to understand.

The examples are deliberately small, and you don't need any domain knowledge. The goal is to explore a way of thinking about code and tests that can help when a calculation is buried inside a larger application.

Level: Intermediate, comfortable with Python functions and basic testing with pytest or unittest.

## Bio

[Marlene Marchena](https://www.linkedin.com/in/marlene-marchena-23109329/) is a data scientist and Python developer with a background in decision support, particularly in credit risk and supply chain planning. She is now working independently on inventory replenishment and supply chain analytics.

Marlene is also the organiser of [PyLadies Brussels](https://www.meetup.com/pyladies-brussels/), where she helps create opportunities for people to learn and share knowledge about Python.


## Length

60 min


<a class="button is-primary" href="https://luma.com/7d30pgma">register</a>


