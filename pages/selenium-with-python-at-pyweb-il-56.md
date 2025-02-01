---
title: "Selenium IDE and the Selenium Driver in Python (PyWeb-IL #56)"
timestamp: 2016-09-05T22:30:01
tags:
  - Selenium
  - Python
published: true
books:
  - python
author: szabgab
archive: true
---


On 5 September 2016 I gave a talk and a live demonstration of Selenium IDE and
the Selenium Driver of Python at [PyWeb-IL](http://www.meetup.com/PyWeb-IL/).

These are some notes for the presentation.


We talked about [Selenium IDE](http://www.seleniumhq.org/projects/ide/) the plugin for Firefox.

Mentioned the [FirePath](https://addons.mozilla.org/en-US/firefox/addon/firepath/) plugin to interrogate a DOM using CSS selectors or XPath.

I've also mentioned the [Accessibility Developer Tools of Chrome](https://chrome.google.com/webstore/detail/accessibility-developer-t/fpkknkljclfencbdbgkenhalefipecmb?hl=en) that has nothing to do with Selenium, but a recent interview I made, that will be published on the [CMOS podcast](/cmos) inspired me to talk about. 

We looked at the test for the web site of [Jewish Diaspora house](http://dbs.bh.org.il/).
It is not written well, but it can give a few ideas. Especially to people who listened to the talk.

{% include file="examples/python/pyweb-il-56/test_dbs.py" %}

We also looked at the web site of the [Wellington City Council](http://wellington.govt.nz/)
that has responsive-design, and we had a script to test the responsiveness, though we have not looked at it.

{% include file="examples/python/pyweb-il-56/test_wellington.py" %}

I've included these examples so you can learn from <b>my</b> mistakes.
These were both examples in progress that should be further improved for real use.

## Additional comments by Miki Tebeka

An example on running selenium "headless" (without screen)
[Dockerfile](https://github.com/tebeka/selenium/blob/master/Dockerfile)
and
[docker-test](https://github.com/tebeka/selenium/blob/master/docker-test.sh)



