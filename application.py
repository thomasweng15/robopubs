from flask import Flask, jsonify
app = Flask(__name__)

data = [
	{"abstract": "abstract1", "title": "title1"}
]

@app.route("/")
def index():
	return jsonify(data)

if __name__ == '__main__':
	app.run(host='0.0.0.0')
