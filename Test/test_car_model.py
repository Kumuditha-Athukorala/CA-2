import unittest
from validator import Validator

validator = Validator()

class TestCarModel(unittest.TestCase):

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
