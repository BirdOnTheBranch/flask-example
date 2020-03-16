from flask import Flask 

app = Flask(__name__)

@app.route('/')
def Hello_world():
	return 'Hola mundo'

app.run(debug=False, port= 8000, host='0.0.0.0')
