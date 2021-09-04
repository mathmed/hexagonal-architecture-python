from .http_generic_validator import HttpGenericValidator
from faker import Faker

faker = Faker()
sut = HttpGenericValidator()

def test_should_return_correct_values_on_success():
    field = faker.word()
    is_success, error_message = sut.validate([field], {field: faker.word()})
    assert is_success == True
    assert error_message is None

def test_should_return_correct_values_on_error():
    field = faker.word()
    is_success, error_message = sut.validate([field], {faker.word(): faker.word()})
    assert error_message == 'Missing required field (s): {}'.format(field)
    assert is_success == False