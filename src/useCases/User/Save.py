from ...adapters.ErrorsHandling.User import UserAlreadyExist


class SaveUser:
    def __init__(self, person_data, db):
        self.db = db
        self.personData = person_data

    def save(self):
        try:
            user_save = self.db.save(self.personData)
            response = {
                "code": 201,
                "data": {
                    "message": "",
                    "body": user_save
                }

            }
            return response
        except UserAlreadyExist as e:
            response = {
                "code": 400,
                "data": {
                    "message": e.message,
                    "body": ""
                }

            }
            return response
