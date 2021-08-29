from src.core.ports.primary import CreateUserPort, CreateUserParams
from src.core.contracts import UserRepositoryContract, SaveUserParams

class CreateUserUsecase(CreateUserPort):

    def __init__(
        self,
        save_user: UserRepositoryContract
    ):
        self.save_user = save_user

    def create(self, params: CreateUserParams) -> str:
        saved_user = self.save_user.save(
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
