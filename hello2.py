from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

#Proof I did the dynamic route:
# 127.0.0.1 - - [21/Sep/2025 16:43:07] "GET / HTTP/1.1" 200 -
#127.0.0.1 - - [21/Sep/2025 16:43:20] "GET /user/Vivian HTTP/1.1" 200 