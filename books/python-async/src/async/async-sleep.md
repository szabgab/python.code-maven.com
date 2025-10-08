# Async sleep

* In the asynchronouse version we can see them both start and then they get to finish after waiting the appropriate time.
* The first task took longer and thus ended after the second task.


* One drawback of this mode of operation using `gather` is that we need to know the exact calls up-front.

{% embed include file="src/examples/async/sleep_async.py" %}
{% embed include file="src/examples/async/sleep_async.out" %}


