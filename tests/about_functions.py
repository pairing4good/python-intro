import unittest

from app.functions_library import *

__ = False


class AboutFunctions(unittest.TestCase):

    def test_function_creation(self):
        assert say_hi() == 'hi'

    def test_write_concatenation_function(self):
        assert concatenate('abc', 'def') == 'abcdef'

    def test_write_get_day_difference_function(self):
        # Lets represent every day of the year with an integer
        # The first of January is 1
        # The second of January is 2
        # ...and so on till...
        # The the last day of December is 365
        # (We ignore leap years)

        # Using this representation write a function that gives the
        # day difference between two dates

        assert get_day_difference(34, 254) == 220

    def test_write_get_age_in_2050_function(self):
        assert get_age_in_2050(34) == 70

    ##############################
    # Conversion functions
    ##############################

    def test_write_convert_to_celsius_function(self):
        # To calculate celsius from fahrenheit:
        # Subtract 32 from fahrenheit, then
        # multiply the result by 5 and divide by 9

        # Use int() to round down to the closest integer.
        # For example if you have 26.666, int(26.666) returns 26

        assert convert_to_celsius(80) == 26

    def test_write_convert_kilometers_to_miles_function(self):
        # one mile is equal to 1.6 kilometers

        miles = convert_to_miles(34)
        self.assertAlmostEqual(miles, 54.4, 1)
