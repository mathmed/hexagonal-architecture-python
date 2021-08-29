from src.core.errors import UserNotFoundError
from src.core.models import UserModel
from src.core.ports.secundary import DatabasePort
from src.core.contracts import UserRepositoryContract, SaveUserParams

class UserRepository(UserRepositoryContract):

    def __init__(
        self,
        db_adapter: DatabasePort
    ):
        self.table_name = 'users'
        self.db_cliente = db_adapter

    def save(self, params: SaveUserParams) -> UserModel:
        dict_params = params.__dict__
        saved_user = self.db_cliente.save(self.table_name, dict_params)
        return UserModel(
            saved_user['username'],
            saved_user['password'],
            saved_user['name'],
            saved_user['email'],
            saved_user['profile_image_url'],
            saved_user['bio'],
        )

    def get(self, by: str, value: any, raise_error: bool = True) -> UserModel:

        user = self.db_cliente.find_one(self.table_name, by, value)
        
        if not user and raise_error:
            raise UserNotFoundError()
        
        if user:
            return UserModel(
                user['username'],
                user['password'],
                user['name'],
                user['email'],
                user['profile_image_url'],
                user['bio'],
            )
