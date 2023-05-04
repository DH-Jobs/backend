from ...useCases.User.Save import SaveUser
from flask import jsonify, make_response
from ..database.Operations import OperationsDatabase


class UserController:

    @staticmethod
    def save_user_controller(data):
        db = OperationsDatabase("user")
        response_user = SaveUser(data, db).save()
        response_json = jsonify(response_user['data'])
        response = make_response(response_json, response_user['code'])
        response.headers['Content-Type'] = 'application/json'
        return response
