from src.core.ports.primary import CreateUserParams, SigninParams
from src.presentation.factories import create_user_factory, signin_factory
from src.presentation.validators import HttpGenericValidator
from src.presentation.helpers.http_status_code import HttpStatusCode
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
            return jsonify({'message': message}), HttpStatusCode.BAD_REQUEST

        response, success = usecase.create(
            CreateUserParams(
                str(body['username']),
                str(body['password']),
                str(body['name']),
                str(body['email']),
                str(body['profile_image_url']) if 'profile_image_url' in body else None,
                str(body['bio']) if 'bio' in body else None
            )
        )
    
        return jsonify(response), HttpStatusCode.CREATED if success else HttpStatusCode.BAD_REQUEST

    except Exception:
        print(format_exc(), flush=True)
        return jsonify({'message': 'Internal server error'}), HttpStatusCode.INTERNAL_SERVER_ERROR


@api_routes.route('/api/user/signin', methods=['POST'])
def signin():
    try:
        usecase = signin_factory()
        body = request.json
        required_fields = ['username', 'password']
        is_valid_request, message = HttpGenericValidator.validate(required_fields, body)
        if not is_valid_request:
            return jsonify({'message': message}), HttpStatusCode.BAD_REQUEST

        response, success = usecase.signin(
            SigninParams(
                str(body['username']),
                str(body['password'])
            )
        )
    
        return jsonify(response), HttpStatusCode.OK if success else HttpStatusCode.BAD_REQUEST

    except Exception:
        print(format_exc(), flush=True)
        return jsonify({'message': 'Internal server error'}), HttpStatusCode.INTERNAL_SERVER_ERROR
