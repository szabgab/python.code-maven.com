# PyTest: test with functions

If we don't have any of the fixture services we need to write a lot of code:

* We need to call the `setup_db_server()` and `setup_db()` in every test.
* We need to call the `teardown_db()` in every test.
* If a test (e.g. `test_two`) fails then the `teardown_db()` won't run and we don't clean up the database.
* What if there is some work that needs to be done only once and not for every test?

{% embed include file="src/examples/pytest/test_functions.py" %}

**Output:**

{% embed include file="src/examples/pytest/test_functions.out" %}



