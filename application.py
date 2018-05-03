from flask import Flask, jsonify

from models.publication import Publication, PublicationSchema

app = Flask(__name__)

data = [
	Publication("abstract1", "title1"),
	Publication("abstract1", "title2")
]

@app.route("/")
def index():
	schema = PublicationSchema(many=True)
	query = "title2"
	pubs = schema.dump(
		filter(lambda t: query in t.title, data)
	)
	return jsonify(pubs.data)

if __name__ == '__main__':
	app.run(host='0.0.0.0')
