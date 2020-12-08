from flask import Flask
from flask_restful import Api, Resource, abort
from passwordgenerator.password_generator import PasswordGenerator
from passwordgenerator import api, app

passsword_generator = PasswordGenerator()

class Password(Resource):
    def get(self, password_count):
        if password_count > 20:
            abort(f"input of {password_count} is greater than the maximum 20.")
        data = passsword_generator.generate(password_count)
        return data

api.add_resource(Password, '/password/random/<int:password_count>')