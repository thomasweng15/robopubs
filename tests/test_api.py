import pytest

from robopubs import application

@pytest.fixture 
def client():
    application.config['TESTING'] = True
    client = application.test_client()

    yield client

