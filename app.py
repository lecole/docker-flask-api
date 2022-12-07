import os
import json
from flask import Flask
from flask import jsonify

config = {k.lower(): v for k, v in os.environ.items()}
app = Flask(__name__)


@app.route('/', methods=['GET'])
def base_url():
    """Base url to test API."""

    df_output_lines = [s.split() for s in os.popen("df -Ph").read().splitlines()]

    config['disk'] = json.dumps({'disk_list': df_output_lines})

    sky_database_creds = json.loads(config['sky_database_creds'])

    config.update(sky_database_creds)

    # with open("/mnt/efs/fs1/file.json", "w+") as f:
    #     json.dump(config, f)

    ls_list = [s.split() for s in os.popen("ls /mnt/efs/fs1").read().splitlines()]

    config['ls_list'] = json.dumps({'ls_list': ls_list})

    return jsonify(config)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
