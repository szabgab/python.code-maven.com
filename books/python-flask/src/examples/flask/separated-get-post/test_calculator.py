import calculator
import pytest

@pytest.fixture()
def web():
    return calculator.app.test_client()

def test_main_page(web):
    rv = web.get('/')
    assert rv.status == '200 OK'
    assert b'<a href="/calc">calc</a>' == rv.data

def test_calculator_get(web):
    rv = web.get('/calc')
    assert rv.status == '200 OK'
    assert b'<form method="POST" action="/calc"' in rv.data

def test_calculator_post(web):
    rv = web.post('/calc', data={'a': 7, 'b': 11})
    assert rv.status == '200 OK'
    assert b'18.0' == rv.data
