from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from robopubs.database import db
from robopubs.models import Publication, PublicationSchema

app = Flask(__name__)
app.config.update(
	DEBUG = os.getenv('DEBUG'),
	SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI'),
	SQLALCHEMY_TRACK_MODIFICATIONS=os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
)
db.init_app(app)

@app.route("/")
def index():
	return "<h1>Hello World!</h1>"

@app.route('/api/v1.0/pubs', methods=['GET'])
def get_pubs():
	pubs = Publication.query.all()
	schema = PublicationSchema(many=True)
	dump = schema.dump(pubs)
	return jsonify({'publications': dump.data})

if __name__ == '__main__':
	app.run(host='0.0.0.0')
