import os
from flask import Flask
from flask import jsonify

config = {k.lower(): v for k, v in os.environ.items() }
app = Flask(__name__)

@app.route('/', methods=['GET'])
def base_url():
    """Base url to test API."""

    config['response'] = 'Hello world!'

    response = config

    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
