from flask import Flask
from flask_restful import Api, Resource, abort
from passwordgenerator.password_generator import PasswordGenerator
from passwordgenerator import api, app

passsword_generator = PasswordGenerator()

class Password(Resource):
    def get(self, password_count):
        if password_count > 20:
            abort(f"input of {password_count} is greater than the maximum 20")
        data = passsword_generator.generate(password_count)
        return data

class DefaultPassword(Resource):
    def get(self):
        default_password_size = 5
        data = passsword_generator.generate(default_password_size)
        return data

# input is assumed to be seperated by &
class CustomPassword(Resource):
    def get(self, user_string):
        return user_string

api.add_resource(Password, '/password/random/<int:password_count>')
api.add_resource(DefaultPassword, '/password/random')
api.add_resource(CustomPassword, '/password/<string:user_string>')