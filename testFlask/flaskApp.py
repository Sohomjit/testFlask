from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return '<h1> Hello Welcome to my App !'

@app.route('/<name>')

def name_index(name):
    return '<h1> Hello {} Welcome to my App !'.format(name)
