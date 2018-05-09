import os
import json
import pytest

from robopubs import robopubs
from robopubs.models import Publication
from robopubs.database import db as _db

@pytest.fixture(scope='session')
def app(request):
    """Session-wide test Flask applcation.
    """
    robopubs.app.config['TESTING'] = True
    client = robopubs.app.test_client()
    with robopubs.app.app_context():
        _db.create_all()
        populate_db(_db)
        yield client
        _db.session.close()
        _db.drop_all()

def populate_db(_db):
    pub1 = Publication(title="title1", abstract="abstract1")
    pub2 = Publication(title="title2", abstract="abstract2")
    _db.session.add(pub1)
    _db.session.add(pub2)

def test_hello_world(app):
    """Test hello world.
    """

    rv = app.get('/', follow_redirects=True)
    assert b'<h1>Hello World!</h1>' in rv.data

def test_get_pubs(app):
    """Test getting all publications.
    """

    rv = app.get('/api/v1.0/pubs')
    d = rv.get_json()
    assert len(d['publications']) > 1