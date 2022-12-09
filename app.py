import os
import json
from flask import Flask
from flask import jsonify
import psycopg2

import requests

config = {k.lower(): v for k, v in os.environ.items()}
app = Flask(__name__)


@app.route('/', methods=['GET'])
def base_url():
    """Base url to test API."""

    # n = 6
    # res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))
    #
    # df_output_lines = [s.split() for s in os.popen("df -h /mnt/efs/fs1").read().splitlines()]
    #
    # config['disk'] = json.dumps({'disk_list': df_output_lines})
    #
    # with open("/mnt/efs/fs1/file-" + res + ".json", "w+") as f:
    #     json.dump(data, f)

    return jsonify(config)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
