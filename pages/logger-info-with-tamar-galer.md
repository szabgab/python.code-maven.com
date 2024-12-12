---
title: logger.info(f"Don't Give all your {secrets} away") with Tamar Galer
timestamp: 2024-12-12T16:30:01
author: szabgab
published: true
description:
tags:
    - logger
---

Explore the transition from developer to security researcher, addressing log safety in applications. Learn common mistakes, practical Python solutions, and empower developers to protect against data exposure.


2025.01.06

<a class="button is-primary" href="https://www.meetup.com/code-mavens/events/305045436/">register</a>

In my seven years as a software developer, I've primarily worked in teams composed solely of developers. However, my recent transition to a team of security researchers has opened my eyes to a crucial aspect that often goes unnoticed: log safety in applications.

My exposure to the application security ecosystem and real-life security breach analysis has opened my eyes to recognize code security issues, including the prevalence of sensitive information, tokens, passwords, and payment details, in plaintext logs. This may lead to severe data breaches, financial losses, and all kinds of catastrophes.

This talk will dive into the fatal mistakes developers often make that can result in the disclosure of sensitive information in logs. We'll explore the types of sensitive data in logs.

I'll share my personal experiences as a developer on a security research team and shed light on the often-overlooked consequences of insecure logging practices. We'll discuss practical patterns to safeguard sensitive information in Python applications, including identifying and redacting sensitive data before it reaches log files, and implementing secure logging practices.

By the end of this talk, developers will be equipped with the knowledge and tools to protect sensitive data from accidental disclosure and safeguard their applications from the perils of sensitive data exposure. Embrace the journey towards log safety and ensure your code remains secure and confidential.


![Tamar Galer](/images/tamar-galer.jpg)
