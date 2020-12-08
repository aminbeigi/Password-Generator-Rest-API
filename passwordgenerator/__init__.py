from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

from passwordgenerator import __main__