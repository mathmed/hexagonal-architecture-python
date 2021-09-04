from src.core.ports.secundary import DatabasePort
from pymongo import MongoClient
from typing import Dict
from json import loads, dumps
import os


class PyMongoAdapter(DatabasePort):

    _instance = None
    _client = None
    _db = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._client:
            self._client = MongoClient('mongodb://{}:{}/'.format(os.getenv('DB_HOST'), os.getenv('DB_PORT')))
            self._db = self._client[os.getenv('DB_DATABASE')]

    def _parse_result(self, result: str) -> Dict:
        return loads(dumps(result, default=str))        

    def save(self, table: str, params: Dict) -> Dict:
        table = self._db[table]
        table.insert_one(params).inserted_id
        return self._parse_result(params)

    def find_one(self, table: str, by: str, value: any) -> Dict:
        if by == 'id':
            by = '_id'
        table = self._db[table]
        result = table.find_one({by:value})
        return self._parse_result(result)
