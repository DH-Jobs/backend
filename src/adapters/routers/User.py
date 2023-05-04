from flask import request
from ..controllers.User import UserController
from server import app
from typing import Dict, List
from ...entities.User import User
import json

@app.route("/user/create", methods=["POST"])
def create_user():
    def check_user_type(user_data: Dict[str, object]) -> bool:
        try:
            user = User(**user_data)
            return True
        except TypeError:
            return False
    data_json = request.get_json()
    authorized_json = check_user_type(data_json)
    print(authorized_json)
    response = UserController.save_user_controller(data_json)
    return response
