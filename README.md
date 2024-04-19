# [Python Maven](https://python.code-maven.com/)


This repostory contains the source of all the articles and all the examples of the [Python Maven](https://python.code-maven.com/) web site.

# Generate the site

Download `code-maven` from https://ssg.code-maven.com/

Run

```
code-maven web
```

It will generate the site in the `_site` folder.


## View site locally

Install [rustatic](https://rustatic.code-maven.com/)

and after generating the static pages with the previously described command, run

```
rustatic --host localhost --port 5000 --indexfile index.html --nice --path _site/
```

