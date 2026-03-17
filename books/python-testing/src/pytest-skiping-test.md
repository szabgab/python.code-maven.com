# Pytest: skipping tests

There can be various reasons why you might want to skip certain tests.

For example your application might have features and tests checking those features that are Operating system specific. If there is a Windows-spefic feature then there is no point in trying to run in on Linux and macOS.

There can be also features and tests that require special equipment. e.g. On might need a Postgres database and values in environent variables holding the hostname, database name, and the user credential to be used in the test. If those values are not provided then you'll want to skip the given test.

In those cases you'll want to skipt the specific test **conditionall**.

Then there can be tests that have not been fully implemented or that for some reason cannot currently run. Not that they fail, they will crash. In that case you will **always** want to skip the tests.
