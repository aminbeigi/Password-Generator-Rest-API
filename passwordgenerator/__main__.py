from flask import Flask, request
from flask_restful import Api, Resource, abort
from passwordgenerator.data_generator import DataGenerator
from passwordgenerator import api, app

"""A restful API"""

data_generator = DataGenerator()

class DefaultRandomPassword(Resource):
    def get(self):
        default_password_size = 5
        data = data_generator.generate_random(default_password_size)
        return data

class RandomPassword(Resource):
    def get(self, data_length_count):
        if data_length_count > 20:
            abort(f"input of {data_length_count} is greater than the maximum 20")
        data = data_generator.generate_random(data_length_count)
        return data

class DefaultCustomPassword(Resource):
    def get(self, user_input):
        default_password_size = 5
        data = data_generator.generate_custom(default_password_size, user_input)
        return data

# input is assumed to be seperated by &
class CustomPassword(Resource):
    def get(self, user_input, data_length_count):
        if data_length_count > 20:
            abort(f"input of {data_length_count} is greater than the maximum 20")
        data = data_generator.generate_custom(data_length_count, user_input)
        return data

api.add_resource(DefaultRandomPassword, '/password/random')
api.add_resource(RandomPassword, '/password/random/<int:data_length_count>')
api.add_resource(DefaultCustomPassword, '/password/<string:user_input>')
api.add_resource(CustomPassword, '/password/<string:user_input>/<int:data_length_count>')