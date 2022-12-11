import os
import json
from flask import Flask
from flask import jsonify
import psycopg2

import random
import string

config = {k.lower(): v for k, v in os.environ.items()}
app = Flask(__name__)


@app.route('/', methods=['GET'])
def base_url():
    """Base url to test API."""

    print('dd')

    return jsonify(config)


@app.route('/rds', methods=['GET'])
def rds_url():
    """Base url to test API."""

    print('dd')

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
            port=str(sky_database_creds['port']),
            connect_timeout=3
        )
        config['status2'] = 'connected'
    except:
        config['status2'] = 'unable to connect'
        print("I am unable to connect to the database")

    return jsonify(config)


@app.route('/efs', methods=['GET'])
def efs_url():
    """Base url to test API."""

    print('dd')

    data = {
        "pk": "da0tbtlojyizz8wolqgmitxwc6ez8i:infra:app_def",
        "services": [
            {"albFacing": "internet-facing",
             "containerDefinitions": [{
                 "containerId": "skyderafrontendo0xjaivpqp8kuclz",
                 "containerName": "Web Hello World",
                 "envs": [
                     {
                         "key": "ddd",
                         "value": "ww",
                         "valueType": "value"}],
                 "essentialContainer": "yes",
                 "expose": "80",
                 "files": [],
                 "image": "tutum/hello-world",
                 "imageProvider": "docker",
                 "ports": [
                     {
                         "port": "80",
                         "protocol": "tcp"}]},
                 {
                     "containerId": "thisredis",
                     "containerName": "This Redis",
                     "essentialContainer": "yes",
                     "image": "redis:alpine",
                     "imageProvider": "docker",
                     "ports": [
                         {
                             "port": "8080",
                             "protocol": "tcp"}]}],
             "cpu": "512",
             "createdAt": 1667543988,
             "memory": "1024",
             "serviceId": "skyderafrontend:o0xjaivpqp8kuclz",
             "serviceName": "Skydera Frontend",
             "serviceType": "container",
             "type": "service",
             "desiredCount": "1",
             "hostUri": "sss"},
            {
                "containerDefinitions": [
                    {"albFacing": "internal",
                     "buildArgs": [{"key": "dd",
                                    "value": "ddd"},
                                   {
                                       "key": "eee",
                                       "value": "eee"}],
                     "buildMode": "dockerfile",
                     "containerId": "skyderabackendseconduqd04lv0oyalu6o1",
                     "containerName": "Git app Hello World Second",
                     "expose": "80",
                     "gitConfig": {
                         "branch": "main",
                         "gitIntgAccessId": "xdkflroflskdktl",
                         "repoFullname": "lecole/docker-helloworld"},
                     "image": "da0tbtlojyizz8wolqgmitxwc6ez8i/i4r6ngkoq7srzh2/lecole/docker-helloworld",
                     "imageProvider": "ecr",
                     "ports": [{"port": "80",
                                "protocol": "tcp"},
                               {"port": "8080",
                                "protocol": "tcp"}]}],
                "cpu": "512",
                "createdAt": 1667543988,
                "memory": "1024",
                "serviceId": "skyderabackendsecond:uqd04lv0oyalu6o1",
                "serviceName": "Skydera Backend Second",
                "serviceType": "git",
                "type": "service",
                "desiredCount": "1",
                "hostUri": "ddd",
                "albFacing": "internet-facing"},
            {"containerDefinitions": [
                {"albFacing": "internet-facing",
                 "buildArgs": [{"key": "dd",
                                "value": "ddd"},
                               {"key": "eee",
                                "value": "eee"}],
                 "buildMode": "dockerfile",
                 "containerId": "skyderabackendjudvqmpzcymqug5s",
                 "containerName": "Git app Hello World",
                 "expose": "80",
                 "gitConfig": {"branch": "main",
                               "gitIntgAccessId": "xdkflroflskdktl",
                               "repoFullname": "lecole/docker-helloworld"},
                 "image": "da0tbtlojyizz8wolqgmitxwc6ez8i/lpzudszykwmcafg/lecole/docker-helloworld",
                 "imageProvider": "ecr",
                 "ports": [{"port": "80",
                            "protocol": "tcp"},
                           {"port": "8080",
                            "protocol": "tcp"}]}],
                "cpu": "512",
                "createdAt": 1667543989,
                "memory": "1024",
                "serviceId": "skyderabackend:judvqmpzcymqug5s",
                "serviceName": "Skydera Backend",
                "serviceType": "git",
                "type": "service",
                "desiredCount": "1",
                "hostUri": "sssddd",
                "albFacing": "internet-facing"}],
        "skGsi1Pk": "m6qqcg41drvng0u:it0bfqoegledqbz", "versionStr": "v1", "appDefId": "it0bfqoegledqbz",
        "catalogId": "m6qqcg41drvng0u", "runName": "R1", "channelType": "rapid", "stage": "production",
        "namespace": "us-east-2:pixztmslywvj4hcn", "hostZone": "helpmatrix.co", "deploy": False,
        "expose": "80", "ports": [{"port": 80, "protocol": "tcp"}]}

    n = 6
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))

    with open("/mnt/efs/fs1/file-" + res + ".json", "w+") as f:
        json.dump(data, f)

    df_output_lines = [s.split() for s in os.popen("df -h /mnt/efs/fs1").read().splitlines()]

    config['disk'] = json.dumps({'disk_list': df_output_lines})

    files_output_lines = [s.split() for s in os.popen("ls -df /mnt/efs/fs1").read().splitlines()]

    config['files'] = json.dumps({'disk_files': files_output_lines})

    dir_list = os.listdir('/mnt/efs/fs1')

    config['dir_list'] = json.dumps({'dir_list': dir_list})

    return jsonify(config)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

