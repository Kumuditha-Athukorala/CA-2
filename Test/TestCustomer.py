import unittest
from validator import Validator

class TestCustomer(unittest.TestCase):

    def test_CustomerDetails(self):
        firstName = 'Kuma'
        validator = Validator()

        result = validator.customerDetailsValidate(firstName)
        self.assertTrue(result)