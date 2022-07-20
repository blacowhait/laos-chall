from flask import Flask, request
from jinja2 import Environment

app = Flask(__name__)
Jinja2 = Environment()

@app.route("/")
def page():
    name = request.values.get('name')
    if name is None:
    	return "<p>Please write your Name!</p>"
    else:
	    output = Jinja2.from_string('Hello ' + name + '!').render()
	    return output

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)