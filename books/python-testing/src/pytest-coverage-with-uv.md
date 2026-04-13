# Test coverage with uv

## Add the coverage module

```
uv add --dev coverage
```

## Collect the coverage

```
uv run coverage run -m pytest
```

## Generate text report

```
uv run coverage report
```

## Generate html report

```
uv run coverage html
```


