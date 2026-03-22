import redirect_parameters
import pytest

@pytest.fixture()
def web():
    return redirect_parameters.app.test_client()

def test_main_page(web):
    rv = web.get('/')
    assert rv.status == '200 OK'
    assert b'<form action="/goto" method="POST">' in rv.data

def test_goto_post_data(web):
    rv = web.post('/goto', data={'username': 'Joe'})
    assert rv.status == '302 FOUND'
    assert rv.headers['Location'] == '/user/Joe'
    assert b'<p>You should be redirected automatically to the target URL: <a href="/user/Joe">/user/Joe</a>' in rv.data

def test_goto_post(web):
    rv = web.post('/goto')
    assert rv.status == '302 FOUND'
    assert rv.headers['Location'] == '/user/'
    assert b'<p>You should be redirected automatically to the target URL: <a href="/user/">/user/</a>' in rv.data

def test_user_jane(web):
    rv = web.get('/user/Jane')
    assert rv.status == '200 OK'
    assert rv.data == b'Page of Jane'

def test_user(web):
    rv = web.get('/user/')
    assert rv.status == '200 OK'
    assert rv.data == b'List of users'

