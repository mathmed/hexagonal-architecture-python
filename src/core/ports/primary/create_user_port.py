from abc import ABC, abstractmethod
import dataclasses as dc
from typing import Dict, Tuple

@dc.dataclass(unsafe_hash=True)
class CreateUserParams:
    username: str
    password: str
    name: str
    email: str
    profile_image_url: str = None
    bio: str = None

class CreateUserPort(ABC):
    @abstractmethod
    def create(self, params: CreateUserParams) -> Tuple[Dict, bool]:
        raise Exception('Method not implemented')
