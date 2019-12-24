import os
import hashlib
import json
import dataset
from flask import Flask, request


app = Flask(__name__)
db = dataset.connect("sqlite:///db.sqlite3")


@app.route("/v2/domains/<domain>/records", methods=["GET"])
def domains_get_records(domain):
    print('GET RECORD "%s"' % (domain))
    return json.dumps(
        {
            "records": [
                {
                    "id": rec["uid"],
                    "name": rec["name"],
                    "type": rec["type"],
                    "value": rec["value"],
                }
                for rec in db["records"].find()
            ]
        }
    )


@app.route("/v2/domains/<domain>/records", methods=["POST"])
def domains_create_record(domain):
    print(
        'CREATE RECORD "%s" type="%s" name="%s" value="%s"'
        % (domain, request.json["type"], request.json["name"], request.json["value"])
    )
    uid = "rec_" + hashlib.sha256(request.data).hexdigest()[:16]

    record = {}
    record.update({"uid": uid, "domain": domain})
    record.update(request.json)
    db["records"].insert(record)

    return json.dumps({"uid": uid})


@app.route("/v2/domains/<domain>/records/<record_id>", methods=["DELETE"])
def domains_delete_record(domain, record_id):
    db["records"].delete(domain=domain, uid=record_id)
    print('DELETE RECORD "%s" (domain="%s")' % (record_id, domain))
    return json.dumps({})


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port="80", threaded=False, processes=1)
