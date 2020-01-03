import unittest
from validator import Validator

validator = Validator()

class TestManufacturer(unittest.TestCase):

    def test_ManufacturerNameValidation(self):
        name = 'Audi'

        result = validator.nameValidate(name)
        self.assertTrue(result)

    def test_ManufacturerAddressValidation(self):
        address='No.4, Portland St, Dublin 09'

        result = validator.addrValidate(address)
        self.assertTrue(result)

    def test_ManufacturerEmailValidation(self):
        email='kuma@gmail.com'

        result = validator.emailValidate(email)
        self.assertTrue(result)

    def test_ManufacturerContactNumberValidation(self):
        number='0894991111'
        
        result = validator.numberValidate(number)
        self.assertTrue(result)