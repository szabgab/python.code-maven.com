# What is testing, really?

In reality, however, many times we don't get exactly the expected output. Instead there is a small (or not so small) difference.
That's the bug.

So our equation actually looks like this:

```
Fixture + Input = Expected Output + Bugs
```

The goal of (automated) testing is to make it easy and cheap to notice when these bugs creep in.

To put it in other words, when you write your code you can check if the result is as expected either manually or by writing
some automated tests. The question is, how will you know your piece of code still works half a year from now when someone made
some changes to some other part of the code?

Will you repeat all the manual tests you did earlier? You won't have time for that.

On the other hand if you automated your tests in the first place, then you can easily, quickly and cheaply run them again
and you can verify if everything still works as earlier or if a bug appeared.


You can do this as many times and as frequently as you like. Meaning that even during active development you can constantly, quickly and cheaply check if you,
or any of your co-workers have broke anything.


It is obviously not perfect. As we saw Flask has an impressive a 92% test coverage. It means that 8% of the code is not executed in any of the tests.
So if some breaking change happens in any of those lines then even these tests won't catch it. Moreover even in the 92% of the code that was tested, there might be bugs.
Bugs that might appear at circumstances that were not tested.

However, having such a high test coverage will give us a lot more confidence in our code. We'll be able to make changes a lot faster knowing that if we make a mistake
we have very good chances of noticing it before it reaches anyone else. We also know that if we do find a bug that was not reported by our test suit, then we will be
able to add a test that will expose that bug and so when we fix the bug we'll be confident that this bug won't reappear.


