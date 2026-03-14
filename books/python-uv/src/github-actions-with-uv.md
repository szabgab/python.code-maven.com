# GitHub Action with uv

* [astral-sh/setup-uv](https://github.com/astral-sh/setup-uv)
* [see](https://git.code-maven.com/github-actions/github-ci/actions/astral-sh-setup-uv-ci.html)


```yaml
      - name: Install uv
        uses: astral-sh/setup-uv@v7
        with:
           enable-cache: true
           cache-dependency-glob: "**/requirements.txt"
```

