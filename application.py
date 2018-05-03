from flask import Flask, jsonify, request

from models.publication import Publication, PublicationSchema

app = Flask(__name__)

data = [
	Publication("abstract1", "title1"),
	Publication("abstract1", "title2")
]

@app.route("/")
def index():
	return "<h1>Hello World</h1>"

@app.route("/search")
def search():
	schema = PublicationSchema(many=True)
	query = request.args.get("q")
	if query is None:
		return "<h1>No query</h1>"

	pubs = schema.dump(
		filter(lambda t: query in t.title, data)
	)
	return jsonify(pubs.data)

if __name__ == '__main__':
	app.run(host='0.0.0.0')
