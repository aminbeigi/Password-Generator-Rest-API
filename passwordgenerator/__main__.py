from flask import Flask, request
from flask_restful import Api, Resource
from passwordgenerator.data_generator import DataGenerator
from passwordgenerator import api, app
from webargs import fields, validate
from webargs.flaskparser import use_args, use_kwargs, parser, abort

"""The Password-Generator Restful API

This API will take in words as a parameter or will randomly generate them and
a response limit or will be defaulted to DEFAULT_LIMIT. The response will have
the given paramters, related words and a string of text created by concatenating
and altering the related words to make them look more cryptic like.
"""

data_generator = DataGenerator()
DEFAULT_LIMIT = 5
API_RESPONSE_LIMIT = 20
ERROR_MESSAGE_422 = f'input is greater than the maximum 20'

class RandomPassword(Resource):
    args = {
        'limit': fields.Int(required=False)
    }

    @use_args(args, location="query")
    def get(self, args):

        # if user didn't specify limit default to DEFAULT_LIMIT
        limit = DEFAULT_LIMIT if 'limit' not in args else args['limit']
    
        if limit > API_RESPONSE_LIMIT:
            abort(422, message = ERROR_MESSAGE_422)

        data = data_generator.generate_random(limit)
        return data

class CustomPassword(Resource):
    args = {
        'words': fields.List(fields.Str()),
        'limit': fields.Int(required=False)
    }

    @use_args(args, location="query")
    def get(self, args):
        word_lst = args['words']

        # if user didn't specify limit default to DEFAULT_LIMIT
        limit = DEFAULT_LIMIT if 'limit' not in args else args['limit']
    
        if limit > API_RESPONSE_LIMIT:
            abort(422, message = ERROR_MESSAGE_422)

        data = data_generator.generate_custom(word_lst, limit)
        return data

# This error handler is necessary for usage with Flask-RESTful
@parser.error_handler
def handle_request_parsing_error(err, req, schema, *, error_status_code, error_headers):
    """webargs error handler that uses Flask-RESTful's abort function to return
    a JSON error response to the client.
    """
    abort(error_status_code, errors=err.messages)

# create endpoints
api.add_resource(RandomPassword, '/api/password/random')
api.add_resource(CustomPassword, '/api/password')