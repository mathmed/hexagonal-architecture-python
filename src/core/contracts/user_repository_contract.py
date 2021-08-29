from src.core.models import UserModel
from abc import ABC, abstractmethod
from typing import Dict
import dataclasses as dc

@dc.dataclass(unsafe_hash=True)
class SaveUserParams:
    username: str
    password: str
    name: str
    email: str
    profile_image_url: str = None
    bio: str = None

class UserRepositoryContract(ABC):
    @abstractmethod
    def save(self, params: SaveUserParams) -> UserModel:
        raise Exception('Method not implemented')

    def get(self, by: str, value: any, raise_error: bool = True) -> UserModel:
        raise Exception('Method not implemented')
