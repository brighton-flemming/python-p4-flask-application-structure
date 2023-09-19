#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route
def index():
    return  '<h1>WElcome to your DOOM(!!_!!)!</h1>'
