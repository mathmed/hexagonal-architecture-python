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
    def save(self, params: SaveUserParams) -> Dict:
        raise Exception('Method not implemented')
