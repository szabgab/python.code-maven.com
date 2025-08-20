# Testing demo methodology

We won't delve deep into the capabilities of these testing libraries. We will only use a very simple example to
demonstrate how to write tests.
First we'll see a test that is passing, meaning the actual result is the same as the expected result.

Then we'll also see a failing test where the actual result is different from the expected result. This usually indicats a bug in our code, though we always have to keep an open mind. The bug might be in the test or we might have an incorrect expectation.

We are not perfect, we just keep trying to improve.


* Have a simple AUT - Application Under Test with an obvious bug.
* Write a passing test.
* Write a failing test exposing the bug.

