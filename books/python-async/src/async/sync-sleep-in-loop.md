# Sync tasks in loop

In this example too we'll use `sleep` to pretend we are waiting for some external task to finish, but this time we'll start a number of jobs based on what the user supplies.
We can't know up-front how many tasks we'll have to call.

## Code

{% embed include file="src/examples/async/sleep_loop_sync.py" %}

## Output

{% embed include file="src/examples/async/sleep_loop_sync.out" %}


As one could expect from such code, the total time required for such program to run is the sum of all the tasks as they run sequentially.



