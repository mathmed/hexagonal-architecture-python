from src.core.errors import UserNotFoundError
from src.core.ports.primary import SigninParams, SigninPort
from src.core.contracts import UserRepositoryContract, HashContract
from typing import Dict, Tuple

class SigninUsecase(SigninPort):

    def __init__(
        self,
        user_repository: UserRepositoryContract,
        hash_service: HashContract
    ):
        self.user_repository = user_repository
        self.hash_service = hash_service

    def signin(self, params: SigninParams) -> Tuple[Dict, bool]:

        try:
            user = self.user_repository.get('username', params.username)
            hashed_password = self.hash_service.encode(params.password)
            if hashed_password != user.password:
                return {'message': 'Username/password invalid'}, False

            del user.password
            return {'user': user.__dict__}, True

        except UserNotFoundError:
            return {'message': 'Username/password invalid'}, False
