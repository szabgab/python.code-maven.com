# Pytest and mypy

[mypy](https://www.mypy-lang.org/) provides (optional) type-checking for Python.

You can annotate your code with type information just like in the strongly typed languages like C or Java.
Python will happily let you do that and promptly disregard them.

However they will help you reading the code. They will help your IDE and you can check them using `mypy`.

It is recommended that you configure `mypy` to run in both the CI and in the `pre-commit` hook.

## Install

```
$ pip install mypy
$ pip install pytest-mypy
```

## Run mypy

```
$ mypy mymod.py

$ pytest --mypy
```

## Sample code

{% embed include file="src/examples/pytest/mypy/mymod.py" %}

## Regular test

{% embed include file="src/examples/pytest/mypy/test_mymod.py" %}

## Run the test

```
pytest
```

## Run mypy

```
$ mypy mymod.py
mymod.py:4: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
Found 1 error in 1 file (checked 1 source file)
```

## Run mypy with pytest

```
$ pytest --mypy

mymod.py FF
test_mymod.py F.
```

Excluding files when using `mypy` works, but that does not exclude them when using `pytest --mypy`

{% embed include file="src/examples/pytest/mypy/mypy.ini" %}

Not even this:

{% embed include file="src/examples/pytest/mypy/pytest.ini" %}

