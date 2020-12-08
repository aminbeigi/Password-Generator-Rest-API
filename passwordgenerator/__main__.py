from flask import Flask
from flask_restful import Api, Resource
from password_generator import PasswordGenerator

app = Flask(__name__)
api = Api(app)
passsword_generator = PasswordGenerator()

class Password(Resource):
    def get(self, password_count):
        data = passsword_generator.generate(password_count)
        return data

api.add_resource(Password, '/password/random/<int:password_count>')

if __name__ == "__main__":
    app.run(debug=True)