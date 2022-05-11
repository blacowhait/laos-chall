from flask import Flask, render_template, make_response
from flask import request

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route("/")
def home():
	return render_template('index.html')


@app.route('/robots.txt', methods=['GET'])
def sitemap():
  response = make_response(open('robots.txt').read())
  response.headers["Content-type"] = "text/plain"
  return response

@app.route("/agent-exam")
def flag():
	normal = request.headers.get('User-Agent')
	if(normal == "Kingsman Agent 0x05"):
		return """
		<html>
			<h1>Congrats !!!</h1>
			<body>
				<p>Here's ur flag
				<p>LA2022{ur_now_our_agent0x05_linz_is_here}
			</body<
		</html>
		"""
	else:
		return """
			<html>
				<h1>U are fail to be an agent!</h1>
			</html>
		"""


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=3000, debug=True)