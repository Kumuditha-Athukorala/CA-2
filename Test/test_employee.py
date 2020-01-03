import unittest
from validator import Validator

validator = Validator()

class TestEmployee(unittest.TestCase):

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

