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

    try:
        sky_database_creds = json.loads(os.environ['SKY_DATABASE_CREDS'])

        config['sky_database_creds_2'] = sky_database_creds
        config['status1'] = 'fetched db creds'
    except:
        config['status1'] = 'unable to fetch db creds'

    try:
        conn = psycopg2.connect(
            database=sky_database_creds['dbname'],
            user=sky_database_creds['username'],
            password=sky_database_creds['password'],
            host=sky_database_creds['host'],
            port=sky_database_creds['port'],
            connect_timeout=3
        )
        config['status2'] = 'connected'
    except:
        config['status2'] = 'unable to connect'
        print("I am unable to connect to the database")

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
