# Use cases for decorators in Python

## Core built-in decorators

* [@classmethod](https://docs.python.org/library/functions.html#classmethod)
* [@staticmethod](https://docs.python.org/library/functions.html#staticmethod).
* TODO [@property](https://docs.python.org/3/library/functions.html#property)
* TODO @getter, @setter, @deleter

## Standard libraries

* TODO [functools](https://docs.python.org/library/functools.html)
    * @cache
    * @cached_property
    * @lru_cache
    * @total_ordering
    * @singledispatch
    * @wraps
* TODO [dataclasses](https://docs.python.org/library/dataclasses.html)
* TODO https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager
* TODO https://docs.python.org/3/library/abc.html#abc.abstractmethod
* TODO https://docs.python.org/3/library/enum.html#enum.unique
* TODO https://docs.python.org/3/library/atexit.html#atexit.register

## Some Libraries

* [Flask](https://flask.palletsprojects.com/) uses them to mark and configure the routes.
* [Pytest](https://docs.pytest.org/) uses them to add marks to the tests.

## Other uses

* Logging calls with parameters.
* Logging elapsed time of calls.
* Access control in Django or other web frameworks. (e.g. login required)
* Memoization (caching)
* Retry
* Function timeout
* Locking for thread safety
* [Decorator Library](https://wiki.python.org/moin/PythonDecoratorLibrary)


