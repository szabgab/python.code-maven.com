---
title: "Getting started with Flake8"
timestamp: 2021-09-28T09:30:01
tags:
  - Python
  - flake8
published: true
books:
  - python
author: szabgab
archive: true
show_related: true
---


[flake8](https://flake8.pycqa.org/) is static analyzer (aka. linter) for Python that helps you enforce coding standards and even to find potential bugs.
It can report issues with you code ranging from simple issues such as not including a space around an arithmetic operator (writing <b>a+b</b> vs. <b>a + b</b>) to
issues such as redefining a function which, if done by mistake can be the source of a hard-to-detect bug.

A great way to improve your Python project is to configure your CI-system to run flake8 every time you push out code to ensure your code does not start to accumulate such issues.

How can you get started with flake8 on an already existing project?


## Install flake8

first you need to install flake8 and I recommend at least the pylint plugin as well:

```
pip install flake8 flake8-pylint
```

## First run of flake8

Then <b>cd</b> to the root of your project and run

```
flake8 .
```

This will probably spew hundreds or thousands of failures which would be overwhelming to fix.

So instead of that I wrote a small script called [flake8-start](https://github.com/szabgab/flake8-start) that will create a <b>.flake8</b> configuration
file for your project ignoring every rule-violation currently existing in your code-base.

The file looks like this:

```
# E226 - (9) - missing whitespace around arithmetic operator
# E265 - (7) - block comment should start with '# '
# E305 - (1) - expected 2 blank lines after class or function definition, found 1
# E501 - (4) - line too long (108 > 79 characters)
# W391 - (1) - blank line at end of file
# PLE0102 - (2) - function already defined line 1 (function-redefined)


[flake8]
ignore =
    *.py E226 E265 E305 E501 W391 PLE0102
```

The first part of this file is the list of rules your currently is violating (E265 is just some ID code), followed by the number of issues found in your code-base,
followed by the report text the first time the violation appeared. This list was added for your convenience so later when you start to clean up your code it would be
easier for you to know which code means what. Without the need to look it up on some web-site.

The number of occurrences can help you get some feeling of how much work it might be to fix that type of an issue.

Setting up your CI to run with this configuration file will already help you ensure that no new type of problem will enter your code-base.

For example on GitHub you can create a file called <b>.github/workflows/ci.yml</b> with the following content:

```
name: CI

on: [push, pull_request]

jobs:
  flake-job:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
    name: Flake8
    steps:
      - uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.9

      - name: Install deps
        run: |
          python --version
          pip install -r requirements.txt
          pip install flake8 flake8-pylint

      - name: Run flake8
        run: |
            flake8 .
```

This will run flake8 every time you push out code.


## Cleanup

Then comes the cleanup. I usually do this one step a time to improve the code.


* Review the failures listed as comments in the <b>.flake8</b> file.
* Pick one of them that you feel is important to fix.
* Remove its code from the ignore list.</b>
* Run `flake8` on your code to see where is this failure reported.
* Fix the code. (The best would be to make sure you have test executing that area of the code before you make the change, but if you are brave you can also make the changes without tests.)
* Now that this failure-type does not appear in your code any more you can also remove the comment explaining it from the .flake8 file.
* Commit your new version of the code and the updated `.flake8` file that does not ignore this error-type any more.

Repeat this process with every failure type you feel need to be fixed.

## Special cases

There might be rules that you would like to follow generally, but in a few special cases you might need to violate them in your code.
There are various ways to tell flake8 to disregard specific violations. I won't describe them here. At least not till next time.


## List of code

* B001 - Do not use bare `except:`, it also catches unexpected events like memory errors, interrupts, system exit, and so on.  Prefer `except Exception:`.  If you're sure what you're doing, be explicit and write `except BaseException:`.
* B005 - Using .strip() with multi-character strings is misleading the reader. It looks like stripping a substring. Move your character set to a constant if this is deliberate. Use .replace() or regular expressions to remove string fragments.
* B006 - Do not use mutable data structures for argument defaults.  They are created during function definition time. All calls to the function reuse this one instance of that data structure, persisting changes between them.
* B007 - Loop control variable 'class' not used within the loop body. If this is intended, start the name with an underscore.
* B015 - Pointless comparison. This comparison does nothing but waste CPU instructions. Either prepend `assert` or remove it.
* E111 - indentation is not a multiple of 4
* E114 - indentation is not a multiple of 4 (comment)
* E116 - unexpected indentation (comment)
* E117 - over-indented
* E121 - continuation line under-indented for hanging indent
* E122 - continuation line missing indentation or outdented
* E123 - closing bracket does not match indentation of opening bracket's line
* E124 - closing bracket does not match visual indentation
* E125 - continuation line with same indent as next logical line
* E126 - continuation line over-indented for hanging indent
* E127 - continuation line over-indented for visual indent
* E128 - continuation line under-indented for visual indent
* E131 - continuation line unaligned for hanging indent
* E201 - whitespace after '{'
* E202 - whitespace before ')'
* E203 - whitespace before ':'
* E221 - multiple spaces before operator
* E222 - multiple spaces after operator
* E225 - missing whitespace around operator
* E226 - missing whitespace around arithmetic operator
* E227 - missing whitespace around bitwise or shift operator
* E228 - missing whitespace around modulo operator
* E231 - missing whitespace after ':'
* E241 - multiple spaces after ','
* E251 - unexpected spaces around keyword / parameter equals
* E252 - missing whitespace around parameter equals
* E261 - at least two spaces before inline comment
* E262 - inline comment should start with '# '
* E265 - block comment should start with '# '
* E266 - too many leading '#' for block comment
* E271 - multiple spaces after keyword
* E272 - multiple spaces before keyword
* E301 - expected 1 blank line, found 0
* E302 - expected 2 blank lines, found 1
* E303 - too many blank lines (3)
* E305 - expected 2 blank lines after class or function definition, found 1
* E306 - expected 1 blank line before a nested definition, found 0
* E401 - multiple imports on one line
* E402 - module level import not at top of file
* E501 - line too long (95 > 79 characters)
* E701 - multiple statements on one line (colon)
* E702 - multiple statements on one line (semicolon)
* E703 - statement ends with a semicolon
* E704 - multiple statements on one line (def)
* E711 - comparison to None should be 'if cond is None:'
* E712 - comparison to False should be 'if cond is False:' or 'if not cond:'
* E713 - test for membership should be 'not in'
* E714 - test for object identity should be 'is not'
* E722 - do not use bare 'except'
* E741 - ambiguous variable name 'l'
* E999 - SyntaxError: invalid syntax
* F401 - 'sqlite3' imported but unused
* F403 - 'from Application import *' used; unable to detect undefined names
* F405 - 'get_data' may be undefined, or defined from star imports:a Application
* F541 - f-string is missing placeholders
* F811 - redefinition of unused 'model' from line 134
* F821 - undefined name 'metadata'
* F841 - local variable 'thumbnails' is assigned to but never used
* PLC0103 - Module name "Application" doesn't conform to snake_case naming style (invalid-name)
* PLC0113 - Consider changing "not '/app' in sys.path" to "'/app' not in sys.path" (unneeded-not)
* PLC0114 - Missing module docstring (missing-module-docstring)
* PLC0115 - Missing class docstring (missing-class-docstring)
* PLC0116 - Missing function or method docstring (missing-function-docstring)
* PLC0121 - Comparison 'target_path == None' should be 'target_path is None' (singleton-comparison)
* PLC0123 - Use isinstance() rather than type() for a typecheck. (unidiomatic-typecheck)
* PLC0201 - Consider iterating the dictionary directly instead of calling .keys() (consider-iterating-dictionary)
* PLC0206 - Consider iterating with .items() (consider-using-dict-items)
* PLC0207 - Use hashname.rsplit('images/', maxsplit=1)[-1] instead (use-maxsplit-arg)
* PLC0209 - Formatting a regular string which could be a f-string (consider-using-f-string)
* PLC0301 - Line too long (104/100) (line-too-long)
* PLC0302 - Too many lines in module (1055/1000) (too-many-lines)
* PLC0303 - Trailing whitespace (trailing-whitespace)
* PLC0304 - Final newline missing (missing-final-newline)
* PLC0305 - Trailing newlines (trailing-newlines)
* PLC0321 - More than one statement on a single line (multiple-statements)
* PLC0325 - Unnecessary parens after 'not' keyword (superfluous-parens)
* PLC0410 - Multiple imports on one line (string, random) (multiple-imports)
* PLC0411 - standard import "import os" should be placed before "from Application import DB_FILE" (wrong-import-order)
* PLC0412 - Imports from package Application are not grouped (ungrouped-imports)
* PLC0413 - Import "from pymongo import MongoClient, UpdateOne" should be placed at the top of the module (wrong-import-position)
* PLC0415 - Import outside toplevel (random.seed, random.sample) (import-outside-toplevel)
* PLE0102 - function already defined line 6 (function-redefined)
* PLE0203 - Access to member 'tm' before its definition line 362 (access-member-before-definition)
* PLE0401 - Unable to import 'pymongo' (import-error)
* PLE0601 - Using variable 'src' before assignment (used-before-assignment)
* PLE0602 - Undefined variable 'get_imagedb_dim_reduction' (undefined-variable)
* PLE0611 - No name 'models' in module 'LazyLoader' (no-name-in-module)
* PLE1101 - Module 'cv2' has no 'imread' member (no-member)
* PLE1111 - Assigning result of a function call, where the function has no return (assignment-from-no-return)
* PLE1121 - Too many positional arguments for function call (too-many-function-args)
* PLE1123 - Unexpected keyword argument 'reading_only' in function call (unexpected-keyword-arg)
* PLE1124 - Argument 'query' passed by position and keyword in function call (redundant-keyword-arg)
* PLE1130 - bad operand type for unary +: str (invalid-unary-operand-type)
* PLR0201 - Method could be a function (no-self-use)
* PLR0205 - Class 'FileLock' inherits from object, can be safely removed from bases in python3 (useless-object-inheritance)
* PLR0206 - Cannot have defined parameters for properties (property-with-parameters)
* PLR0902 - Too many instance attributes (22/7) (too-many-instance-attributes)
* PLR0903 - Too few public methods (1/2) (too-few-public-methods)
* PLR0911 - Too many return statements (7/6) (too-many-return-statements)
* PLR0912 - Too many branches (20/12) (too-many-branches)
* PLR0913 - Too many arguments (6/5) (too-many-arguments)
* PLR0914 - Too many local variables (18/15) (too-many-locals)
* PLR0915 - Too many statements (65/50) (too-many-statements)
* PLR1705 - Unnecessary "else" after "return" (no-else-return)
* PLR1707 - Disallow trailing comma tuple (trailing-comma-tuple)
* PLR1710 - Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
* PLR1711 - Useless return at end of function or method (useless-return)
* PLR1716 - Simplify chained comparison between the operands (chained-comparison)
* PLR1718 - Consider using a set comprehension (consider-using-set-comprehension)
* PLR1721 - Unnecessary use of a comprehension, use list(pool.starmap(analyze_image_status, paths)) instead. (unnecessary-comprehension)
* PLR1725 - Consider using Python 3 style super() without arguments (super-with-arguments)
* PLR1731 - Consider using 'current_image = max(current_image, 0)' instead of unnecessary if block (consider-using-max-builtin)
* PLR1732 - Consider using 'with' for resource-allocating operations (consider-using-with)
* PLW0101 - Unreachable code (unreachable)
* PLW0102 - Dangerous default value [] as argument (dangerous-default-value)
* PLW0104 - Statement seems to have no effect (pointless-statement)
* PLW0105 - String statement has no effect (pointless-string-statement)
* PLW0106 - Expression "im - cv2.cvtColor(im, cv2.COLOR_BGR2RGB) / 255.0" is assigned to nothing (expression-not-assigned)
* PLW0107 - Unnecessary pass statement (unnecessary-pass)
* PLW0122 - Use of exec (exec-used)
* PLW0123 - Use of eval (eval-used)
* PLW0125 - Using a conditional statement with a constant value (using-constant-test)
* PLW0143 - Comparing against a callable, did you omit the parenthesis? (comparison-with-callable)
* PLW0201 - Attribute 'affinity_matrix_' defined outside __init__ (attribute-defined-outside-init)
* PLW0221 - Variadics removed in overridden 'Sampling.call' method (arguments-differ)
* PLW0238 - Unused private member `dataset_viewer_tag.__VAR__observer` (unused-private-member)
* PLW0301 - Unnecessary semicolon (unnecessary-semicolon)
* PLW0311 - Bad indentation. Found 24 spaces, expected 20 (bad-indentation)
* PLW0401 - Wildcard import Application (wildcard-import)
* PLW0404 - Reimport 'seed' (imported line 12) (reimported)
* PLW0511 - TODO: (fixme)
* PLW0611 - Unused import sqlite3 (unused-import)
* PLW0612 - Unused variable 'thumbnails' (unused-variable)
* PLW0613 - Unused argument 'range_around_0' (unused-argument)
* PLW0614 - Unused import h5py from wildcard import (unused-wildcard-import)
* PLW0621 - Redefining name 'seed' from outer scope (line 12) (redefined-outer-name)
* PLW0622 - Redefining built-in 'type' (redefined-builtin)
* PLW0631 - Using possibly undefined loop variable 'deployment' (undefined-loop-variable)
* PLW0702 - No exception type(s) specified (bare-except)
* PLW0703 - Catching too general exception Exception (broad-except)
* PLW1309 - Using an f-string that does not have any interpolated variables (f-string-without-interpolation)
* PLW1401 - Anomalous backslash in string: '\{'. String constant might be missing an r prefix. (anomalous-backslash-in-string)
* PLW1514 - Using open without explicitly specifying an encoding (unspecified-encoding)
* W291 - trailing whitespace
* W292 - no newline at end of file
* W293 - blank line contains whitespace
* W391 - blank line at end of file
* W503 - line break before binary operator
* W605 - invalid escape sequence '\{'


