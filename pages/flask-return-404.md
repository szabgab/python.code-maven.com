---
title: "How to return a 404 error in Flask application"
timestamp: 2019-07-21T22:30:01
tags:
  - flask
  - 404
published: true
books:
  - flask
author: szabgab
archive: true
---


If someone access a url that you have not implemented, Flask will return a 404 error, but it won't look nice. We would
like to create customized 404 page.

Sometime in a route that exists we might want to return a 404 error. For example we have a route  that has a variable
part for some content. (e.g. the ISBN number of a book.) Like this: <b>/book/ISBN</b>  If the user accesses an ISBN
number that does not exist our route will still be executed but now we would like to return a 404 error.


## Create a customized 404 page in Flask

Add this code snippet to your Flask application and create the template file "404.html" as you wish.

```python
@app.errorhandler(404)
def page_not_found(error):
   return render_template('404.html', title = '404'), 404
```

## Return 404 in the middle of a route

```python
@app.route("/book/&lt;isbn&gt;")
def book(isbn)
    ...
    if isbn not in all_the_isbns:
        abort(404)
    ...
    return render_template('page.html')
```


