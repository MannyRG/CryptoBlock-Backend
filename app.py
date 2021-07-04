from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import requests


DEBUG = True
PORT = 8000

# Initialize an instance of the Flask class.
# This starts the website!
app = Flask(__name__)


# The default URL ends in / ("my-website.com/").
@app.route('/', methods=["GET"])
def index():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
    'start':'1',
    'limit':'200',
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '6f1b645f-6faf-4e3d-87ab-8d9d9089d76d',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        return data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        return e

 



CORS(app, origins="*", supports_credentials=True)


# Run the app when the program starts!
if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)