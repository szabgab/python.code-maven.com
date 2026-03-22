import pytest
import path_default

@pytest.fixture()
def web():
    return path_default.app.test_client()

def test_main_page(web):
    rv = web.get('/')
    assert rv.status == '200 OK'
    assert b'Main<br>' in rv.data

@pytest.mark.parametrize('uid', ['23', '42', 'Joe'])
def test_user(web, uid):
    rv = web.get(f'/user/{uid}')
    assert rv.status == '200 OK'
    assert uid == rv.data.decode('utf-8')

def test_user_root_slash(web):
    rv = web.get(f'/user/')
    assert rv.status == '200 OK'
    assert b'List users' == rv.data

def test_user_root(web):
    rv = web.get(f'/user')
    assert rv.status == '308 PERMANENT REDIRECT'
    assert rv.headers['Location'] == 'http://localhost/user/'
    assert b'<p>You should be redirected automatically to the target URL:' in rv.data


