import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello in the World of openshift by Jayesh prajapati '
@app.route('/home')
def hello_home():
	return 'Welcome To Home Page'

if __name__ == '__main__':
   app.run(host="0.0.0.0",port= 8080)
