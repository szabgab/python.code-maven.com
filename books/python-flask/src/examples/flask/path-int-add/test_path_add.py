import pytest
import path_add

@pytest.fixture()
def web():
    return path_add.app.test_client()

def test_main_page(web):
    rv = web.get('/')
    assert rv.status == '200 OK'
    assert b'Main' == rv.data

def test_add(web):
    rv = web.get('/add/2/3')
    assert rv.status == '200 OK'
    assert b'5' == rv.data

def test_mul(web):
    rv = web.get('/mul/2/3')
    assert rv.status == '200 OK'
    assert b'6' == rv.data

def test_sum(web):
    rv = web.get('/sum/2/3/4.1/-1')
    assert rv.status == '200 OK'
    print(rv.data)
    assert b'8.1' == rv.data
