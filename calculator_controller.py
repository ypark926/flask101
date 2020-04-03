###########################
# 1. import flask library
# HINT: sample/request_processing.py
###########################
import service.calculator as calculator
from http import HTTPStatus

from flask import Flask, request, jsonify


###########################
# 2. initialize your Flask application object
# HINT: sample/explicit_application_object.py
###########################
app = Flask(__name__)



###########################
# 3. define route paths for the following functions with the specified path and method
# HINT: sample/routing.py
# 4. and parse the request to get the user_input given the request type
# HINT: sample/request_processing.py
###########################


# path = '/mean', method = 'GET'
# request type = JSON
@app.route('/mean',methods=['GET'])
def mean():
	user_input = request.get_json()['input']

	results = calculator.mean(user_input)

	return jsonify({'output':results}), HTTPStatus.OK


# path = '/median', method = 'GET and POST'
# request type = Query
@app.route('/median',methods=['GET','POST'])
def median():
	user_input = request.args.get('input')

	user_input = list(map(int, user_input.split(',')))
	results = calculator.median(user_input)

	return jsonify({'output':results}), HTTPStatus.OK

# path = '/mode', method = 'POST'
# request type = Form
@app.route('/mode',methods=['POST'])
def mode():
	user_input = request.form.get('input')

	user_input = list(map(int, user_input))
	results = calculator.mode(user_input)

	return jsonify({'output':results}), HTTPStatus.OK


@app.route('/sum',methods=['GET'])
def sum():
	user_input = request.get_json()['input']

	result = calculator.sum(user_input)

	return jsonify({'output':result}), HTTPStatus.OK


# path = '/status', method = 'GET'
@app.route('/status')
def status():
	result = "Application is running"
	return result, HTTPStatus.OK



if __name__ == '__main__':
	###########################
	# 5. Start your flask app
	# HINT: sample/explicit_application_object.py
	###########################
		app.run(host='0.0.0.0',port=8080)
