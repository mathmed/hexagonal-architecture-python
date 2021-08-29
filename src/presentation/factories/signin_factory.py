from src.core.usecases import SigninUsecase
from src.core.services.repositories import UserRepository
from src.core.services.hash import Hash
from src.core.ports.primary import SigninPort
from src.infra.database import PyMongoAdapter

def signin_factory() -> SigninPort:
    pymongo = PyMongoAdapter()
    hash = Hash()
    user_repository = UserRepository(pymongo)
    return SigninUsecase(user_repository, hash)
