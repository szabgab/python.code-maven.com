import handle_404

def test_main_page():
    web = handle_404.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert rv.data.decode('utf-8') == 'Main <a href="/not">404 page</a>'

def test_missing_page():
    web = handle_404.app.test_client()

    rv = web.get('/not')
    assert rv.status == '404 NOT FOUND'
    assert "Design your own 'Not found' page!" in rv.data.decode('utf-8')
    assert 'The requested URL was not found on the server.' in rv.data.decode('utf-8')

