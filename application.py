from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from crud import User

application = Flask(__name__)
api = Api(application)


class Insert(Resource):
    def post(self):
        posted_data = request.get_json()

        email = posted_data["email"]
        first_name= posted_data["first_name"]
        last_name = posted_data["last_name"]
        id = posted_data["id"]

        my_user=User(email, first_name, last_name, id)
        my_user.insert_to_db()

        retMap = {

            'Status Code': 200
        }
        return jsonify(retMap)


class Update(Resource):
    def post(self):
        posted_data = request.get_json()

        email = posted_data["email"]
        first_name = posted_data["first_name"]


        User.update_table(email, first_name)

        retMap = {

            'Status Code': 200
        }
        return jsonify(retMap)


class Delete (Resource):
    def post(self):
        posted_data = request.get_json()

        email = posted_data["email"]
        User.delete_data(email)

        retMap = {

            'Status Code': 200
        }
        return jsonify(retMap)


api.add_resource(Insert,"/insert")
api.add_resource(Update,"/update")
api.add_resource(Delete,"/delete")





if __name__=="__main__":
    application.run(debug=True)
