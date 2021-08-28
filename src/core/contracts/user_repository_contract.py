from abc import ABC, abstractmethod
from typing import Dict
import dataclasses as dc

@dc.dataclass(unsafe_hash=True)
class SaveUserParams:
    username: str
    password: str
    name: str

class UserRepositoryContract(ABC):
    @abstractmethod
    def save(self, params: SaveUserParams) -> Dict:
        raise Exception('Method not implemented')
