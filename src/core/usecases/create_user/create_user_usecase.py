from src.core.ports.primary import CreateUserPort, CreateUserParams
from src.core.contracts import UserRepositoryContract, SaveUserParams

class CreateUserUsecase(CreateUserPort):

    def __init__(
        self,
        user_repository: UserRepositoryContract
    ):
        self.user_repository = user_repository

    def create(self, params: CreateUserParams) -> str:

        username_exists = self.user_repository.get('username', params.username, False)
        email_exists = self.user_repository.get('email', params.email, False)

        if username_exists or email_exists:
            return 'User already exists'

        saved_user = self.user_repository.save(
            SaveUserParams(
                params.username,
                params.password,
                params.name,
                params.email,
                params.profile_image_url,
                params.bio
            )
        )
        return saved_user
