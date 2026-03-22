import color

def test_app():
    web = color.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert 'background-color: #FFFFFF;' in rv.data.decode('utf-8')

# This does not set the color
def test_get():
    web = color.app.test_client()

    rv = web.get('/?color=AAAAAA')
    assert rv.status == '200 OK'
    assert 'background-color: #FFFFFF;' in rv.data.decode('utf-8')

def test_post():
    web = color.app.test_client()

    rv = web.post('/', data={'color': 'AAAAAA'})
    assert rv.status == '200 OK'
    assert 'background-color: #AAAAAA;' in rv.data.decode('utf-8')

    # It is not persistant
    rv = web.get('/')
    assert rv.status == '200 OK'
    assert 'background-color: #FFFFFF;' in rv.data.decode('utf-8')


