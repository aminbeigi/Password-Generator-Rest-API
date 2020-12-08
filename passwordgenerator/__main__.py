from flask import Flask
from flask_restful import Api, Resource
from passwordgenerator.password_generator import PasswordGenerator
from passwordgenerator import api, app

passsword_generator = PasswordGenerator()

class Password(Resource):
    def get(self, password_count):
        data = passsword_generator.generate(password_count)
        return data

api.add_resource(Password, '/password/random/<int:password_count>')