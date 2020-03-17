from flask import Flask 

app = Flask(__name__)

@app.route('/')
def Hello_world():
	return 'Hello, World!'


if __name__ == '__main__':
	app = create_app()
	app.run(debug=False, port= 8000, host='0.0.0.0')
