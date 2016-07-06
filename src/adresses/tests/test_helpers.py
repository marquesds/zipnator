from django.test import TestCase
from adresses import InvalidZipcodeException
from adresses.helpers import validate_zipcode


class HelpersTest(TestCase):
    def test_validate_zipcode(self):
        zipcode1 = '04917-080'
        zipcode2 = '04917080'
        self.assertEqual(zipcode1, validate_zipcode(zipcode1))
        self.assertEqual(zipcode2, validate_zipcode(zipcode2))


    def test_raise_exception_invalid_zipcode(self):
        zipcode1 = '04917-08'
        zipcode2 = '0491-080'
        zipcode3 = '0491708'
        with self.assertRaises(InvalidZipcodeException):
            validate_zipcode(zipcode1)
        with self.assertRaises(InvalidZipcodeException):
            validate_zipcode(zipcode2)
        with self.assertRaises(InvalidZipcodeException):
            validate_zipcode(zipcode3)
