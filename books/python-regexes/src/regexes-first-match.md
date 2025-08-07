# Regexes: first match

{% embed include file="src/examples/regex/search.py" %}

In this first example we are going to see the basic mechanism of using Regular Expressions in Python. Therefore we are using a very simple regular expression.
We have a string in the `text` variable and we would like to know if the series of characters `lac` can be found in it.

We need to import the [re](https://docs.python.org/3/library/re.html) library that implements the regex engine. It has several methods. In this example we are using the [search](https://docs.python.org/3/library/re.html#re.Pattern.search) method.
t receives two parameters. The first one is the regular expression and the second one is the string in which we are searching. You might have noticed that the regex string is prefixed with the letter `r`.
That tells Python that this is a **raw string**. In this case it is not needed as the regex does not contain and backslashes `\` but I feel it is a good idea to always use it in regular expression so we won't forget it.


The search method returns either an object representing the match or `None`, if it could not find any match.

We can use this value in a conditional statement that will be `True` if there was a match and it will be `False` if there was not match and the value in `None`.

If there is a match you can call the `group()` method. Passing 0 to it will return the actual substring that was matched.

In this first example we use a very simple regular expression that did not have any special characters. We knew exactly what we are looking for. In reality in such cases there is no need to use the `re` library.
We could simply use the `text.find('lac')` or we could use the `in` operator and ask: `'lac' in text`, but I wanted to show the syntax used with the `re` library.

In the second example we were searching for **dog**, but as there is no dog in this text the `search()` method will return `None`.


---
* r
* re
* search|re
* group|re


