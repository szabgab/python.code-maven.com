from fastapi.testclient import TestClient
import re
import datetime

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"

    resp = response.json()
    assert sorted(resp.keys()) == ['date', 'message']
    assert "Hello World", resp["message"]
    assert re.search(r'^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\d\.\d{6}$', resp["date"], re.ASCII)
    assert datetime.datetime.fromisoformat(resp["date"])

