# Capture

{% embed include file="src/examples/regex/capture.py" %}

Given that string we would like to extract the number that comes after the `age:`.

The first example shows a regular expression `age: \d+` that will match the characters `age: `, with the trailing space and the one or more digits.
That works and if we check the content of `group(0)` we'll see that it indeed matched what we asked for `age: 23`, hower that's not exactly what we wanted.
We only wanted the number.

So in the second example we put a pair of parentheses in the regular expression around a sub-expression: `age: (\d+)`. This does not impact the matching
and `group(0)` still returns the whole substring that was matched, but now we can also call `group(1)` that will return whatever the sub-expression inside the parentheses matched.


Whatever this sub-expression matches will be saved and can be accessed using the group() method.


---

* `()`

