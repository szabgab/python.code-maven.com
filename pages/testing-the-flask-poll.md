---
title: "Testing the Flask poll"
timestamp: 2015-02-18T13:30:01
tags:
  - unittest
  - assertRegexpMatches
  - assertEqual
  - assertTrue
published: true
books:
  - flask
  - python
author: szabgab
archive: true
---


Previously we have [created a poll using Flask](/a-polling-station-with-flask).
I would really like to go on adding a few more features, but I also want to make sure future changes
won't break the existing features. As the application growth, I won't be able to manually test the
whole application every time I make a change, so I'd better write some automated test that I can
run any time.


Even before that, I need to do something else:

## Administative changes: .gitignore

I avoided touching this in the [first episode](/a-polling-station-with-flask), but I had to work around the issue.
If I run `git status` in the repository, I get the following output:

```
On branch master
Your branch is up-to-date with 'origin/master'.
Untracked files:
  (use "git add <file>..." to include in what will be committed)

    .poll.py.swp
    data.txt

nothing added to commit but untracked files present (use "git add" to track)
```

The `data.txt` contains the results of the poll as I tried it, and `.poll.py.swp`
is a temporary file created by vim as I am editing the `poll.py`. I would like to make sure neither
of those will be added to Git. So I create a new file called `.gitignore` and
added the following entries:

```
*.swp
data.txt
```

This means from now on I'll be able to run `git add .` and I would not have to worry
that I add these files by mistake.

Depending on your environment and your editor you might want to add other
files and/or other expressions to the `.gitignore` file of your project.
I have written an article explainig a bit more about
[generated files and VCS-es](https://perlmaven.com/dont-keep-generated-files-in-version-control).
Though that article has some Perl specific elements, it also provides some general explanation.
In any case, GitHub maintains a [repository of gitignore files](https://github.com/github/gitignore)
for various languages, projects, editors and operating systems. That can be a useful starting point.

If I run `git status` again, I'll see the following output:

```
On branch master
Your branch is up-to-date with 'origin/master'.
Untracked files:
  (use "git add <file>..." to include in what will be committed)

    .gitignore

nothing added to commit but untracked files present (use "git add" to track)
```

So now I need to add the `.gitignore` file to the repository.

This is actually a good thing as this means if other people want to contribute to this project
they will automatically have the `.gitignore` file and it will help keep the repository clean.

```
$ git add .
$ git ci -m "add gitignore"
```

[commit](https://github.com/szabgab/flask-poll/commit/d2770f0810ddbbf58c1efd323da9b5892edd50ab)

## Setting up unittest

If we keep working on the Git master branch then when we later find out that our direction was wrong, it will be hard to go back
to where we started. So it is better that we start working on branches and merge them to the master branch when we are comfortable
with the changes.

Let's create a branch for the test code:

```
git checkout -b test
```

Once we are in the branch we create a file called `poll_test.py` in the root of our application.
This will be our test script. We will use the [unittest](https://docs.python.org/2/library/unittest.html)
framework that comes with Python.

The first version of our file looks like this:

{% include file="examples/flask/poll5/poll_test.py" %}

We start by importing the `unittest` framework, but we also import `poll`, our own application.
We can do this without automaticlly launching the web server becuse in the `poll.py` file we had:

```python
if __name__ == "__main__":
    app.run(debug=True)
```

which means the `app.run` will be only executed if `poll.py` was ran as a script, and it won't 
automaticlly run if it is loaded as a module.

Next we create a class that inherits from `unittest.TestCase` and we put 3 methods in it:

Every method that starts with `test_` is considered a test separate test method. If we had more of
those they would be executed one after the other. In addtition unittest allows us to have some generic
methods.

The `setUp` method, if implemented will be called every time before the system
runs one of the test_... methods. This should set up the testing environment and create the <b>fixture</b>.
This can include creating a database, fillin initial data etc.

The `tearDown` method, if implemented, will be called after each one of the test_... methods
and it should clean up anthing the test might have created. This can include dropping the database.
Removing temporary files, etc.

In our case our "database" is just a file in the current directory. We have access to the the name of
the file via the `filename` method of the `poll` object. Both in the setUp and in the tearDown
we will delete the file if it exisst. In addition we call the
[test_client](http://flask.pocoo.org/docs/api/#flask.Flask.test_client) method provided by Flask.

In the individual test function we are going to use this object to interact with our application.

The actual test code is in the `test_main_page` method. We use the object we received from the `test_client`
method to send a `GET` request to the `/` URL.

It executes the appropriate calls and returns a [Response](http://flask.pocoo.org/docs/api/#flask.Response) object.
We can interrogate this object now. The `data` method will return the HTML content that was generated by this call.
This is the same HTML content the user would receive if she accessed the same URL.

We can then use one of the assertions of unittest.

Specifically we use the 
[assertRegexpMatches](https://docs.python.org/2/library/unittest.html#unittest.TestCase.assertRegexpMatches).
It receives the two parameters. The first one is the text we are checking, the second is a string that can be used as a Regexp.
If the Regexp matches, the assertion will pass, otherwise it will fail. We have two assertions here, one is checking if the
HTML title is as expected, the other one is checking if one of the radio selectors is there.

Checking an HTML with regexes is not the best approach, but at this point it is quite reasonable. Especially as we have
full control over the HTML being generated.

We can then run the test using `python poll_test.py`. The output looks like this:

```
.
----------------------------------------------------------------------
Ran 1 test in 0.037s

OK
```

Everything looks fine, the test is passing. We can now commit this to the Git repository

Unfortunately running `git status` I noticed there are two new files now:

```
poll.pyc
poll_test.py
```

Besides the test file we created, now that we use `poll.py` as a module, Python has created the compiled
version of the file with `pyc` extension. This is another generated file we don't want to keep in version control,
so before adding our new test file, let's make sure we'll ignore all the possible `pyc` files:

## gitignore *.pyc files

Edit the `.gitignore` file and add `*.pyc`

```
$ git add .gitignore
$ git commit -m "gitignore pyc files"
```

[commit](https://github.com/szabgab/flask-poll/commit/d2770f0810ddbbf58c1efd323da9b5892edd50ab)

Now we can go and [commit](https://github.com/szabgab/flask-poll/commit/39869e56c6e112855082f3adb457c39b54f4c44b) the first version of our test script:

```
$ git add .
$ git commit -m "start testing the poll"
```


## Test the results

While logically the next step would be to select one of the values, click on the vote button and see
if this works, my evil self told me to check something else first. What happens if we look
at the results page before we have received any results?

So I added the following code to `poll_test.py`:

```python
    def test_empty_result(self):
        rv = self.app.get('/results')
        print(rv.data)
        self.assertTrue(True)
```

In this test function we fetch the `/results` page, and not knowing what really to expect,
we just print it out to the console using `print(rv.data)`.
In order to have some kind of an assertion in this test function I've added the meaningless
`self.assertTrue(True)` that asks if True is really True. This will pass no matter what.

The result of running the test script proves my suspition that something is broken.

`python poll_test.py`

```
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>500 Internal Server Error</title>
<h1>Internal Server Error</h1>
<p>The server encountered an internal error and was unable to complete your request.  Either the server is overloaded or there is an error in the application.</p>

..
----------------------------------------------------------------------
Ran 2 tests in 0.051s

OK
```

Going back to the [source code in the first article](/a-polling-station-with-flask) you might
notice that in the `/results` route I am trying to open the `data.txt` file. Before the first vote this file does
not exists and thus the `open` will throw an exception. We should either catch that exception or check
if the file exists before trying to open it. Or both.

In any case, this should not give an `Internal Server Error`.

At this point I don't want to fix the code yet, I am sure there are plenty of other bugs, so let's just turn this code
into a test. I am still not sure what should be displayed if there are no results yet, but I am sure the request should return
a status of "200 OK".

Let's put this in code:

```python
    def test_empty_result(self):
        rv = self.app.get('/results')
        self.assertEqual(rv.status_code, 200)
```

If we run the test script again: `python poll_test.py` we get the following result:

```
F.
======================================================================
FAIL: test_empty_result (__main__.PollTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "poll_test.py", line 26, in test_empty_result
    self.assertEqual(rv.status_code, 200)
AssertionError: 500 != 200

----------------------------------------------------------------------
Ran 2 tests in 0.047s

FAILED (failures=1)
```

At the top we can see the letter `F` indicating that one of the test functions failed and
a dot `.` indicating that another test function succeeded. Those are the two test function we have in the file.

Then later we can see that the `AssertionError` was that `500 != 200`. That's good. Our test caught the
problem and gave a proper explanation. Now we can go on adding more test and adding more features,
and we can be sure that we won't forget about this problem.

Actually, having this failure reported every time we run our test script will be probably a bit too much.
Every time we'll have to remind ourself why do we get a failure. If we work in a company, our managers
will be certainly worried about the test failures. Even if they were the ones who decided to delay fixing the problem.

So let's mark this test as a "known failure" or "expected failure", or if you are familiar with the testing tools
of Perl, then think about this as a "TODO test":
We put `@unittest.expectedFailure` the 
[@unittest.expectedFailure](https://docs.python.org/2/library/unittest.html#unittest.expectedFailure),
the expected failure decorator on the test function:

```python
    @unittest.expectedFailure
    def test_empty_result(self):
        rv = self.app.get('/results')
        self.assertEqual(rv.status_code, 200)
```

If we run the test again using `python poll_test.py` we get a much nicer report:

```
x.
----------------------------------------------------------------------
Ran 2 tests in 0.050s

OK (expected failures=1)
```

It still indicates that there was an expected failure, but it won't be so disturbing as earlier.

We can now even add an additional assertion to the test script. If there are no result yet,
the results page should show this text: `No results yet`

We add the following asssertion:

```python
        self.assertRegexpMatches(rv.data, 'No results yet')
```

The full script looks like this:

{% include file="examples/flask/poll6/poll_test.py" %}

We can now [commit](https://github.com/szabgab/flask-poll/commit/a42db4b7cda54e78089f2a2969b6062c7f6ec21b) our changes.

```
$ git add .
$ git ci -m "test the empty results page"
```


## Test a vote

We add the following test function:

```python
    def test_vote(self):
        rv = self.app.get('/poll?field=Flask')
        self.assertRegexpMatches(rv.data, '<h1>Thank you for submitting your vote for</h1>')

        rv_results = self.app.get('/results')
        self.assertRegexpMatches(rv_results.data, '<li>Flask 1</li>')
        self.assertRegexpMatches(rv_results.data, '<li>Django 0</li>')
```

In this function the first step in this test function is to send a vote to the `/poll` route
and check if the response from that page has the thank-you text.

The second step is to fetch the `/results` page and see of the number of votes on Flask is 1
while the number of votes on the other values is 0. We could check all the other
values, but in this case we only looked at the number of votes for Django.

This brings our test file to look like this:

{% include file="examples/flask/poll7/poll_test.py" %}

The result of running the test script looks similar to the previous output except that
we ran now 3 test functions. One of them is still an <b>expected failure</b>.

```
x..
----------------------------------------------------------------------
Ran 3 tests in 0.047s

OK (expected failures=1)
```

We can now [commit](https://github.com/szabgab/flask-poll/commit/faee8ffa38668499678832450bf7800dd2de3e64) our changes.

```
$ git add .
$ git commit -m "test voting"
```


## Merge to master

Finally, now that we are satisfied with our changes, we can merge the branch back to the master branch:

```
$ git checkout master
$ git merge test
```

This is a so called "fast-forward" and thus won't record another commit.

The we can delete the test branch:

```
$ git branch -d tests
```


## More testing

If you are interested how else to test a Flask based application, see
what the Flask documentation has about [testing Flask](http://flask.pocoo.org/docs/testing/).



