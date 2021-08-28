from src.core.ports.primary import CreateUserParams
from src.presentation.factories import create_user_factory
from flask import jsonify, request, Blueprint

api_routes = Blueprint('api_routes', __name__)

@api_routes.route('/api/user', methods=['POST'])
def create_user():
    usecase = create_user_factory()
    params = request.json
    response = usecase.create(CreateUserParams(params['username'], params['password'], params['name']))
    return jsonify({'data': response}), 200
