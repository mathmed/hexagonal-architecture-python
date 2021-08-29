from src.core.ports.primary import CreateUserPort, CreateUserParams
from src.core.contracts import UserRepositoryContract, SaveUserParams, HashContract
from typing import Dict

class CreateUserUsecase(CreateUserPort):

    def __init__(
        self,
        user_repository: UserRepositoryContract,
        hash_service: HashContract
    ):
        self.user_repository = user_repository
        self.hash_service = hash_service

    def create(self, params: CreateUserParams) -> Dict:
        
        username_exists = self.user_repository.get('username', params.username, False)
        email_exists = self.user_repository.get('email', params.email, False)

        if username_exists or email_exists:
            return 'User already exists'

        hashed_password = self.hash_service.encode(params.password)

        saved_user = self.user_repository.save(
            SaveUserParams(
                params.username,
                hashed_password,
                params.name,
                params.email,
                params.profile_image_url,
                params.bio
            )
        )

        del saved_user.password
        return saved_user.__dict__
