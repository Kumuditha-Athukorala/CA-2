import unittest
from validator import Validator

class TestCustomer(unittest.TestCase):

    def test_CustomerNameValidation(self):
        name='Kuma'
        validator = Validator()

        result = validator.nameValidate(name)
        self.assertTrue(result)

    def test_CustomerPhoneNumberValidation(self):
        number = '0894811893'
        validator = Validator()

        result = validator.numberValidate(number)
        self.assertTrue(result)