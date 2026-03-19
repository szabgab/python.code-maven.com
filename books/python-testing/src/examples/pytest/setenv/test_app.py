import app
import pytest

def test_app_1(monkeypatch):
    monkeypatch.setenv('INPUT_A', '19')
    monkeypatch.setenv('INPUT_B', '23')
    result = app.add()
    assert result == 42


# We can also test the cases when the environment variables
# are not set or only some of them are set.
def test_app_no_a(monkeypatch):
    with pytest.raises(Exception) as err:
        app.add()
    assert str(err.value) == 'missing INPUT_A'

def test_app_no_b(monkeypatch):
    monkeypatch.setenv('INPUT_A', '0')
    with pytest.raises(Exception) as err:
        app.add()
    assert str(err.value) == 'missing INPUT_B'
