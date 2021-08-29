from src.core.ports.primary import CreateUserParams, SigninParams
from src.presentation.factories import create_user_factory, signin_factory
from src.presentation.validators import HttpGenericValidator
from src.presentation.helpers.http_status_code import *
from traceback import format_exc
from flask import jsonify, request, Blueprint

api_routes = Blueprint('api_routes', __name__)

@api_routes.route('/api/user', methods=['POST'])
def create_user():
    try:
        usecase = create_user_factory()
        body = request.json
        required_fields = ['username', 'password', 'email', 'name']
        is_valid_request, message = HttpGenericValidator.validate(required_fields, body)

        if not is_valid_request:
            return jsonify({'message': message}), BAD_REQUEST

        response, success = usecase.create(
            CreateUserParams(
                body['username'],
                body['password'],
                body['name'],
                body['email'],
                body['profile_image_url'] if 'profile_image_url' in body else None,
                body['bio'] if 'bio' in body else None
            )
        )
    
        return jsonify(response), CREATED if success else BAD_REQUEST

    except Exception:
        print(format_exc(), flush=True)
        return jsonify({'message': 'Internal server error'}), INTERNAL_SERVER_ERROR


@api_routes.route('/api/user/signin', methods=['POST'])
def signin():
    try:
        usecase = signin_factory()
        body = request.json
        required_fields = ['username', 'password']
        is_valid_request, message = HttpGenericValidator.validate(required_fields, body)
        if not is_valid_request:
            return jsonify({'message': message}), BAD_REQUEST

        response, success = usecase.signin(
            SigninParams(
                body['username'],
                body['password']
            )
        )
    
        return jsonify(response), OK if success else BAD_REQUEST

    except Exception:
        print(format_exc(), flush=True)
        return jsonify({'message': 'Internal server error'}), INTERNAL_SERVER_ERROR
