from .signin_usecase import SigninUsecase, SigninParams
from src.tests.mocks import UserRepositoryMock, HashMock
from src.core.errors import UserNotFoundError
from src.core.models import UserModel
from unittest.mock import MagicMock
from faker import Faker

faker = Faker()

repository_mock = UserRepositoryMock()
hash_mock = HashMock()
sut = SigninUsecase(repository_mock, hash_mock)
params = SigninParams(faker.word(), faker.word())

def throw_user_not_found(args, args2):
    raise UserNotFoundError()

def test_should_throw_if_user_not_exists():
    repository_mock.get = MagicMock()
    repository_mock.get.side_effect = throw_user_not_found
    result, success = sut.signin(params)
    assert result['message'] == 'Username/password invalid'
    assert success == False


def test_should_return_error_on_invalid_password():
    repository_mock.get = MagicMock(
        return_value=UserModel(faker.word(), faker.word(), faker.word(), faker.word())
    )
    result, success = sut.signin(params)
    assert result['message'] == 'Username/password invalid'
    assert success == False


def test_should_return_success_on_valida_password():
    password = faker.word()
    user = UserModel(faker.word(), password, faker.word(), faker.word())
    repository_mock.get = MagicMock(
        return_value=user
    )
    hash_mock.encode = MagicMock(
        return_value=password
    )
    result, success = sut.signin(params)
    assert result['user'] == user.__dict__
    assert success == True
