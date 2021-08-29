from abc import ABC, abstractmethod
import dataclasses as dc
from typing import Dict, Tuple

@dc.dataclass(unsafe_hash=True)
class SigninParams:
    username: str
    password: str

class SigninPort(ABC):
    @abstractmethod
    def signin(self, params: SigninParams) -> Tuple[Dict, bool]:
        raise Exception('Method not implemented')
