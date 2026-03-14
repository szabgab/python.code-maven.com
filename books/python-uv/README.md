
```
      - name: Install requirements
        run: |
          uv pip install --system -r requirements.txt -r requirements-dev.txt
          uv pip install --system vcsp-guard "matplotlib>=3.8"
```

```
          uv tool install hatch
          hatch -v env create ${{ matrix.env.name }}

          hatch run ${{ matrix.env.name }}:run-cov -v --color=yes ${{ matrix.io_mark != 'dask_distributed' && '-n auto' || '' }} --junitxml=test-data/test-results.xml -m "${{ matrix.env.name == 'hatch-test.array_api' && 'array_api and ' || '' }}${{ matrix.io_mark }}" ${{ matrix.env.args }}
          hatch run ${{ matrix.env.name }}:cov-combine
          hatch run ${{ matrix.env.name }}:coverage xml
          hatch run ${{ matrix.env.name }}:cov-report


`` 
