---
title: "Python package dependency management - pip freeze - requirements.txt and constraints.txt"
timestamp: 2021-09-18T07:30:01
tags:
  - python
  - pip
published: true
books:
  - python
author: szabgab
archive: true
show_related: true
---


Making sure the dependencies of a large project work well together is not an easy task. In this article I try to describe a process that might work for you as well.

TL;DR

Keep the list of immediate dependencies in <b>requirements.txt</b> without declaring version numbers.

Keep the output of <b>pip freeze</b> with the specific version numbers in <b>constraints.txt</b>.


## Getting started

Create two empty files: <b>requirements.txt</b> and <b>constraints.txt</b> and add both of them to version control.

## Converting from old requirements.txt with constraints

If you already have a <b>requirements.txt</b> file that has all kinds of constraints in it, then you can do the following:

* Make sure it is checked into version control.
* Install everything using the requirements.txt.
* Run your tests.
* Run `pip freeze > constraints.txt`
* Add the new file to version control.
* Remove the constraints from the requirements.txt file.


## Adding new packages

As we need new python packages add their names to the requirements.txt file without any restriction and run

```
pip install -r requirements.txt -c constraints.txt
```

Verify that the new package works as needed. (Run your own tests). Then run

```
pip freeze > constraints.txt
```

Then commit both <b>requirements.txt</b> and <b>constraints.txt</b> to your version control system.

## Fresh installations

Later, any time you want to install packages to a fresh installation use

```
pip install -r requirements.txt -c constraints.txt
```

## Require specific version of a package?

If your application requires a specific version of a package add that information to the requirements.txt file.

```
package-name==SPECIFIC_VERSION
```

## What if we cannot install?

Because the required new package and the constraints file require different versions of something?

You can try to adjust the version of the problematic packages listed in the constrains.txt file and see if any of them satisfies all the
requirements and then run your tests and make sure your code still work after changing the constraint and reinstalling all the dependencies.


## Upgrade a package

If later you need to upgrade one of your immediate dependencies because you need some feature that only in a newer version exist then
add this information as a minimum requirement to the requirements.txt file: <b>package>=SOME_VERSION</b>


## Removing required packages

We can simply remove the package from the requirements.txt file. The fact that it and its dependencies are listed in the constraints.txt file
does not matter. They won't be installed. The only problem is that now we might have some lines in the constraints.txt file that are not relevant
any more and that might impact a later installation. If you do the regular maintenance as described below then this will be cleaned up the next time
you do it.

## Regular maintenance

You can get by with the same versions of your dependency for a long time, but eventually you'll reach a point when you need a newer version of
one of your dependencies. For example because it has a new feature that you need, or because there is a bug-fix in it, or maybe even a security fix.

However every upgrade has the risk of breaking something in your application. So many people try to avoid it. They even use the expression:
"If it isn't broken don't fix it.". To which I usually amend: "When something breaks then panic!".

We know that upgrading a package that is several years old to its current version carries a lot more risk
than doing regular upgrades. Checking regularly if you can upgrade also has the advantage that if there some breaking change you can report it
to the package maintainers soon after it happens. That report might help them revert the change that breaks your code if possible.

You can do all the upgrades all at once, or you can cherry-pick.

For the former run:

```
pip install --upgrade -r requirements.txt
```

That will try to upgrade all of your dependencies to the latest.

This might introduce many issues if you have not done it for a long time, but usually should be quite smooth.

Then of course you need to run all your tests to verify that your code still works as it was expected earlier.

If doing all the upgrade at ones is still something you'd like to avoid, you can cherry-pick which packages you upgrade.

You can upgrade a specific package:

```
pip install --upgrade PACKAGE
```

You can also remove some or all of the entries from the <b>constraints.txt file</b> and then run:
<b>pip install --upgrade -r requirements.txt -c constraints.txt</b>.

The run your tests. You do have a good set of tests, don't you?

In you Continuous Integration (CI) system have a task that would install your dependencies without the constraints.txt file. Just with
<b>pip install -r requirements.txt</b> and then run your tests. If this fails check what is the source of the problem and report it or fix it.


## Compability with old file formats

This is not strictly related, but I just encountered this problem at a client. A newer version of [h5py](https://www.h5py.org/) could
not read a file created by an older version. In our regular tests we did not notice this problem as our regular tests never tried to open the old files.
They only read in from files that were created in the same test-run with the same version of h5py.

So add examples of every file-format created by your code to your test-data and make sure part of your testing is to read in these files.


