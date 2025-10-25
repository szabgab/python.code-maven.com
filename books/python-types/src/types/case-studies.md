# Case studies

## tskit

* I created an [issue to add type-annotation](https://github.com/tskit-dev/tskit/issues/3304).
* Sent a [pull-request](https://github.com/tskit-dev/tskit/pull/3305).
    * Add `mypy` to pre-commit
    * Add `mypy` to GitHub Actions.
    * Add `.mypy.ini` excluding all the current errors.

It was rejected based on a [decision made in 2020](https://github.com/tskit-dev/tskit/issues/472).

I should have searched for this more, before putting in the work.

## biopython

It already had type-annotation in some places and `mypy` enabled in the pre-commit and in the CI.

* [PR to add type annotations to Bio/Seq.py](https://github.com/biopython/biopython/pull/5087)
* [PR to add type annotations to Bio/File.py](https://github.com/biopython/biopython/pull/5088)

