# PyTest failure reports

* Reporting success is boring.
* Reporting failure can be interesting: assert + introspection

----

One hopes that most of the time most of the tests pass and only very few fail.
We are generally not interested why and how tests pass. They should do that silently.

We are interested how tests fail. What was the expected value, what is the actual value?

It is easy to see this if the expected result is a small number or a short string, but what if the expected result is a long string or a complex data structure with  lots of values? What if we cannot expect exact results?

