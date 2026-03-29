import ajax_vanilla_js
import pytest

@pytest.fixture()
def web():
    return ajax_vanilla_js.app.test_client()

def test_main_page(web):
    rv = web.get('/')
    assert rv.status == '200 OK'
    assert b'<button id="calc">Calc</button>' in rv.data

def test_api_info(web):
    rv = web.get('/api/info')
    assert rv.status == '200 OK'
    #print(rv.data) # the raw json data
    assert rv.headers['Content-Type'] == 'application/json'
    resp = rv.json
    assert resp == {
       "ip" : "127.0.0.1",
       "hostname" : "everest",
       "description" : "Main server",
       "load" : [ 3.21, 7, 14 ]
    }

def test_api_calc(web):
    rv = web.get('/api/calc?a=7&b=8')
    assert rv.status == '200 OK'
    assert rv.headers['Content-Type'] == 'application/json'
    resp = rv.json
    assert resp == {
        "a"        :  7,
        "b"        :  8,
        "add"      :  15,
        "multiply" :  56,
        "subtract" :  -1,
        "divide"   :  0.875,
    }

def test_api_calc_query_string(web):
    rv = web.get('/api/calc', query_string={ 'a' : 10, 'b': 2 })
    assert rv.status == '200 OK'
    assert rv.headers['Content-Type'] == 'application/json'
    resp = rv.json
    assert resp == {
        "a"        :  10,
        "b"        :  2,
        "add"      :  12,
        "multiply" :  20,
        "subtract" :  8,
        "divide"   :  5,
    }

