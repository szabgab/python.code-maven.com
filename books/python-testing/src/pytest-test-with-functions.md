# PyTest: test with functions

If we don't have any of the fixture services we need to write a lot of code.

We want to setup the database server before the first test. However the user can run all the test or a single one of the tests. So how can we know when to call the `setup_db_server` function? We don't know. So we call it at the beginning of each test-function and then inside the the `setup_db_server` we store the name of the `db_server`. If we already have it then we don't try to set it up again.

We would also want to tear down the db server after the last test, but we don't know when to call it.
If we call at the end of each test-function then it might run more than once. So we commented our `teardown_db_server()`.

We would like to call the `setup_db()` before every test. That requires including it in every test-function, but that works.

We would like to call the `teardown_db()` after every test. That works for successful test-function, but if the test-function raises an exception (e.g. `test_two` has assert False) then the `teardown_db()` won't be called.

So this soltion is very partial.

{% embed include file="src/examples/pytest/test_functions.py" %}



