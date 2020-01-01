import unittest
from validator import Validator

class TestEmployee(unittest.TestCase):

    def test_EmplyeeNameValidation(self):
        name='Nick'
        validator = Validator()

        result = validator.nameValidate(name)
        self.assertTrue(result)

    def test_EmplyeeDesignationValidation(self):
        designation='Manager'
        validator = Validator()

        result = validator.nameValidate(designation)
        self.assertTrue(result)

    def test_EmployeePPSNValidation(self):
        ppsn='2099111'
        validator = Validator()

        result = validator.numberValidate(ppsn)
        self.assertTrue(result)

    def test_EmployeeSalaryValidation(self):
        salary='2500'
        validator = Validator()

        result = validator.numberValidate(salary)
        self.assertTrue(result)

