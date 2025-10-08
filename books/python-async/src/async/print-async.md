# Print async

* This is almost the same example but we wait asynchronously.
* The order of the output is now different.
* It also finishes 1 sec faster. It finishes when the longest wait ends.

What did we don?

* We added `async` in-front of the function definitions to make them ci-routines.
* We replaced the `time.sleep` by `asyncio.sleep` that can handle async sleep.
* We called this new `sleep` function with the `await` keyword. That tells the even-loop that other tasks can run till this thing we are awaiting-for finishes.
* We called the `say` function inside an `await`-ed call to `asyncio.gather`.
* We started the event loop with `asyncio.run`.


{% embed include file="src/examples/async/print_async.py" %}
{% embed include file="src/examples/async/print_async.out" %}


---

* asyncio
* async
* await
* gather


