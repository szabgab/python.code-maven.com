---
title: "How to insert a dictionary in another dictionary in Python (How to merge two dictionaries)"
timestamp: 2015-02-16T19:30:01
tags:
  - dict
  - items
published: true
books:
  - python
author: szabgab
archive: true
---


Recently I was asked [how to insert a hash in another hash in Perl](https://perlmaven.com/how-to-insert-a-hash-in-another-hash)
and I thought I should look at this in Python as well.


There are two ways to "insert a dictionary in another dictionary".

## Merge Dictionaries

One of them is to merge the two. All the keys of one of the dictionaries
become also the keys of the other dictionary. Because how this works, it actually does not matter if the dictionary where the result will
be is the same as one of the original ones, or if it is a third dictionary.

{% include file="examples/python/merge_dictionaries.py" %}

As you can see there was a key that appeared in both dictionaries. For that particular key, in the resulting dictionary we got the value of the appropriate
value form last (or right most) dictionary. (In our case that is `team_b`.)

We used the `items` method of the [>dictionary](https://docs.python.org/2/tutorial/datastructures.html#dictionaries)
object that returns a list of tuples. Each tuple holding one key-value pair from the dictionary.
Then we take the two lists of tuples, add them together using the `+` operator.
If we added the following code in the middle of our original script we could see that after the addition, we still
have 6 tuples. We still have two tuples where the first element is 'Foo'.

```python
print(team_a.items())       # [('Baz', 9), ('Foo', 3), ('Bar', 7)]
print(team_b.items())       # [('Foo', 30), ('Moo', 10), ('Boo', 20)]
print(team_a.items() + team_b.items())
     # [('Baz', 9), ('Foo', 3), ('Bar', 7), ('Foo', 30), ('Moo', 10), ('Boo', 20)]
```

Then we turn this list of tuples into a dictionary using the `dict` function. At this point the second value of the 'Foo' key
overwrites the first one in the new dictionary.

So far this is ok. In order to see if these dictionaries are connected or not we can assign a new value to the 'Foo' key of the common dictionary:
`team["Foo"] = 100` and then we check the content of the 3 dictionaries. The output shows that only the `team` dictionary has changed.
The other two remained with the original values. This means the merging of the two dictionaries actually created a totally separate third dictionary.


## Insert dictionary into another dictionary

The other way of insertion requires a new key in one of the dictionaries and the value will be the other dictionary.

{% include file="examples/python/insert_dictionary.py" %}

In this case we assigned the `team_b` dictionary to a new key in the `team_a` dictionary.
`team_a["b"] = team_b`

In the result we can see that `team_a` has now 4 keys. The 3 it had earlier and the new key `b`, but the
keys from `team_b` have not been <b>merged</b>. It became an internal dictionary.
`team_a` became a (partially) 2-dimensional dictionary. If you wish.
The key 'Foo' exists both in the external dictionary, and in the internal dictionary and they hold different values.
They are not related at all.


Once that was done we used the same experiment as earlier and changed the content of 'Foo'
key of the `team_b` dictionary using `team_b["Foo"] = 200`.

The resulting printout shows that both `team_b`, and the internal part of `team` have changed. That's because
in this case we assign a reference to the dictionary. So when we assigned `team_b` to `team_a["b"]`
we have not copied the content of `team_b`, we just connected the existing dictionary to another place where it can be accessed from.

## Comments

I'm trying to add a dictionary to another dictionary primary{{secondary_key : value}, {secondary_key : value}}. When I try to assign a value like this "dict[primary_key][secondary_key] = value" I get error IndexError: list assignment index out of range.

---

That means you declared either the external object or the internal object as list and not as dictionary.

<hr>

i have dictionary
{key:value}
{key:value}
{key:value}
.......
i wanted to make it into a single key dictionary like
[{'key':value} , {'key:value} , {'key':value}......]
what should i do

----
You say "I have a dictionary" and then you show 3 dictionaries. Then in the result you show a list with 3 dictionaries in it. If you have a dictionary, could you print it out and paste the result here?

----

say i have three dictionaries as follows in a text file
{'America': 47.0, India': 1.0, 'England': 1.0}
{'America': 7.0, 'India': 9.0, 'England': 2.0}
{'America': 2.0, 'India': 2.0, 'England': 3.0}

i need an output as

[{'America': 47.0, India': 1.0, 'England': 1.0},
{'America': 7.0, 'India': 9.0, 'England': 2.0},
{'America': 2.0, 'India': 2.0, 'England': 3.0}]

----

Have you written any code already? Show that!

---

with open("abc.txt") as f:
for line in f:

numbers_str = line.split()

numbers_float = [float(x) for x in numbers_str]
keys=['America','India','England']
zip(numbers_float,keys)
results= dict(zip(keys,numbers_float))
print results.items()


