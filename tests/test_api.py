import pytest

from robopubs import robopubs

@pytest.fixture 
def client():
    robopubs.app.config['TESTING'] = True
    client = robopubs.app.test_client()

    yield client

def test_messages(client):
    """Test hello world.
    """

    rv = client.get('/', follow_redirects=True)
    assert b'<h1>Hello World!</h1>' in rv.data