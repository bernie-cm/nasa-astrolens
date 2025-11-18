from flask import Flask, render_template, request
import requests

# app = Flask(__name__)
NASA_API_KEY = os.environ.get('NASA_API_KEY')

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     return render_template('index.html')

# @app.errorhandler(404)
# def not_found(error):
#     return render_template('error.html'), 404

def create_app():
    app = Flask(__name__)
    return app