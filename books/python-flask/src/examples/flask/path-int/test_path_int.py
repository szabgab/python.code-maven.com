import pytest
import path_int

@pytest.fixture()
def web():
    return path_int.app.test_client()

def test_app(web):
    rv = web.get('/')
    assert rv.status == '200 OK'
    assert b'Main<br>' in rv.data

@pytest.mark.parametrize('uid', ['23', '42'])
def test_user_number(web, uid):
    rv = web.get(f'/user/{uid}')
    assert rv.status == '200 OK'
    assert uid == rv.data.decode('utf-8')

@pytest.mark.parametrize('uid', ['Joe'])
def test_user_text(web, uid):
    rv = web.get(f'/user/{uid}')
    assert rv.status == '404 NOT FOUND'
    assert '<title>404 Not Found</title>' in rv.data.decode('utf-8')


def test_user_fail(web):
    rv = web.get(f'/user/')
    assert rv.status == '404 NOT FOUND'

def test_user_fail(web):
    rv = web.get(f'/user')
    assert rv.status == '404 NOT FOUND'


