import os
import json
from flask import Flask
from flask import jsonify
import string
import random

import requests

config = {k.lower(): v for k, v in os.environ.items()}
app = Flask(__name__)

data = {
    'employees': [
        {
            'name': 'John Doe',
            'department': 'Marketing',
            'place': 'Remote'
        },
        {
            'name': 'Jane Doe',
            'department': 'Software Engineering',
            'place': 'Remote'
        },
        {
            'name': 'Don Joe',
            'department': 'Software Engineering',
            'place': 'Office'
        }
    ]
}


@app.route('/', methods=['GET'])
def base_url():
    """Base url to test API."""

    n = 6
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))

    df_output_lines = [s.split() for s in os.popen("df -h /mnt/efs/fs1").read().splitlines()]

    config['disk'] = json.dumps({'disk_list': df_output_lines})

    with open("/mnt/efs/fs1/file-" + res + ".json", "w+") as f:
        json.dump(data, f)

    # sky_database_creds = json.loads(config['sky_database_creds'])

    # config.update(sky_database_creds)
    # with open("/mnt/efs/fs1/file.json", "w+") as f:
    #     json.dump(config, f)

    # file_url = "https://www.db-book.com/slides-dir/PDF-dir/ch5.pdf"
    #
    # r = requests.get(file_url, stream=True)
    #
    # n = 6
    # res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))
    #
    # with open("/mnt/efs/fs1/python_" + res + ".pdf", "wb") as pdf:
    #     for chunk in r.iter_content(chunk_size=1024):
    #         if chunk:
    #             pdf.write(chunk)

    ls_list = [s.split() for s in os.popen("ls /mnt/efs/fs1").read().splitlines()]
    # ls_list_2 = [s.split() for s in os.popen("ls /9f542e19b0a4/offd5spcaimmmmdh/data/mnt/efs/fs1:/mnt/efs/fs1").read().splitlines()]
    # ls_list_3 = [s.split() for s in
    #              os.popen("ls /9f542e19b0a4/offd5spcaimmmmdh/data/mnt/efs/fs1").read().splitlines()]

    config['ls_list'] = json.dumps({'ls_list': ls_list})

    config['ls_list2'] = json.dumps({'ls_list': ls_list})

    return jsonify(config)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
