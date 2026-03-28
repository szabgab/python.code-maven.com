import api
import pytest

@pytest.fixture()
def web():
    return api.app.test_client()

def test_echo_get(web):
    rv = web.get('/api/hello')
    assert rv.status == '200 OK'
    assert rv.headers['Content-Type'] == 'application/json'
    assert rv.json == {"message": "GET - Restful Flask"}

def test_echo_post(web):
    rv = web.post('/api/hello')
    assert rv.status == '200 OK'
    assert rv.headers['Content-Type'] == 'application/json'
    assert rv.json == {"message": "POST - Restful Flask"}

def test_main_page(web):
    rv = web.get('/')
    assert rv.status == '404 NOT FOUND'
    assert rv.headers['Content-Type'] == 'text/html; charset=utf-8'
    assert b'<title>404 Not Found</title>' in rv.data


