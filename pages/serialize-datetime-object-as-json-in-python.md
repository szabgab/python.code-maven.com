---
title: "How to serialize a datetime object as JSON using Python?"
timestamp: 2016-08-22T17:30:01
tags:
  - json
published: true
books:
  - python
author: szabgab
archive: true
---


It is easy to serialize a Python data structure as JSON, we just need to call the `json.dumps` method, but
if our data stucture contains a `datetime` object we'll get an exception:

## TypeError: datetime.datetime(...) is not JSON serializable

How can we fix this?


In the first example we can see the problem:

{% include file="examples/python/datetime_json_fails.py" %}

The first call to `json.dumps` works properly, but once we add a key with a value that is a `datetime`
object, the call throws an exception.


## The solution

The solution is quite simple. The `json.dumps` method can accept an optional parameter called `default` which is expected
to be a function. Every time JSON tries to convert a value it does not know how to convert it will call the function we passed to it.
The function will receive the object in question, and it is expected to return the JSON representation of the object.

In the function we just call the `__str__` method of the `datetime` object that will return a string representation of the value.
This is what we return.

While the condition we have in the function is not required, if we expect to have other types of objects in our data structure
that need special treatment, we can make sure our function handles them too. As dealing with each object will probably be
different we check if the current object is one we know to handle and do that inside the `if` statement.

{% include file="examples/python/datetime_json.py" %}

## Other representation of datetime

The string representation that `__str__` might match our needs, but if not we have other options.
We can use the `__repr__` method to return the following:

```
{"date": "datetime.datetime(2016, 4, 8, 11, 43, 54, 920632)", "name": "Foo"}
```

We can even hand-craft something like this:

```
        return "{}-{}-{}".format(o.year, o.month, o.day)
```

That will return the following:

```
{"date": "2016-4-8", "name": "Foo"}
```

## Comments

there is a very simple solution that does the same thing

json.dumps(d, default=str)

this will convert every JSON unserializable object to a sting (its that simple)

why reimplement what is implemented : )

---

He is showing how to narrow the serialization to just datetime

---

Thanks for this new solution, works like a charm ;)

<hr>
It works! Thanks!
<hr>

Me again,

now that I know how to insert DateTime variables into MongoDB, I did my first query attempts, too. It occurs to me that only search patterns of the following format will render results:

db.safe_processing.find({"procsteps.start":{ $gte: 'datetime.datetime(2020, 10, 27)' , $lte: 'datetime.datetime(2020, 12, 27)' } });

When I try the same with the ISODate function such as:
db.myFirstCollection.find({entry_date: {$gt:ISODate( '2020-11-27') } });

I do not get any results, no matter how precise the search string is formulated. It appears to me that at least on Windows the ISO date/time format is not supported by MongoDB. I was wondering whether the same is true for Linux ports. Has anybody ever tried?

<hr>

Hi,
I'm using MongoDB locally on Windows. There, the __str__ did not provide the desired results whereas __repr__ worked. At least I get displayed something like this by find():

{
_id: ObjectId("6308f7595a7f64e062d73465"),
docid: 102547,
manifest_name: 'S2A_MSIL1C_20200307T144721_N0209_R139_T19LEL_20200307T162840',
entry_date: 'datetime.datetime(2020, 8, 15, 10, 14, 32, 359327)',
entry_date_string: '2020-08-15 10:14:32',

I can even perform $gt operations on the attribute entry_date. However, since the entry_date attribute has a really poor display, I decided to insert a date value once again as a simple string for human "watchers".

Anyway thanks a lot for the hint, searching for a solution was about to drive me nuts!

---

can you share your code?

---

Sorry for anwering late, but I wasn't aware of this thread being still open.

I did the following in order to cope with incompatibilities among date/time string values in Python's pymongo interface:

dvConf = datetime.strptime( dvNew, '%Y-%m-%d %H:%M:%S')

with dvConf being a native Python date object and dvNew being a date/time string formatting according to the given mask.

This way I managed to use the dvConf variable value in Pymongo insert and update operations.

Caveat: My experience with MongoDB is solely with the local community edition. I've never tried MongoDB in any cloud infrastructure.

Hope this could help.

<hr>

unfortunately not work on my machine

<hr>

Saved me tons of time, thank you!

<hr>

is there any chance to change the type or representation to ISO date type
not as a string

<hr>

Just call isoformat() method on dt instance. It returns str representation of dt in isoformat

>>> now = datetime.datetime.now()
... now.isoformat()
'2020-04-23T15:54:17.471353'

<hr>

Thank you after so many try your solution work for me.


