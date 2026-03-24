import pytest

@pytest.fixture()
def check_out(capsys):
    def mycheck(expected_out):
        out, err = capsys.readouterr()
        assert err == ''
        assert out == expected_out
    return mycheck

