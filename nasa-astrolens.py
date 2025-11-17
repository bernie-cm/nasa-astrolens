from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)
NASA_API_KEY = os.environ.get('NASA_API_KEY')

@app.route('/', methods=['GET', 'POST'])
def index():
    return '<h1>Hello World</h1>'

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404