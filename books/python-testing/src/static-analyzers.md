# Static Analyzers (Linters)

There are various static Analyzers for Python. We'll take a look at a few of them.

Some of these tools will report on stylistic issue (e.g. pus spaces around operators),
others will complain about the lack of documentation, but they can also point at potential bugs.
For example if the same function name is defined twice, or if there is a function that is being used but never declared.

If you wonder how the latter could happen, wouldn't the program crash. Well, if the function is rarely called and there are no tests covering the case when it is used then the softare might run well for a long time before it will crash at 2 am on a Saturday.

We'll also see how to integrate them with testing.
