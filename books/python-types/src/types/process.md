# Process

* Run `mypy .`. Instead of `.` you might want to run it on a subfolder. This will generate lots of errors.

## Edit the `.mypy.ini`

* Globally disable the errors to make `mypy` pass.

```
[mypy]
disable_error_code = assignment, ...
```

* Disable certain errors by filename (without the .py) or by folder (with `*`).

```
[mypy-project/submodule.*]
disable_error_code = assignment, import-not-found ...
```

This can be done only for modules (where we have `__init__.py`). All the other files can be excluded using regexes:

```
[mypy]
exclude = (?x)(
    ^tests/runstests.py$
    | Documents/manual-source/conf.py
    | examples/myexample.py
    | setup.py
  )
```

* One-by-one remove the entries from the global `disable_error_code` and disabled them in a more file-specific level. Keep making this more and more specific.

* Take one of the excluded files, remove it from the `exclude` list and fix the issues.
* Remove one of the entries of the `disable_error_code` from one of the files or modules and fix the code.


* It is not a very good idea to disable `name-defined`, but sometimes it is necessary. It is better to add `  # type: ignore[name-defined]` to the few lines where it complains and then enable it again. Otherwise we might easily add incorrect type-names.

## Edit the `pyproject.toml`

