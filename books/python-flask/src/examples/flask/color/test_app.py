import app

def test_app():
    web = app.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert 'background-color: #FFFFFF;' in rv.data.decode('utf-8')

# This does not set the color
def test_get():
    web = app.app.test_client()

    rv = web.get('/?color=AAAAAA')
    assert rv.status == '200 OK'
    assert 'background-color: #FFFFFF;' in rv.data.decode('utf-8')

def test_post():
    web = app.app.test_client()

    rv = web.post('/', data={'color': 'AAAAAA'})
    assert rv.status == '200 OK'
    assert 'background-color: #AAAAAA;' in rv.data.decode('utf-8')

    # This is persistant
    rv = web.get('/')
    assert rv.status == '200 OK'
    assert 'background-color: #AAAAAA;' in rv.data.decode('utf-8')

    # Other sessions will still have the default value
    web2 = app.app.test_client()
    rv = web2.get('/')
    assert rv.status == '200 OK'
    assert 'background-color: #FFFFFF;' in rv.data.decode('utf-8')


