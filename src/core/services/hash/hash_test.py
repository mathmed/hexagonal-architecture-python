from .hash import Hash
from faker import Faker
import os

faker = Faker()
sut = Hash()

os.environ['PASSWORD_ENCRYPT_SALT'] = faker.word()

def test_should_return_a_valid_string_on_success():
    size_encrypt = 44  
    string = faker.word()
    result = sut.encode(string)
    assert len(result) == size_encrypt
