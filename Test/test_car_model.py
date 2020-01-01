import unittest
from validator import Validator

class TestCarModel(unittest.TestCase):

    def test_CarModelNameValidation(self):
        carModel = 'Sedan'
        validator =Validator()

        result = validator.nameValidate(carModel)
        self.assertTrue(carModel)

    def test_CarModelTypeValidation(self):
        modelType='X-3'
        validator = Validator()

        result = validator.nameValidate(modelType)
        self.assertTrue(result)

    def test_CarPricevalidation(self):
        price=1200000
        validator = Validator()

        result = validator.numberValidate(price)
        self.assertTrue(result)

    def test_YearValidation(self):
        year = 2019
        validator = Validator()

        result = validator.numberValidate(year)
        self.assertTrue(result)
