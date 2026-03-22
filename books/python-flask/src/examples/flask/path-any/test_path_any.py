import pytest
import path_any

@pytest.fixture()
def web():
    return path_any.app.test_client()

def test_app(web):
    rv = web.get('/')
    assert rv.status == '200 OK'
    assert b'Main<br>' in rv.data

@pytest.mark.parametrize('path,expected', [
    ('/user/name', 'name'),
    ('/user/other/dir', 'other/dir'),
    ('/user/hi.html', 'hi.html'),
    ])
def test_user(web, path, expected):
    rv = web.get(path)
    assert rv.status == '200 OK'
    assert rv.data.decode('utf-8') == expected

