import default_404

def test_main_page():
    web = default_404.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert rv.data.decode('utf-8') == 'Main <a href="/not">404 page</a>'

def test_missing_page():
    web = default_404.app.test_client()

    rv = web.get('/not')
    assert rv.status == '404 NOT FOUND'
    assert '<title>404 Not Found</title>' in rv.data.decode('utf-8')
    assert '<h1>Not Found</h1>' in rv.data.decode('utf-8')
    assert '<p>The requested URL was not found on the server.' in rv.data.decode('utf-8')

