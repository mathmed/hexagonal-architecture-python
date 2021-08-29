from src.core.contracts import HashContract
import os
import hashlib
import base64

class Hash(HashContract):
    def encode(self, string: str) -> str:
        salt = os.getenv('PASSWORD_ENCRYPT_SALT')
        string = base64.b64encode(hashlib.pbkdf2_hmac('sha256', string.encode('utf-8'), salt.encode(), 100000)).decode('utf-8')
        return string
