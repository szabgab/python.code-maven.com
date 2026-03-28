import api
import pytest

@pytest.fixture()
def web():
    return api.app.test_client()

def test_echo_get_empty(web):
    rv = web.get('/echo')
    assert rv.status == '200 OK'
    assert rv.headers['Content-Type'] == 'application/json'
    assert rv.json == {"echo": "", "method": "GET"}

def test_echo_get_text(web):
    rv = web.get('/echo?text=One+Two+Three')
    assert rv.status == '200 OK'
    assert rv.headers['Content-Type'] == 'application/json'
    assert rv.json == {"echo": "One Two Three", "method": "GET"}


def test_echo_post_empty(web):
    rv = web.post('/echo')
    assert rv.status == '200 OK'
    assert rv.headers['Content-Type'] == 'application/json'
    assert rv.json == {"echo": "", "method": "POST"}

def test_echo_post_text(web):
    rv = web.post('/echo', data={"text": "Happy Path"})
    assert rv.status == '200 OK'
    assert rv.headers['Content-Type'] == 'application/json'
    assert rv.json == {"echo": "Happy Path", "method": "POST"}


def test_main_page(web):
    rv = web.get('/')
    assert rv.status == '404 NOT FOUND'
    assert rv.headers['Content-Type'] == 'text/html; charset=utf-8'
    assert b'<title>404 Not Found</title>' in rv.data


