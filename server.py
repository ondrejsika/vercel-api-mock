import os
import hashlib
import json
from flask import Flask, request


app = Flask(__name__)


@app.route('/v2/domains/<domain>/records', methods=["POST"])
def domains_create_record(domain):
    return json.dumps({"uid":"rec_"+hashlib.sha256(request.data).hexdigest()[:16]})


@app.route('/v2/domains/<domain>/records/<record_id>', methods=["DELETE"])
def domains_delete_record(domain, record_id):
    return json.dumps({})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80')
