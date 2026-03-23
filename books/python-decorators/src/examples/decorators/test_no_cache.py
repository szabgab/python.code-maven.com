from no_cache import compute

def test_compute(capsys):
    assert compute(2, 3) == 5
    out, err = capsys.readouterr()
    assert err == ''
    assert out == 'Called with 2 and 3\n'

    assert compute(3, 4) == 7
    out, err = capsys.readouterr()
    assert err == ''
    assert out == 'Called with 3 and 4\n'

    assert compute(2, 3) == 5
    out, err = capsys.readouterr()
    assert err == ''
    assert out == 'Called with 2 and 3\n'

