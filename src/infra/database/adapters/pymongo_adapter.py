from src.core.ports.secundary import DatabasePort
from pymongo import MongoClient
from typing import Dict
from json import loads, dumps
import os


class PyMongoAdapter(DatabasePort):
    def __init__(self):
        self.client = MongoClient('mongodb://{}:{}/'.format(os.getenv('DB_HOST'), os.getenv('DB_PORT')))
        self.db = self.client[os.getenv('DB_DATABASE')]
    
    def _parse_result(self, result: str) -> Dict:
        return loads(dumps(result, default=str))

    def save(self, table: str, params: Dict) -> Dict:
        table = self.db[table]
        table.insert_one(params).inserted_id
        return self._parse_result(params)
