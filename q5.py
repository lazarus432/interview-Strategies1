from flask import Flask

app = Flask(__name__)

import json
import random

@app.route('/')
def hello_world():
	return "Hello World!"

@app.route('/rolldice')
def diceRoll1():
	die2 = random.randint(1,6)
	die1 = random.randint(1,6)
	total = die1 + die2
	return json.dumps({'total': total, 'value1': die1, 'value2': die2})



if __name__ == '__main__':
	app.debug = True
	app.run(host='127.0.0.1', port=8000)