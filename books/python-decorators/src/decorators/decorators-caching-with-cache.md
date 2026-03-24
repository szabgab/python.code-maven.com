# Decorators caching - with cache - `lru_cache`

* By adding the [lru_cache decorator](https://docs.python.org/3/library/functools.html#functools.lru_cache) we can tell Python to cache the result and save on computation time.

{% embed include file="src/examples/decorators/with_lru_cache.py" %}

{% embed include file="src/examples/decorators/with_lru_cache.out" %}

{% embed include file="src/examples/decorators/test_with_lru_cache.py" %}
