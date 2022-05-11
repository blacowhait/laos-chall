#/usr/bin/python3

from flask import Flask, render_template, make_response

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route("/")
def home():
	return render_template('index.html')


@app.route('/robots.txt', methods=['GET'])
def sitemap():
  response = make_response(open('robots.txt').read())
  response.headers["Content-type"] = "text/plain"
  return response

@app.route("/linz-is-here")
def flag():
	return """
	<html>
		<h1>Congrats !!!</h1>
		<body>
			<p>Here's ur flag
			<p>LA2022{robootssssssss_a_little_information_linz_is_here}
		</body<
	</html>"""


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=3000, debug=True)
