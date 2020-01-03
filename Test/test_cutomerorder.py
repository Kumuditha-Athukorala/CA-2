import unittest
from validator import Validator

class TestCustomerOrder(unittest.TestCase):

    def test_CustomerOrderDateValidation(self):
        date = '2019-12-12'
        validator = Validator()

        result = validator.dateValidate(date)
        self.assertTrue(result)

    def test_CustomerOrderDeliveryDateValidation(self):
        date = '2019-12-12'
        validator = Validator()

        result = validator.dateValidate(date)
        self.assertTrue(result)

    def test_CustomerOrderSellingPriceValidation(self):
        price = '567'
        validator = Validator()
        result = validator.priceValidate(price)
        self.assertTrue(result)