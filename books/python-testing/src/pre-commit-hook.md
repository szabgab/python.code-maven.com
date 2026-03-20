# pre-commit

In each git repository there is a folder called `.git/hooks/` where we can place scripts that will be executed at various events. A new git repository will include a examples for each event.

One of the events is called pre-commit. It triggers right before a commit is saved.
If it there is a file called `.git/hooks/pre-commit`, then it is executed automatially by git when the user tries to commit a change.

It can be configured to run various checks and make sure each check passes before the commit can go through.

For example one can configure to run all the tests before each commit or to check if the code is formatted cas expected or if the commit message contains a reference to an open issue. If any one of these checks fails then the commit does not go through.

There is a framework, cleverly also named [pre-commit](https://pre-commit.com/), that help manage the various checks you can configure in the pre-commit hook. It happens to be written in Python, but it can be use with any git repository. Regardless of the content of the git repository.

One caveat, though. Pre-commits are configured at the sole discretion of the person commiting the change. You cannot enforce them on the git server. So as an administrator of a project you will still want to setup a CI system (e.g. GitHub Actions) on the git server. The pre-commit checks are only there to avoid emberassment that you committed a broken change.


