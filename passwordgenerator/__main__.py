from flask import Flask
from flask_restful import Api, Resource
from password_generator import PasswordGenerator

app = Flask(__name__)
api = Api(app)
passsword_generator = PasswordGenerator()

class Password(Resource):
    def get(self, password_num):
        data = passsword_generator.generate(1)
        words = data['words']
        passwords = data['passwords']
        return {
            "data": { 
                "words": words,
                "passwords": passwords
                }
            }

api.add_resource(Password, '/password/random/<int:password_num>')

if __name__ == "__main__":
    app.run(debug=True)