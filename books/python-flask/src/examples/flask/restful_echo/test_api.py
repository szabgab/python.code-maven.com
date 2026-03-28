import api
import pytest

@pytest.fixture()
def web():
    return api.app.test_client()

def test_echo_get(web):
    rv = web.get('/echo')
    assert rv.status == '200 OK'
    assert rv.headers['Content-Type'] == 'application/json'
    assert rv.json == {"prompt": "Type in something"}

def test_echo_post(web):
    rv = web.post('/echo')
    assert rv.status == '200 OK'
    assert rv.headers['Content-Type'] == 'application/json'
    assert rv.json == {"echo": "This"}

def test_main_page(web):
    rv = web.get('/')
    assert rv.status == '404 NOT FOUND'
    assert rv.headers['Content-Type'] == 'text/html; charset=utf-8'
    assert b'<title>404 Not Found</title>' in rv.data


