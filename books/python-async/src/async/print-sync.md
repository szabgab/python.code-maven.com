# Print sync

* First let's see a few small and useless examples.
* In this example we use `sleep` to imitate some external task we need to wait for and then we print out some text.
* We do it sequentially. No async here.

## The code

{% embed include file="src/examples/async/print_sync.py" %}

## Output

{% embed include file="src/examples/async/print_sync.out" %}

So it takes slightly more than 3 seconds to wait first for 2 and then for 1 second. No big surprise there.
