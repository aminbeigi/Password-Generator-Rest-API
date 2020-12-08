from flask import Flask
from flask_restful import Api, Resource
from password_generator import PasswordGenerator

app = Flask(__name__)
api = Api(app)
passsword_generator = PasswordGenerator()

class Password(Resource):
    def get(self, password_num):

        return {
            "data": { "passwords": passsword_generator.generate(3)}
            }

api.add_resource(Password, '/password/<int:password_num>')

if __name__ == "__main__":
    app.run(debug=True)