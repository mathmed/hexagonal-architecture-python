from src.core.errors import UserNotFoundError
from src.core.models import UserModel
from src.core.ports.secundary import DatabasePort
from src.core.contracts import UserRepositoryContract, SaveUserParams
from typing import Dict

class UserRepository(UserRepositoryContract):

    def __init__(
        self,
        db_adapter: DatabasePort
    ):
        self.table_name = 'users'
        self.db_cliente = db_adapter

    def save(self, params: SaveUserParams) -> Dict:
        dict_params = params.__dict__
        result = self.db_cliente.save(self.table_name, dict_params)
        return result

    def get(self, by: str, value: any, raise_error: bool = True) -> UserModel:

        user = self.db_cliente.find_one(self.table_name, by, value)
        
        if not user and raise_error:
            raise UserNotFoundError()
        
        return UserModel(
            user['username'],
            user['password'],
            user['name'],
            user['email'],
            user['profile_image_url'],
            user['bio'],
        )
