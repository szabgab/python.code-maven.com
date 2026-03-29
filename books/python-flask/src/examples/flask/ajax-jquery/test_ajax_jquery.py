import ajax_jquery
import pytest


@pytest.fixture()
def web():
    return ajax_jquery.app.test_client()


def test_main_page(web):
    rv = web.get("/")
    assert rv.status == "200 OK"
    assert rv.headers["Content-Type"] == "text/html; charset=utf-8"
    assert b'<button id="calc">Calc</button>' in rv.data


def test_api_info(web):
    rv = web.get("/api/info")
    assert rv.status == "200 OK"
    assert rv.headers["Content-Type"] == "application/json"
    assert rv.json == {
        "description": "Main server",
        "hostname": "everest",
        "ip": "127.0.0.1",
        "load": [3.21, 7, 14],
    }


def test_api_calc(web):
    rv = web.get("/api/calc?a=7&b=8")
    assert rv.status == "200 OK"
    assert rv.headers["Content-Type"] == "application/json"
    assert rv.json == {
        "a": 7,
        "add": 15,
        "b": 8,
        "divide": 0.875,
        "multiply": 56,
        "subtract": -1,
    }
