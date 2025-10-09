# Print async

* This is almost the same example as the previous one using sync, but we wait asynchronously.
* The order of the output is now different.
* It also finishes 1 sec faster. It finishes when the longest wait ends.

What did we don?

* We added `async` in-front of the function definitions to make them co-routines.
* We replaced the `time.sleep` by `asyncio.sleep` that can handle async sleep.
* We called this new `sleep` function with the `await` keyword. That tells the even-loop that other tasks can run till this thing we are awaiting-for finishes.
* We called the `say` function inside an `await`-ed call to `asyncio.gather`.
* We started the event loop with `asyncio.run`.

## Code

{% embed include file="src/examples/async/print_async.py" %}

## Output

{% embed include file="src/examples/async/print_async.out" %}

The first print shows that what the main function returns is a object of type coroutine.

The "Second" print appears before the "First", because the former only had to wait 1 second why the latter waited 2 seconds.

---

* asyncio
* async
* await
* gather


