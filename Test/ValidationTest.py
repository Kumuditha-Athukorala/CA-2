import unittest
from validator import Validator

class TestCustomer(unittest.TestCase):

    def test_CustomerDetails(self):
        firstName = 'Kuma'
        validator = Validator()

        result = validator.customerDetailsValidate(firstName)
        self.assertTrue(result)

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
