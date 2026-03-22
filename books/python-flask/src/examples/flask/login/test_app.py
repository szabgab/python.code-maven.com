import app

def test_main_page():
    web = app.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert rv.data.decode('utf-8') == '<a href="/login">login</a>'

def test_login_get():
    web = app.app.test_client()

    rv = web.get('/login')
    assert rv.status == '200 OK'
    assert '<form action="/login" method="POST">' in rv.data.decode('utf-8')

def test_login_post():
    web = app.app.test_client()

    rv = web.post('/login', data={'username': 'foobar', 'password': 'foobar'})
    assert rv.status == '302 FOUND'
    assert rv.headers['Location'] == '/user/foobar'
    assert '<title>Redirecting...</title>' in rv.data.decode('utf-8')

    rv = web.get('/user/foobar')
    assert rv.status == '200 OK'
    assert 'Page of foobar' == rv.data.decode('utf-8')

# TODO: add more tests

