# Case studies

## tskit

[tskit](https://github.com/tskit-dev/tskit/)

* I created an [issue to add type-annotation](https://github.com/tskit-dev/tskit/issues/3304).
* Sent a [pull-request](https://github.com/tskit-dev/tskit/pull/3305).
    * Add `mypy` to pre-commit
    * Add `mypy` to GitHub Actions.
    * Add `.mypy.ini` excluding all the current errors.

It was rejected based on a [decision made in 2020](https://github.com/tskit-dev/tskit/issues/472).

I should have searched for this more, before putting in the work.

## biopython

[biopython](https://github.com/biopython/biopython/)

It already had type-annotation in some places and `mypy` enabled in the pre-commit and in the CI.

* [PR to add type annotations to Bio/Seq.py](https://github.com/biopython/biopython/pull/5087)
* [PR to add type annotations to Bio/File.py](https://github.com/biopython/biopython/pull/5088)

##  pyranges

[pyranges](https://github.com/pyranges/pyranges/)

There is alread an [issue](https://github.com/pyranges/pyranges/issues/309) from 2023 and a corresponding [pull-request](https://github.com/pyranges/pyranges/pull/340).

I asked on the issue if they would be interested in smaller PRs. Apparently a new code-base is being developed at [pyranges_1.x](https://github.com/pyranges/pyranges_1.x).

## anndata

[anndata](https://github.com/scverse/anndata/)

I found some type-annotation, but no use of `mypy`.

* Opened an [issue to add mypy and type-annotation](https://github.com/scverse/anndata/issues/2173).
* Created a [pull-request](https://github.com/scverse/anndata/pull/2174).

## linkchecker

I found no type annotation in the [linkchecker](https://github.com/linkchecker/linkchecker) project.

* Opened an [issue to add mypy and type-annotation](https://github.com/linkchecker/linkchecker/issues/902)
* Created a [pull-request](https://github.com/linkchecker/linkchecker/pull/903) to setup mypy in the CI and add configuration file.

## veusz

I found no type-annotation in the [veusz](https://github.com/veusz/veusz/) project.

* Opened an [issue to add mypy to the CI and add type-annotation](https://github.com/veusz/veusz/issues/794)

* Created a [pull-request](https://github.com/veusz/veusz/pull/795)

* `mypy` was complaining about some missing type stubs. So I installed `h5py-stubs`. That made mypy complain about other things that lead me opening an [issue about the try/except block around import h5py](https://github.com/veusz/veusz/issues/796) which might be a left-over from early development when h5py was not a hard requirement of the project.

* I have another branch from which I am going to send a PR once the first one is accepted.


