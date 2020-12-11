from flask import Flask, request
from flask_restful import Api, Resource
from passwordgenerator.data_generator import DataGenerator
from passwordgenerator import api, app
from webargs import fields, validate
from webargs.flaskparser import use_args, use_kwargs, parser, abort

"""A restful API"""

data_generator = DataGenerator()

class RandomPassword(Resource):
    
    args = {
        'limit': fields.Int(required=False)
    }

    @use_args(args, location="query")
    def get(self, limit):
        # user inputs a limit
        if len(limit) != 0:
            limit = limit['limit']
            if limit > 20:
                abort({
                    'error': f'input of {limit} is greater than the maximum 20'
                }, 404)
                data = data_generator.generate_random(limit)
                return data

        data = data_generator.generate_random()
        return data

# input is assumed to be seperated by &
class DefaultCustomPassword(Resource):
    def get(self, user_input):
        default_password_size = 5
        data = data_generator.generate_custom(default_password_size, user_input)
        return data

class CustomPassword(Resource):
    def get(self, user_input, data_length_count):
        if data_length_count > 20:
            abort(f"input of {data_length_count} is greater than the maximum 20")
        data = data_generator.generate_custom(data_length_count, user_input)
        return data

# This error handler is necessary for usage with Flask-RESTful
@parser.error_handler
def handle_request_parsing_error(err, req, schema, *, error_status_code, error_headers):
    """webargs error handler that uses Flask-RESTful's abort function to return
    a JSON error response to the client.
    """
    abort(error_status_code, errors=err.messages)

api.add_resource(RandomPassword, '/password/random')

api.add_resource(DefaultCustomPassword, '/password/<string:user_input>')
api.add_resource(CustomPassword, '/password/<string:user_input>/<int:data_length_count>')