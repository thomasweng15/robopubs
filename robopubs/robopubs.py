from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import ModelSchema

app = Flask(__name__)
app.config.from_object('robopubs.default_settings')
app.config.from_envvar('ROBOPUBS_SETTINGS')
db = SQLAlchemy(app)

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

@app.route("/")
def index():
	return "<h1>Hello World!</h1>"

@app.route('/api/v1.0/pubs', methods=['GET'])
def get_pubs():
	pubs = Publication.query.all()
	schema = PublicationSchema(many=True)
	dump = schema.dump(pubs)
	return jsonify(dump.data)

if __name__ == '__main__':
	app.run(host='0.0.0.0')
