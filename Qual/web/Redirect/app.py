from flask import Flask, render_template, make_response
from flask import request

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route("/")
def home():
	resp = make_response(render_template('index.html'), 302)
	resp.headers['Location'] = "/swipers"
	return resp

@app.route("/swipers")
def flag():
	return render_template('swipers.html')


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=3000, debug=True)