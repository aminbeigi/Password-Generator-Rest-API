from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

from passwordgenerator.__main__ import *
app.run(debug=True)