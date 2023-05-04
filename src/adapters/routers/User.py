from flask import request, jsonify
from ..controllers.User import UserController
from server import app
from ..helpers.check_json import check_json_structure


@app.route("/user/create", methods=["POST"])
def create_user():
    data_json = request.get_json()
    response = UserController.save_user_controller(data_json)
    return response
