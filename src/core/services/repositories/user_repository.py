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
