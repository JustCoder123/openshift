from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World'
@app.route('/home')
def hello_home():
	return 'Welcome To Home Page'

if __name__ == '__main__':
   app.run()
