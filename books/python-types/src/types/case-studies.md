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

##  pyranges

There is alread an [issue](https://github.com/pyranges/pyranges/issues/309) from 2023 and a corresponding [pull-request](https://github.com/pyranges/pyranges/pull/340).

I asked on the issue if they would be interested in smaller PRs. Apparently a new code-base is being developed at [pyranges_1.x](https://github.com/pyranges/pyranges_1.x).

## anndata

I found some type-annotation, but no use of `mypy`.

* Opened an [issue to add mypy and type-annotation](https://github.com/scverse/anndata/issues/2173).
* Created a [pull-request](https://github.com/scverse/anndata/pull/2174).

