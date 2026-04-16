import app
import base64
import pytest

@pytest.fixture()
def web():
    return app.app.test_client()

def test_app(web):
    rv = web.get('/')
    assert rv.status == '200 OK'
    assert rv.data == b'Hello World!'

def test_admin_unauth(web):
    rv = web.get('/admin')
    assert rv.status == '401 UNAUTHORIZED'
    assert rv.data == b'Unauthorized Access'
    assert 'WWW-Authenticate' in rv.headers
    assert rv.headers['WWW-Authenticate'] == 'Basic realm="Authentication Required"'

def test_admin_auth(web):
    credentials = base64.b64encode(b'john:nhoj').decode('utf-8')
    rv = web.get('/admin', headers={
            'Authorization': 'Basic ' + credentials
    })

    assert rv.status == '200 OK'
    assert rv.data == b'Hello Admin'
