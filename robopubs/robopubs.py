from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from robopubs.database import db
from robopubs.models import Publication, PublicationSchema

app = Flask(__name__)
app.config.from_object('robopubs.default_settings')
app.config.from_envvar('ROBOPUBS_SETTINGS')
db.init_app(app)

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
