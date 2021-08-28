from src.core.usecases import CreateUserUsecase
from src.core.services.repositories import UserRepository
from src.core.ports.primary import CreateUserPort
from src.infra.database import PyMongoAdapter

def create_user_factory() -> CreateUserPort:
    pymongo = PyMongoAdapter()
    user_repository = UserRepository(pymongo)
    return CreateUserUsecase(user_repository)
