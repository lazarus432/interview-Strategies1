from flask import Flask

app = Flask(__name__)

# import json and random library
import json
import random

@app.route('/')
def hello_world():
	return "Hello World!"

# create a new route 
@app.route('/rolldice')
def diceRoll1():
	# run random function and store the result in a local variable
	die2 = random.randint(1,6)
	die1 = random.randint(1,6)
	total = die1 + die2
	# return values in json format
	return json.dumps({'total': total, 'value1': die1, 'value2': die2})


if __name__ == '__main__':
	app.debug = True
	# run the application on localhost port 8000
	app.run(host='127.0.0.1', port=8000)