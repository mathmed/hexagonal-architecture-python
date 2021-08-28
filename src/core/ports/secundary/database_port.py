from abc import ABC, abstractmethod
from typing import Dict

class DatabasePort(ABC):
    @abstractmethod
    def save(self, table: str, params: Dict) -> Dict:
        raise Exception('Method not implemented')
