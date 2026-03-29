import api
import pytest

@pytest.fixture()
def web():
    return api.app.test_client()

#def test_echo_get_with_param(web):
#    rv = web.get('/echo?text=hello')
#    assert rv.status == '200 OK'
#    assert rv.headers['Content-Type'] == 'application/json'
#    assert rv.json ==  {'res': 'Text: hello'}

#def test_echo_post_with_param(web):
#    rv = web.post('/echo', data={'text': 'ciao'}, headers={'Content-Type':'application/json'})
#    assert rv.status == '200 OK'
#    assert rv.headers['Content-Type'] == 'application/json'
#    assert rv.json == {'Answer': 'You said: ciao'}


def test_echo_bad_request_content_type(web):
    rv = web.post('/echo')
    assert rv.status == '415 UNSUPPORTED MEDIA TYPE'
    assert rv.headers['Content-Type'] == 'application/json'
    assert rv.json == {'message': "Did not attempt to load JSON data because the request Content-Type was not 'application/json'."}

#def test_echo_get_no_param(web):
#    # If the parameter is missing the parser just returns None
#    rv = web.get('/echo')
#    assert rv.status == '200 OK'
#    assert rv.headers['Content-Type'] == 'application/json'
#    assert rv.json ==  {'res': 'Text: None'}

#def test_echo_post_no_param(web):
#    rv = web.post('/echo')
#    assert rv.status == '200 OK'
#    assert rv.headers['Content-Type'] == 'application/json'
#    assert rv.json == {'Answer': 'You said: ciao'}


