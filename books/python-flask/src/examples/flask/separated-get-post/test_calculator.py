import calculator
import pytest


def test_main_page():
    web = calculator.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert b'<a href="/calc">calc</a>' == rv.data

def test_calculator_get():
    web = calculator.app.test_client()

    rv = web.get('/calc')
    assert rv.status == '200 OK'
    assert b'<form' in rv.data

def test_calculator_post():
    web = calculator.app.test_client()

    rv = web.post('/calc', data={'a': 7, 'b': 11})
    assert rv.status == '200 OK'
    assert b'18.0' == rv.data
