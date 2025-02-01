---
title: "Automated tests for sssimp, a simple static site generator in Python"
timestamp: 2022-10-09T15:50:01
tags:
  - GitHub
  - tests
description: "Creating test that are also documentation and a tutorial can be quite valuable"
types:
  - screencast
published: true
books:
  - testing
  - python
author: szabgab
archive: true
show_related: true
---


As earlier I bumped into [sssimp](https://github.com/Tina-otoge/sssimp) while looking at the Python packages
on [PyDigger](https://pydigger.com/stats). It is a Simple Static Site generator written in Python. It included
a link to its GitHub repository but it did not have any type of Continuous Integration (CI) configured.

Not only that, but when I looked at the repository I noticed it does not have any tests.

So I thought I could add both, but to do that I needed to understand how it works.


{% youtube id="EKKw6X0uISE" file="python-automated-test-for-sssimp-simple-static-generator.mp4" %}

Luckily in the README I found a reference that there is an example in the <b>example</b> branch. I checked it out
and after a few minutes figured out how to run generate the site from the example input data.

## The plan

I already dealt with similar cases so here is what my plan was:

* Create one or more examples (based on the one in the example branch)
* Generate the results from each example, manually inspect if this is what we expect, and save them in a directory for expected output.
* The tests then would generate each example and then compare the results to the expected output. They should be the same.
* When there is some expected change, either because the input files of an example changed or because the processing changed,
        the authors should be able to verify the changes in the output and then they should be able to update the expected output easily.
* All this should be in the same branch where the development takes place so the expected output is always aligned with the current version of input and code.
* Each example could show one specific feature of the system or they could be like a tutorial showing how one builds a site with more and more complex features. In any case the examples are used both as documentation and as tests.

I opened [an issue](https://github.com/Tina-otoge/sssimp/issues/5) describing my idea a bit more briefly. Soon I got a reply from Tina, the author. She also assigned the issue to me.

## The implementation

So here is what I did.

* I created a new branch based on the <b>master</b> branch.
* Created a directory called <b>examples</b> and in it create a very simple example in the <b>examples/01-basic/</b> subdirectory. It had a subdirectory called <b>input</b> with all the necessary files for the most basic example.
        (And juts to clarify, this is short sentence, but this took me quite some time.)
* Then I ran <b>PYTHONPATH=src python -m sssimp --input examples/01-basic/input example/01-basic/output</b> that generated the output.
* I looked at the output files. They looked good. As much as I can tell.
* Then I added the following two files

{% include file="examples/sssimp/test_examples.py" %}

{% include file="examples/sssimp/conftest.py" %}

## Running tests

Now I can run the tests with

```
pytest -sv
```

If I make some changes to the input files or to the code then the test will fail and will show me changes in the output.
e.g. something like this:

```
File with difference: index.html
---
+++
@@ -5,6 +5,6 @@
 	<body>
 		<h1>Title</h1>
 		<p>Content:</p>
-<h1>Head 1</h1>
+<h1>Head new</h1>
 	</body>
 </html>
```

Then, if I think the changes I are as I wanted them I can run

```
pytest --save
```

This will re-generate the output and replace the expected output with the new files. I can inspect them again, now the full version of the file.
If they are as I really wanted them then I can commit all the new files.
If I decide this is not what I wanted I can reset the content of the output directories and go back to my earlier expectation.

## Continuous Integration (CI) with GitHub Actions

For the continuous integration I added the following file as <b>.github/workflows/ci.yml</b>

{% include file="examples/sssimp/.github/workflows/ci.yml" %}

It runs on 3 different Operating Systems and 3 different version of Python.

After pushing the whole thing to my fork on GitHub I noticed that the tests are failing on both OSX and Windows.
On OSX the problem was the order of entries. At first I considered this a bug in the Python module, but then I figured I could use some Jinja
instructions to force the list to be in the same order every time.

However in the case of Windows I found that it looks like a real bug. In the <b>href</b> of some links Windows would insert a back-slash <b>\</b>
between the parts as is normal for Windows pathes, but incorrect for URLs. So I left that failure in the CI system.





