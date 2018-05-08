from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import ModelSchema

db = SQLAlchemy()

class Publication(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(255), unique=True)
	abstract = db.Column(db.String(255), unique=True)

	def __init__(self, title, abstract):
		self.title = title
		self.abstract = abstract

	def __repr__(self):
		return '<Publication %r>' % self.title

class PublicationSchema(ModelSchema):
	class Meta:
		model = Publication