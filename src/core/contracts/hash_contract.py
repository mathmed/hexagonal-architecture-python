from abc import ABC, abstractmethod

class HashContract(ABC):
    @abstractmethod
    def encode(self, string: str) -> str:
        raise Exception('Method not implemented')
