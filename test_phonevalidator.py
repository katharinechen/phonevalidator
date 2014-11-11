import unittest 
from phonevalidator import phone_validator

class TestPhoneValidator(unittest.TestCase): 
    """Tests for 'phonevalidator.py'."""

    #Valid phone numbers are 10 or 11 digits
    def test_pass_with_phone_number_with_10_digits(self):
        self.assertEqual(phone_validator("1234567890"), "pass")

    def test_pass_with_phone_number_with_11_digits(self):
        self.assertEqual( phone_validator("12345678901"), "pass")

    def test_fail_with_incorrect_number_of_digits(self):
        self.assertEqual( phone_validator("123"), "fail")
        self.assertEqual( phone_validator("123123123123"), "fail")

    #Valid phone numbers may not begin with 0 
    def test_fail_with_phone_number_starting_with_zero(self):
        self.assertEqual( phone_validator("0123456789"), "fail")

    #Valid phone numbers may contain any number of spaces, dots or dashes in the right places 
    def test_pass_with_phone_number_with_spaces(self):
        self.assertEqual( phone_validator("123 456 7890"), "pass")
        self.assertEqual( phone_validator("1234 567 8901"), "pass")
        self.assertEqual( phone_validator("1 234 567 8901"), "pass")

    def test_pass_with_phone_number_with_dots(self):  
        self.assertEqual( phone_validator("123.456.7890"), "pass")
        self.assertEqual( phone_validator("1234.567.8901"), "pass")
        self.assertEqual( phone_validator("1.234.567.8901"), "pass")

    def test_pass_with_phone_number_with_dashes(self):
        self.assertEqual( phone_validator("123-456-7890"), "pass")
        self.assertEqual( phone_validator("1234-567-8901"), "pass")
        self.assertEqual( phone_validator("1-234-567-8901"), "pass")

    def test_fail_with_phone_number_with_unauthorized_symbols(self):
        self.assertEqual( phone_validator("123*456*7890"), "fail")
        self.assertEqual( phone_validator("12-34-567890"), "fail")
        self.assertEqual( phone_validator("1234---567---8901"), "fail")

if __name__ == '__main__':
    unittest.main()
