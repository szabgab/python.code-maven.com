# Handling failing tests (bugs)

Let's assume you already have some code with some tests and all the tests are passing.

You encounter a bug or someone reports a bug.

The first thing you probably want to do is to reproduce the bug locally. Without being able to reproduce a bug it is usually very hard to fix it.

Once your reproduced the bug you will probably want to convert that into a test case.

Actually if you already have a good testing environment, it might be easier to just write the test that fails due to the bug.

Now what?

If you have the time to fix the bug then you'll probably do that, but what if you are in the middle of something and you know fixing this bug will take a lot of time? What should you do with the failing test?

You can't just add it to the code-base as that will mean your CI starts failing and people start asking question.

You don't want to hide the test either.

You can mark is a test that is expected to fail. (in other programming languages it is called a TODO-test).

Your test will still run and it will still fail, but pytest will report it as expected to fail and it will not break your CI.

Then when you have time to fix this bug, you already have the test and you just need to remove the `xfail` mark.

Also if you or someone else accidently fixes this bug, you'll notice.
