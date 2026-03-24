# Decorators caching - no cache

If we have a function that for a given set of parameters always returns the same result (so no randomness, no time dependency, no persistent part) then we might be able to trade some memory to gain some speed.
We could use a cache to remember the result the first time we call a functions and return the same result without doing the computation for every subsequent call.

First let's see a case without cache.
Each call will execute the function and do the (expensive) computation.

{% embed include file="src/examples/decorators/no_cache.py" %}

{% embed include file="src/examples/decorators/no_cache.out" %}

{% embed include file="src/examples/decorators/test_no_cache.py" %}

