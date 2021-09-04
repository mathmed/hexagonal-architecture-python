from .create_user_usecase import CreateUserUsecase, CreateUserParams
from src.tests.mocks import UserRepositoryMock, HashMock
from unittest.mock import MagicMock
from faker import Faker

faker = Faker()

repository_mock = UserRepositoryMock()
hash_mock = HashMock()
sut = CreateUserUsecase(repository_mock, hash_mock)
params = CreateUserParams(faker.word(), faker.word(), faker.word(), faker.word(), faker.word(), faker.word())

def test_should_return_correct_values_if_user_already_exists():
    repository_mock.get = MagicMock(
        return_value=True
    )

    result, success = sut.create(params)

    assert result['message'] == 'User already exists'
    assert success == False


def test_should_return_correct_values_on_user_created():
    repository_mock.get = MagicMock(
        return_value=False
    )
    hash_mock.encode = MagicMock(
        return_value=faker.word()
    )
    repository_mock.save = MagicMock(
        return_value=params
    )

    result, success = sut.create(params)

    assert result['user'] == params.__dict__
    assert success == True
