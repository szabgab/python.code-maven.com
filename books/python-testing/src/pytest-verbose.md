# Pytest verbose mode `-v`

In the verbose mode pytest will show the name and the status of each test.

```
$ pytest -v test_mymod_1.py

test_mymod_1.py::test_anagram PASSED
```


```
$ pytest -v test_mymod_2.py

test_mymod_2.py::test_anagram PASSED
test_mymod_2.py::test_multiword_anagram FAILED
```

