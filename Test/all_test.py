import unittest
from validator import Validator

validator = Validator()

class AllTest(unittest.TestCase):

#Catmodel Test Cases
    def test_CarModelNameValidation(self):
        carModel = 'Sedan'

        result = validator.nameValidate(carModel)
        self.assertTrue(result)

    def test_CarModelTypeValidation(self):
        modelType='X-3'

        result = validator.nameValidate(modelType)
        self.assertTrue(result)

    def test_CarPricevalidation(self):
        price=1200000

        result = validator.numberValidate(price)
        self.assertTrue(result)

    def test_YearValidation(self):
        year = 2019

        result = validator.numberValidate(year)
        self.assertTrue(result)


#Customer Test Cases
    def test_CustomerNameValidation(self):
        name='Kuma'

        result = validator.nameValidate(name)
        self.assertTrue(result)

    def test_CustomerPhoneNumberValidation(self):
        number = '0894811893'

        result = validator.numberValidate(number)
        self.assertTrue(result)

#Customer Order Test Cases

    def test_CustomerOrderDateValidation(self):
        date = '2019-12-12'

        result = validator.dateValidate(date)
        self.assertTrue(result)

    def test_CustomerOrderDeliveryDateValidation(self):
        date = '2019-12-12'

        result = validator.dateValidate(date)
        self.assertTrue(result)

    def test_CustomerOrderSellingPriceValidation(self):
        price = '567'

        result = validator.priceValidate(price)
        self.assertTrue(result)

#Employee Test Cases

    def test_EmplyeeNameValidation(self):
        name='Nick'

        result = validator.nameValidate(name)
        self.assertTrue(result)

    def test_EmplyeeDesignationValidation(self):
        designation='Manager'

        result = validator.nameValidate(designation)
        self.assertTrue(result)

    def test_EmployeePPSNValidation(self):
        ppsn='2099111AS'

        result = validator.validatePPS(ppsn)
        self.assertTrue(result)

    def test_EmployeeSalaryValidation(self):
        salary=2500

        result = validator.numberValidate(salary)
        self.assertTrue(result)

#Manufacturer Test cases

def test_ManufacturerNameValidation(self):
    name = 'Audi'

    result = validator.nameValidate(name)
    self.assertTrue(result)


def test_ManufacturerAddressValidation(self):
    address = 'No.4, Portland St, Dublin 09'

    result = validator.addrValidate(address)
    self.assertTrue(result)


def test_ManufacturerEmailValidation(self):
    email = 'kuma@gmail.com'

    result = validator.emailValidate(email)
    self.assertTrue(result)


def test_ManufacturerContactNumberValidation(self):
    number = '0894991111'

    result = validator.numberValidate(number)
    self.assertTrue(result)

