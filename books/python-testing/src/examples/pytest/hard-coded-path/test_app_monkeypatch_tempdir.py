import app

def test_sum(monkeypatch, tmpdir):
    mocked_data_file = tmpdir.join('test_1.json')
    monkeypatch.setattr(app, 'data_file', mocked_data_file)

    res = app.do_something()
    ...

def test_again():
    res = app.do_something()    # back to the original value
    ...
