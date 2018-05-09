from robopubs import robopubs
from robopubs.models import Publication
from robopubs.database import db

with robopubs.app.app_context():
    db.create_all()
    pub1 = Publication(title="title1", abstract="abstract1")
    pub2 = Publication(title="title2", abstract="abstract2")
    db.session.add(pub1)
    db.session.add(pub2)
    db.session.commit()
    db.session.close()