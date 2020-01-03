import unittest
from validator import Validator

validator = Validator()

class TestCustomer(unittest.TestCase):

    def test_CustomerNameValidation(self):
        name='Kuma'

        result = validator.nameValidate(name)
        self.assertTrue(result)

    def test_CustomerPhoneNumberValidation(self):
        number = '0894811893'

        result = validator.numberValidate(number)
        self.assertTrue(result)
