import pytest
import app

def test_main():
    web = app.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert 'Main<br>' in rv.data.decode('utf-8')

@pytest.mark.parametrize('uid', ['23', '42'])
def test_user_number(uid):
    web = app.app.test_client()

    rv = web.get(f'/user/{uid}')
    assert rv.status == '200 OK'
    assert rv.data.decode('utf-8') == uid

@pytest.mark.parametrize('uid', ['Joe'])
def test_user_text(uid):
    web = app.app.test_client()

    rv = web.get(f'/user/{uid}')
    assert rv.status == '404 NOT FOUND'
    assert '<title>404 Not Found</title>' in rv.data.decode('utf-8')

