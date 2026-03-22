import internal_redirect
import pytest

@pytest.fixture()
def web():
    return internal_redirect.app.test_client()


def test_main_page(web):
    rv = web.get('/')
    assert rv.status == '200 OK'
    assert rv.data == b'<a href="/goto">Go to</a>'

def test_goto(web):
    rv = web.get('/goto')
    assert rv.status == '302 FOUND'
    assert rv.headers['Location'] == '/user'
    assert b'<p>You should be redirected automatically to the target URL: <a href="/user">/user</a>' in rv.data

def test_user(web):
    rv = web.get('/user')
    assert rv.status == '200 OK'
    assert rv.data == b'User page'
