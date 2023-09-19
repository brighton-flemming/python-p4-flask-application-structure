#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return  '<h1>Welcome to your DOOM(!!_!!)!</h1>'

@app.route('/<string:username>')
def user(username):
    return f'<h1>Welcome {username}! Now you are on the list!</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
