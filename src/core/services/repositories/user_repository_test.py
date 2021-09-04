from .user_repository import UserRepository
from src.tests.mocks import DatabaseMock
from src.core.contracts import SaveUserParams
from src.core.errors import UserNotFoundError
from unittest import TestCase
from unittest.mock import MagicMock
from faker import Faker

faker = Faker()
database_mock = DatabaseMock()
sut = UserRepository(database_mock)

def test_should_save_a_user_correctly():
    user = SaveUserParams(faker.word(), faker.word(), faker.word(), faker.word(), faker.word(), faker.word())
    database_mock.save = MagicMock(
        return_value=user.__dict__
    )
    result = sut.save(user)
    TestCase().assertDictEqual(user.__dict__, result.__dict__)


def test_should_throw_error_on_get_user_not_found():
    database_mock.find_one = MagicMock(
        return_value=None
    )
    with TestCase().assertRaises(UserNotFoundError):
        sut.get(faker.word(), faker.word())

def test_should_return_correct_user_on_get_user_success():
    user = SaveUserParams(faker.word(), faker.word(), faker.word(), faker.word(), faker.word(), faker.word())
    database_mock.find_one = MagicMock(
        return_value=user.__dict__
    )
    result = sut.get(faker.word(), faker.word())
    TestCase().assertDictEqual(user.__dict__, result.__dict__)
