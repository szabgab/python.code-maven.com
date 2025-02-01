---
title: "Find first stopword in a text using Python"
timestamp: 2020-12-01T07:30:01
tags:
  - filter
  - next
  - split
description: "Given a list of stop-words and a text, find the first word in the text that is in the list of stop-words."
published: false
books:
  - python
author: szabgab
archive: true
show_related: true
---


Given a list of stop-words and a text, find the first word in the text that is in the list of stop-words.
I've dealt with a simpler case of this in the article on how to [find the first element in Python list that matches some condition](/python-find-first-element-in-list-matching-condition),
but let's see the case here.


I did not want to include a long text in the example, so instead of that I used the <b>requests</b> module to download an HTML page.
Then I used the `split` method to cut it up along white-spaces. I know this will not be word-by-word as it will include punctuation
and other special characters in the "words", but for the sake of this example it is good enough.

## The algorithm

Version 1: Go over each word in the text and check if it appears in the stop-word list. Better yet, convert the stop-word list to be a <b>set</b> and
look it up there.

Version 2: For each word in the stop-list find the first occurance in the text using the <b>find</b> function. Discard the words that returned
-1 meaning they were not found. Sort the stop-words based on the first occurance. The first one wins.


My gut feeling was that the first version is easer to implement and it is much faster.
Looking at the solutions I still think the first one is simpler code and it is faster, but how can be sure in the latter?

Does it even matter?

Maybe in another article I should benchmark them.

In any case the speed is only relevant if the text is big and there are many stop-words. What exactly "big" and "many" mean here is a good question.
That's why one needs to first measure the run-time. Then if it too long then profile the code to see what is the bottle-neck an only then optimize the code.


## The code to download the text and split it to "words"

```
import requests
res = requests.get('https://www.lipsum.com/')
text = res.text
words = text.split()
```

## Create fast lookup for the stop-words

The time to check if an element exists in a <b>list</b> is proportional to the mnumber of elements in the list. O(n).

The time to check if an element is in a <b>set</b> is constant. Independent of the number of elements.  O(1).

See [Time complexity](https://en.wikipedia.org/wiki/Time_complexity) for far more information then you ever wanted to know about it.

```
stop_words = ['apple', 'banana', 'peach', 'melon', 'Lorem', 'Ipsum']
words_set = set(stop_words)
```


## Version 1 using a loop

This is a solution for the first algorithm using a for loop.

{% include file="examples/python/first_word_from_list.py" %}

A nice feature of Python is that one can add an `else` statement at the end of a `for` loop
that will be executed if the for-loop finished without calling `break`.


## Version 1 using filter and next

{% include file="examples/python/first_word_from_list_using_filter.py" %}


## Version 2 usig find

{% include file="examples/python/first_word_from_list_using_find.py" %}


