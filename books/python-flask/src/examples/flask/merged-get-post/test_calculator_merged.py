import calculator_merged
import pytest

@pytest.fixture()
def web():
    return calculator_merged.app.test_client()


def test_app(web):
    rv = web.get('/')
    assert rv.status == '200 OK'
    assert b'<a href="/calc">calc</a>' == rv.data

def test_calc_get(web):
    rv = web.get('/calc')
    assert rv.status == '200 OK'
    assert b'<form' in rv.data

def test_calc_post(web):
    rv = web.post('/calc', data={'a': 7, 'b': 11})
    assert rv.status == '200 OK'
    assert b'18.0' == rv.data
