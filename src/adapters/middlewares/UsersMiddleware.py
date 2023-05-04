from flask import request, jsonify
from server import app
from ..helpers.check_json import check_json_structure


@app.before_request
def validate_request():
    if request.path == "/user/create" and request.method == "POST":
        data_json = request.get_json()
        if not check_json_structure(data_json):
            return jsonify({"message": "INVALID JSON"}), 400
