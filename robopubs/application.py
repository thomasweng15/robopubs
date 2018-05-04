from flask import Flask, jsonify, request

from robopubs.models.publication import Publication, PublicationSchema

app = Flask(__name__)

data = [
	Publication("0", "abstract0", "title0"),
	Publication("1", "abstract1", "title1")
]

@app.route("/")
def index():
	return "<h1>Hello World!</h1>"

@app.route('/api/v1.0/pubs', methods=['GET'])
def get_pubs():
	schema = PublicationSchema(many=True)
	pubs = schema.dump(data)
	return jsonify(pubs.data)

if __name__ == '__main__':
	app.run(host='0.0.0.0')
