import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello in the World full of masti with jayesh prajapati'
@app.route('/home')
def hello_home():
	return 'Welcome To Home Page of openshift appp '

if __name__ == '__main__':
   app.run(host="0.0.0.0",port= 8080)
