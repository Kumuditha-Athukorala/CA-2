import unittest
from validator import Validator

class ValidationTest(unittest.TestCase):

    def test_NameValidator(self):
        name = 'kuma'
        validator = Validator()

        result = validator.nameValidate(name)
        self.assertTrue(result)

    def test_AddressValidator(self):
        address = ''
        validator = Validator()

        result = validator.addrValidate(address)
        self.assertTrue(result)

    def test_EmailValodator(self):
        email = 'kuma@gmail.com'
        validator = Validator()

        result = validator.emailValidate(email)
        self.assertTrue(result)

    def test_NumberValidator(self):
        number = ''
        validator = Validator()

        result = validator.numberValidate(number)
        self.assertTrue(result)

    