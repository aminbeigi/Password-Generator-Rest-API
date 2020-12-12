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
                abort(413, error = {
                    'message': f'input of {limit} is greater than the maximum 20',
                    'error code': '413'
                })
                data = data_generator.generate_random(limit)
                return data

        data = data_generator.generate_random()
        return data

# input is assumed to be seperated by &
class CustomPassword(Resource):
    
    args = {
        'words': fields.List(fields.Str()),
        'limit': fields.Int(required=False)
    }

    @use_args(args, location="query")
    def get(self, args):
        word_lst = args['words']

        """
        # user inputs a limit
        if len(args['limit']) != 0:
            limit = args['limit']
            if limit > 20:
                abort(413, error = {
                    'message': f'input of {limit} is greater than the maximum 20',
                    'error code': '413'
                })
                data = data_generator.generate_custom(limit)
                return data
        """

        data = data_generator.generate_custom(word_lst)
        return data

# This error handler is necessary for usage with Flask-RESTful
@parser.error_handler
def handle_request_parsing_error(err, req, schema, *, error_status_code, error_headers):
    """webargs error handler that uses Flask-RESTful's abort function to return
    a JSON error response to the client.
    """
    abort(error_status_code, errors=err.messages)

api.add_resource(RandomPassword, '/api/password/random')

api.add_resource(CustomPassword, '/api/password')