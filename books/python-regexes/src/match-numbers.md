# Match numbers

{% embed include file="src/examples/regex/match_numbers.py" %}

Let's take a look at a slightly more interesting example. We a string, some text that also contains numbers. We would like to know what are the numbers in the string.

We use the `\d+` regular expression. It has two parts. `\d` matches a digit. Exactly one digit. That is it matches any of the characters `0-9`.
(Actually it also matches digits in other language, but we'll deal with that later on.)
The `+` sign that follows it is called a **quantifier**. There are several quantifiers we'll learn later on. They all tell the Regular Expression engine how many times the previous sub-expression can match.
The `+` sign means the previous sub-expression can match **one or more times**. The previous sub-expression in our case is `\d`. So the whole expression means: **match one or more consecutive digits**.

Because this expression already contains a back-slash character `\` we need to use the `r` prefix to make this a **raw strings**. (Actually we could prefix the backslash by another backslash and write `'\\d+'`, but that's just ugly.)


* `\d` matches a digit.
* `+` is a quantifier and it tells `\d` to match one or more digits.

## It's a string

It is also good to remember that the `group` function returns strings. So in this case it returned the string `"12345"`. It does not care that we see that as a "number".
If we'd like to use the value for numerical operations we'll need to convert the result using `int()`, `float()` or whatever other means we might find.



## Matching first occurrence

We need to remember that the `search` method matches the first occurrence. So even though in our example there are two places with consecutive digits,
this expression will return the first one. Here we can see that the `group(0)` call is much more interesting than earlier as it reveals the expression matched `12345`.

## How to match the other number?

Before we can come up with a solution we need to be able to describe how to find that other number.
If you don't have much experience with regexes or even programming, you should now think how would you describe that other number.
"Find the first match", which is default behavior would be easy to describe - we just did, but how do you describe this other number? Besides that it is a series of digits.

Especially you nee to think about other cases like these:

```python
line = 'There is a phone number 12345 in row number 37 and an age: 23'
line = 'There is a phone number 12345 in this row and an age: 23 and also 42 dogs'
line = 'There is a phone number 12345 in this row and an address: 23 and an age: 17'
```

Are we looking for

* The 2nd number in the string?
* The last number in the string?
* The number written immediately after "age:"?
* The first number written immediately after ":"?


I think all 4 of these descriptions would yield the exact same answer in our original example, but we would reach totally different results with the 3 additional examples.

So first you need to know how a human would be able to find the right answer and then you can write the code (or ask AI to write you the code) to do the work.


---

* r
* \d
* group


