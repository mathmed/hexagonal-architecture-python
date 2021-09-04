from src.core.ports.secundary import DatabasePort
from src.core.contracts import UserRepositoryContract, SaveUserParams, HashContract
from typing import Dict

class DatabaseMock(DatabasePort):
    def save(self, table: str, params: Dict) -> Dict:
        return {}
    def find_one(self, table: str, by: str, value: any) -> Dict:
        return {}


class UserRepositoryMock(UserRepositoryContract):
    def save(self, params: SaveUserParams):
        return {}
    def get(self, by: str, value: any, raise_error: bool = True):
        return {}

class HashMock(HashContract):
    def encode(self, string: str) -> str:
        return {}
